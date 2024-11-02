import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties like volume and speaking rate
engine.setProperty('rate', 140)  # Adjust this value for speed
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to convert text to speech (no file saving)
def audio_direct(text):
    engine.say(text)
    engine.runAndWait()  # Wait for the speech to complete

# Example usage to check the audio output
text = "This is a test speech to check audio output."
audio_direct(text)
