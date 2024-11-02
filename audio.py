from gtts import gTTS
import threading
import os

# Function to convert text to speech and save it as an .mp3 file
def audio(text, file_path):
    def speak():
        # Check if the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create directory if it doesn't exist

        # Generate and save audio file
        if not os.path.exists(file_path):
            tts = gTTS(text=text, lang='en')
            tts.save(file_path)

    # Start TTS in a thread so the UI doesn't block
    tts_thread = threading.Thread(target=speak)
    tts_thread.start()

# Function to stop speech (not applicable in gTTS, included for consistency)
def stop_audio():
    pass  # gTTS does not support stopping speech dynamically
