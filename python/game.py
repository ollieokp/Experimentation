import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("smily pong")
keepGoing = True
pic = pygame.image.load("Crazysmyle.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
white = (255,255,255)
