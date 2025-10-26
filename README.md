🤖 AI Voice & Text Converter

This project is an interactive Python application that allows users to convert text to speech and speech to text in French.
It uses gTTS for text-to-audio conversion, PyDub for audio handling and playback, and SpeechRecognition for audio transcription.
Users can either type a message to hear it spoken or record their voice to get a transcription.

Features

✅ Text → Audio conversion (plays audio directly without saving to a file)

✅ Audio → Text conversion using microphone recording

✅ Supports MP3/WAV playback and recording

✅ Simple interactive menu

Requirements

All dependencies are listed in requirements.txt. To install them, run:

pip install -r requirements.txt

Main Packages

gTTS → Convert text to speech

pydub → Audio manipulation and playback

speechrecognition → Convert recorded audio to text

sounddevice → Record audio from microphone

soundfile → Save recorded audio temporarily

How to Run

Clone the repository:

git clone https://github.com/HadilBoussensla/AI-Text-Voice-Converter.git
cd your-repo


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Follow the interactive menu to choose:

1 → Convert text to audio

2 → Record voice and get transcription

Project Structure
ai-voice-text-converter/
 ┣ app.py              # Main script
 ┣ requirements.txt    # Dependencies
 ┣ .gitignore          # Ignored files
 ┗ README.md           # Project documentation

License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.

Author

Developed by Hadil Boussensla 🚀
Focused on AI, speech processing, and interactive Python applications.
