from flask import Flask, request, render_template
import os
from extractors.pdf_extractor import extract_text_from_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for uploading and processing PDF
@app.route('/', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if not file.filename.lower().endswith('.pdf'):
            return "Invalid file format. Only PDF files are allowed.", 400
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            extracted_data = extract_text_from_pdf(filepath)
            return render_template("parsed_resume.html", extracted_data=extracted_data)
    
    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug=True, port=50033)
