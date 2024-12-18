import pygame

    
pygame.init()
pygame.mixer.init()

IMAGES = "images/"
SOUNDS = "sounds/"

walkRight = [pygame.image.load(IMAGES + f'R{i}.png') for i in range(1, 7)]
walkLeft = [pygame.image.load(IMAGES + f'L{i}.png') for i in range(1, 7)]
DwalkRight = [pygame.image.load(IMAGES + f'DR{i}.png') for i in range(1, 7)]
DwalkLeft = [pygame.image.load(IMAGES + f'DL{i}.png') for i in range(1, 7)]
game_bg = pygame.image.load(IMAGES + 'game_bg.png')
charHR = pygame.image.load(IMAGES + 'RBS.png')
charHL = pygame.image.load(IMAGES + 'LBS.png')
charDR = pygame.image.load(IMAGES + 'DRstanding.png')
charDL = pygame.image.load(IMAGES + 'DLstanding.png')
menu_bg= pygame.image.load(IMAGES + 'menu_bg.png')

pygame.mixer.music.load(SOUNDS + "bgs.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

projectile_sound = pygame.mixer.Sound(SOUNDS + "projectile.wav")  
projectile_sound.set_volume(0.1)