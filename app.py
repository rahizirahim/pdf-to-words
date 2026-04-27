from flask import Flask, render_template, request, send_file, jsonify
import os
from pdf2docx import Converter
from pdf2image import convert_from_path
import pytesseract
from docx import Document
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Path untuk Tesseract dan Poppler
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\poppler\Library\bin'

def is_scanned_pdf(pdf_path):
    try:
        cv = Converter(pdf_path)
        cv.close()
        return False
    except:
        return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['pdf_file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Please upload a PDF file'}), 400

    unique_id = str(uuid.uuid4())
    pdf_path = os.path.join(UPLOAD_FOLDER, f'{unique_id}.pdf')
    docx_filename = file.filename.replace('.pdf', '.docx')
    docx_path = os.path.join(OUTPUT_FOLDER, f'{unique_id}.docx')

    file.save(pdf_path)

    try:
        # Check dulu ada text ke tak dalam PDF
        import fitz
        pdf_doc = fitz.open(pdf_path)
        has_text = any(page.get_text().strip() for page in pdf_doc)
        pdf_doc.close()

        if has_text:
            # PDF biasa — guna pdf2docx
            cv = Converter(pdf_path)
            cv.convert(docx_path)
            cv.close()
        else:
            # Scanned PDF — guna OCR
            images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
            doc = Document()
            for img in images:
                text = pytesseract.image_to_string(img)
                doc.add_paragraph(text)
                doc.add_page_break()
            doc.save(docx_path)

    except Exception as e:
        return jsonify({'error': f'Conversion failed: {str(e)}'}), 500
    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    return send_file(
        docx_path,
        as_attachment=True,
        download_name=docx_filename,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__ == '__main__':
    app.run(debug=True)