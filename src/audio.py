import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

    def play_audio(self, audio_file):
        sound = pygame.mixer.Sound(audio_file)
        channel = pygame.mixer.find_channel()
        if channel:  # Si hay un canal disponible
            channel.play(sound)

    def stop_audio(self):
        pygame.mixer.stop()
