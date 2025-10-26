from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf

# ---------------- TEXTE -> AUDIO ----------------
def text_to_audio(text):
    """Convertit un texte en audio et le joue directement sans fichier temporaire."""
    tts = gTTS(text=text, lang='fr')
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    audio = AudioSegment.from_file(audio_buffer, format="mp3")
    play(audio)
    print("🎧 Le texte a été converti et joué directement.")

# ---------------- AUDIO -> TEXTE ----------------
def record_and_recognize(duration=5, fs=44100):
    """Enregistre la voix pendant `duration` secondes et renvoie la transcription."""
    print(f"🎙️ Enregistrement pour {duration} secondes...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Attendre la fin de l'enregistrement
    
    # Sauvegarder en mémoire pour SpeechRecognition
    audio_file = "temp_audio.wav"
    sf.write(audio_file, recording, fs)
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        print(f"🗣️ Vous avez dit : {text}")
        return text
    except sr.UnknownValueError:
        print("⚠️ Impossible de comprendre l'audio.")
        return None
    except sr.RequestError:
        print("⚠️ Service de reconnaissance vocale indisponible.")
        return None

# ---------------- MENU INTERACTIF ----------------
mode = input("Choisissez le mode (1 = Texte -> Audio, 2 = Audio -> Texte) : ")

if mode.strip() == "1":
    user_text = input("Entrez le texte à convertir en audio : ")
    text_to_audio(user_text)
elif mode.strip() == "2":
    transcription = record_and_recognize()
    if transcription:
        print("✅ Transcription terminée :", transcription)
else:
    print("⚠️ Mode invalide.")
