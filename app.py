from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils import extract_text_from_file
from hugging_face_service import classify_email, generate_response

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        email_text = request.form.get('email_text', '')

        if not email_text and 'email_file' in request.files:
            file = request.files['email_file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                email_text = extract_text_from_file(filepath)

        if email_text:
            category = classify_email(email_text)
            response = generate_response(email_text, category)
            result = {
                'text': email_text,
                'category': category,
                'response': response
            }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)