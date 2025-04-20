import pyttsx3

def text_to_speech(text,filename="output_audio.wav",
                   rate=150,volume=1.0,voice_id=None):
    engine = pyttsx3.init()
    
    engine.setProperty('rate',rate)
    engine.setProperty('volume',volume)
    
    voices = engine.getProperty('voices')
    
    if voice_id is not None and 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        engine.setProperty('voice' , voices[0].id)
    
    engine.save_to_file(text, filename)
    engine.say(text)
    engine.runAndWait()
    print(f"Audio file saved as {filename}")

if __name__ == "__main__":
    input_text = input("Enter text you want to convert to audio:\n")
    print("Processing...")
    text_to_speech(input_text) 