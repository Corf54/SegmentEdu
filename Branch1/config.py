import pygame
pygame.init()

K_czionkaMenu = (0,128,0)
K_czarny = (0,0,0)
K_niebo = (151,196,229)

Menu_i = pygame.image.load("obrazy/MainMenu.jpg")
opcja = pygame.image.load("obrazy/Option.png")
death = pygame.image.load("obrazy/death.png")

gracz_lewo = [pygame.image.load("tex/chodzenie/lewochod0.png"), pygame.image.load("tex/chodzenie/lewochod1.png"), pygame.image.load("tex/chodzenie/lewochod2.png")]
gracz_prawo = [pygame.image.load("tex/chodzenie/prawochod0.png"), pygame.image.load("tex/chodzenie/prawochod1.png"), pygame.image.load("tex/chodzenie/prawochod2.png")]

platforma = pygame.image.load("tex/dol.png")

menu_font = pygame.font.Font("fonts/Bloomer DEMO.otf", 23)


win_x = 1000
win_y = 600

p_predkosc = 5

