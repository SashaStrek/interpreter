"""
An attempt to implement a local interpreter.
A. Strekalovskiy, 11 March 2025
"""

import subprocess
import whisper
from transformers import pipeline


def record_audio(duration=5, output_file="temp_audio.wav"):
    """
    Uses ffmpeg to capture audio from the default input device (your earbuds).
    """
    # Record using ffmpeg
    command = [
        "ffmpeg",
        "-y",  # overwrite
        "-f", "avfoundation",  # for macOS
        "-i", ":0",  # default input device
        "-t", str(duration),
        output_file
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_file

def transcribe_audio(file_path):
    model = whisper.load_model("small")  # small / medium / large
    result = model.transcribe(file_path, language="en")  # or "en" if you want English
    return result["text"]

def translate_en_to_fr(text):
    # Initialize the translation pipeline for English-to-French
    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    translation = translator(text)
    return translation[0]["translation_text"]

def translate_fr_to_en(text):
    # Initialize the translation pipeline for French-to-English
    translator = pipeline("translation_fr_to_en", model="Helsinki-NLP/opus-mt-en-fr")
    translation = translator(text)
    return translation[0]["translation_text"]

# ~~~~~~~~~~~~~
def speak_french(text):
    # "Thomas" is one of the French voices available on macOS.
    subprocess.run(["say", "-v", "Thomas", text])

if __name__ == "__main__":
    # en_to_fr pipeline
    # Listen to English and Transcribe
    audio_file = record_audio(5)  # 5 seconds of audio
    english_text = transcribe_audio(audio_file)
    # Print Transcribe English
    print("Transcribed text:", english_text)
    # Translate en_to_French
    french_translation = translate_en_to_fr(english_text)
    print("Translated to French:", french_translation)
    # Spell French text
    speak_french(french_translation)
