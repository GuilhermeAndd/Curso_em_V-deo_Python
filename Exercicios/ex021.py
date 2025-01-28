import pygame

# Inicializar pygame
pygame.mixer.init()

# Cargar el archivo de audio
pygame.mixer.music.load("mario_jump.mp3")

# Reproducir el audio
pygame.mixer.music.play()

# Mantener el script ejecutándose hasta que termine el audio
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)