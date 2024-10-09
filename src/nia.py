from src.audio import AudioManager
from src.voice_recognition import VoiceRecognizer
import speech_recognition as sr
import pygame
import threading

class Nia:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(3)  # Permitir hasta 2 canales de audio
        self.audio_manager = AudioManager()
        self.voice_recognizer = VoiceRecognizer()
        self.greeting_audio = r"Audio\Saludo Inicio.mp3"
        self.response_audio = r"Audio\Dime.mp3"
        self.farewell_audio = r"Audio\Adios.mp3"
        self.running = True
        self.active = False
        self.greet()
        threading.Thread(target=self.listen_for_name, daemon=True).start()  # Hilo de escucha activa

    def greet(self):
        self.audio_manager.play_audio(self.greeting_audio)

    def listen_for_name(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            while self.running:
                if not self.active:
                    audio = self.voice_recognizer.listen(source)
                    try:
                        command = self.voice_recognizer.recognize(audio)
                        if command and "oye niña" in command:
                            self.active = True
                            threading.Thread(target=self.respond).start()  # Hilo para responder
                    except Exception as e:
                        print(f"Error al reconocer el nombre: {e}")

    def respond(self):
        pygame.mixer.music.load(self.response_audio)
        pygame.mixer.music.play()
        
        
        with sr.Microphone() as source:
            print("Escuchando tu comando...")
            audio = self.voice_recognizer.listen(source)
            try:
                command = self.voice_recognizer.recognize(audio)
            except Exception as e:
                print(f"Error al reconocer el comando: {e}")
                self.active = False  # Desactiva la escucha
                return

            if command:
                print(f"Comando escuchado: {command}")

                if "hola" in command:
                    print("oka")

        self.active = False  # Vuelve a estar lista para escuchar
        print("Nia está lista para escuchar nuevamente.")

    def stop(self):
        self.running = False
        print("Nia se está deteniendo...")
