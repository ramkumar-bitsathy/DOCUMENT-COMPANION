import pyttsx3
import threading
import os

# Initialize the TTS engine globally
engine = pyttsx3.init()

# Set properties like volume and speaking rate
engine.setProperty('rate', 100)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to convert text to speech and save it as a .wav file
def audio(text, file_path):
    def speak():
        # Check if the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create directory if it doesn't exist

        # Generate and save audio file
        if not os.path.exists(file_path):
            engine.save_to_file(text, file_path)
            engine.runAndWait()

    # Start TTS in a thread so the UI doesn't block
    tts_thread = threading.Thread(target=speak)
    tts_thread.start()

# Function to stop speech
def stop_audio():
    engine.stop()
