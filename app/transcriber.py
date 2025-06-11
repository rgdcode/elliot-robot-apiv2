import speech_recognition as sr

def transcribir_audio(path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Texto transcrito: {texto}")
        return texto
    except sr.UnknownValueError:
        return "No se entendió el audio."
    except sr.RequestError as e:
        return f"Error al conectar con Google: {e}"

