import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Inicializa el reconocedor de voz

    def listen(self, source):
        audio = self.recognizer.listen(source)  # Escucha el audio
        return audio

    def recognize(self, audio):
        try:
            command = self.recognizer.recognize_google(audio, language='es-ES').lower()  # Reconoce el texto en español
            return command
        except sr.UnknownValueError:
            return None  # Ignora si no entiende
        except sr.RequestError as e:
            print(f"Error en el servicio de reconocimiento de voz: {e}")
            return None
