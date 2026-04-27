# 📄➡️📝 PDF to Word Converter

A simple web app that converts PDF files to Word (.docx) documents instantly.

## 🚀 Features

- Drag & drop or browse to upload PDF
- Converts to Word (.docx) format
- Clean and simple web interface
- Runs locally on your computer

## 🛠️ Tech Stack

- **Python** + **Flask** (backend)
- **pdf2docx** (conversion library)
- **HTML / CSS / JavaScript** (frontend)

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/pdf-to-word.git
cd pdf-to-word
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
Go to: [http://localhost:5000](http://localhost:5000)

## 📁 Project Structure

```
pdf-to-word/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Frontend UI
├── uploads/             # Temp PDF storage (auto-created)
├── outputs/             # Converted files (auto-created)
└── README.md
```

## 📌 Notes

- Only PDF files are supported as input
- Converted files are saved temporarily and served for download
- Works best with text-based PDFs (not scanned images)

## 🌐 Live Demo
👉 [Click here to use the app](https://pdf-to-words.onrender.com/)


Made with ❤️ using Python & Flask
