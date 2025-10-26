# 🤖 AI Text & Voice Converter

## Description
This Python project allows users to convert text to speech (TTS) and speech to text (STT). 
It uses **gTTS** for TTS, **pydub** for audio playback, **sounddevice** and **soundfile** for recording, and **SpeechRecognition** for transcribing audio.

### Features
- Text → Audio (plays directly without saving)
- Audio → Text (records and transcribes voice)
- Interactive command-line interface
- In-memory audio playback (no temporary files)

### Tech Stack
- Python 3.8+
- gTTS
- Pydub
- SoundDevice
- SoundFile
- SpeechRecognition

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/AI_Text_Voice_Converter.git
cd AI_Text_Voice_Converter

Install dependencies:

pip install -r requirements.txt

Usage
python app.py


Choose mode 1 for Text → Audio

Choose mode 2 for Audio → Text

Project Structure
📦 AI_Text_Voice_Converter
 ┣ 📜 app.py             # Main script with TTS & STT
 ┣ 📜 requirements.txt   # Dependencies
 ┣ 📜 .gitignore         # Ignored files
 ┗ 📜 README.md          # Documentation

License

MIT License. Free to use, modify, and distribute with attribution.

Author

Hadil Boussensla


---

## **requirements.txt**



gTTS
pydub
SpeechRecognition
sounddevice
soundfile


> ⚠️ On Windows, install **FFmpeg** and add it to your PATH for `pydub` to work.

---

## **.gitignore**



pycache/
*.pyc
*.pyo
*.pyd
*.wav
*.mp3
.env
.DS_Store
.ipynb_checkpoints/
