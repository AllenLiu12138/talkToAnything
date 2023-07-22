from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import textract
import speech_recognition as sr
from moviepy.editor import VideoFileClip
from PIL import Image
import pytesseract
import openai
import cv2
import os
import uuid
import pdfplumber

openai.api_key = "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"
app = Flask(__name__)
app.secret_key = "your_secret_key"

# In-memory "database" to store documents
documents = {}

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = " ".join(page.extract_text() for page in pdf.pages)
    return text

def extract_text_from_doc(file_path):
    text = textract.process(file_path).decode()
    return text

def extract_text_from_image(file_path):
    image = cv2.imread(file_path)
    text = pytesseract.image_to_string(Image.fromarray(image))
    return text

def transcribe_audio(file_path):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text

def extract_audio_from_video(file_path):
    clip = VideoFileClip(file_path)
    audio_file = "/tmp/" + str(uuid.uuid4()) + ".wav"
    clip.audio.write_audiofile(audio_file)
    return audio_file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    session_id = str(uuid.uuid4())
    file = request.files['file']
    file_path = os.path.join("/tmp", secure_filename(file.filename))
    file.save(file_path)

    try:
        if file.filename.endswith('.pdf'):
            content = extract_text_from_pdf(file_path)
        elif file.filename.endswith('.doc') or file.filename.endswith('.docx'):
            content = extract_text_from_doc(file_path)
        elif file.filename.endswith('.jpg') or file.filename.endswith('.png'):
            content = extract_text_from_image(file_path)
        elif file.filename.endswith('.wav'):
            content = transcribe_audio(file_path)
        elif file.filename.endswith('.mp4'):
            audio_filename = extract_audio_from_video(file_path)
            content = transcribe_audio(audio_filename)
        else:
            return jsonify({"error": "Invalid file type"}), 400

        documents[session_id] = content
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "File uploaded successfully", "session_id": session_id}), 200

def interact_with_gpt(question, session_id):
    content = documents.get(session_id)
    if content is None:
        return jsonify({"error": "No document found"}), 400

    prompt = content + "\nQuestion: " + question

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "I am the document. user will ask questions based on document. I will askwer those questions based on the information on document"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6  # Limiting the message to a shorter length
    )

    return {"role": "assistant", "content": response['choices'][0]['message']['content']}

@app.route('/interact', methods=['POST'])
def interact():
    question = request.json['message']
    session_id = request.json['session_id']
    response = interact_with_gpt(question, session_id)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
