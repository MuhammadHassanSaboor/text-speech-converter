import speech_recognition as sr

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        print("Listening to Audio...")
        audio = recognizer.record(source)
        
    
    try:
        text = recognizer.recognize_google(audio,language="en-US")
        print("Transcribed Text\n", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google API {e}")
        
if __name__ == "__main__":
    filename = "output_audio.wav"
    speech_to_text(filename)