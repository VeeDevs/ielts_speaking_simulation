import os
import whisper
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the Whisper model
model = whisper.load_model("base")  # You can use a different model if needed

# Set your OpenAI API key
OPENAI_API_KEY=your-api-key-here

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily
    audio_file_path = os.path.join('audio', file.filename)
    file.save(audio_file_path)

    # Transcribe the audio file
    transcription = transcribe_audio(audio_file_path)

    # Clean up the temporary audio file
    os.remove(audio_file_path)

    return jsonify({"transcription": transcription})


def transcribe_audio(file_path):
    # Transcribe the audio using the Whisper model
    result = model.transcribe(file_path)
    return result["text"]


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Generate a response from OpenAI's GPT model
    response = generate_chatgpt_response(user_input)
    return jsonify({"response": response})


def generate_chatgpt_response(prompt):
    try:
        # Send the prompt to OpenAI for a chatbot response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use a different model if needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    # Ensure the audio directory exists
    if not os.path.exists('audio'):
        os.makedirs('audio')

    # Run the Flask application
    app.run(debug=True)
