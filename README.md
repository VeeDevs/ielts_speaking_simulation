# IELTS Speaking Simulation App

This is an IELTS Speaking Simulation app designed to help users practice for the IELTS speaking exam. It provides real-time feedback through a chatbot, transcribes speech to text, and integrates the OpenAI API for dynamic interaction.

## Features

- **Speech-to-Text**: Converts your spoken responses to text using advanced speech recognition.
- **Chatbot Feedback**: Get personalized feedback on your responses using the OpenAI API.
- **IELTS Speaking Simulation**: Simulates IELTS speaking questions for practice, covering all parts of the exam.
- **Real-Time Interaction**: Provides instant feedback to help improve pronunciation, fluency, and grammar.
- **Recording Audio**: Records and transcribes your spoken responses for further analysis.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YourUsername/ielts_speaking_simulation.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd ielts_speaking_simulation
    ```

3. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up OpenAI API key**:
   - Obtain your API key from [OpenAI](https://platform.openai.com/signup).
   - Add it to your `app.py` or set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="your-api-key"  # On Windows, use `set OPENAI_API_KEY=your-api-key`
    ```

## Usage

1. **Run the app**:

    ```bash
    python app.py
    ```

2. Open a browser and navigate to `http://127.0.0.1:5000` to access the app.

3. Begin practicing IELTS speaking questions by speaking into the microphone. The app will transcribe your responses and provide real-time feedback.

## Dependencies

- Flask: Web framework used for the app.
- OpenAI: API client to interact with OpenAI models for feedback generation.
- SpeechRecognition: Python library to handle speech-to-text functionality.
- PyAudio: Required for recording audio.
- Whisper (optional for advanced transcription): For enhanced speech-to-text capabilities.

## API Integration

The app utilizes OpenAI's API to provide feedback on your responses. It uses GPT models to assess your speaking fluency, grammar, and pronunciation.

### Example OpenAI API request:

```python
import openai

openai.api_key = "your-api-key"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Provide feedback on the following IELTS speaking answer: [user response]",
    max_tokens=100
)

feedback = response.choices[0].text.strip()
