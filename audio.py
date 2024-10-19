# audio.py
import pyttsx3
import threading

# Initialize the TTS engine globally
engine = pyttsx3.init()

# Set properties like volume and speaking rate
engine.setProperty('rate', 250)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to convert text to speech and play it in a separate thread
def audio(text):
    def speak():
        engine.say(text)
        engine.runAndWait()

    # Start TTS in a thread so the UI doesn't block
    tts_thread = threading.Thread(target=speak)
    tts_thread.start()

# Function to stop speech
def stop_audio():
    engine.stop()
