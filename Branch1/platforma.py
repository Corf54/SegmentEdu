import pygame, config
pygame.init()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = config.platforma
        self.rect = self.image.get_rect()
    def lvl1(self):
        pozycje_plik = open("poziomy\LVL_1\platforms.map").read()
        lista = list(pozycje_plik.split())
        lista = list(map(int,lista))
        pozycje = []
        for i in range(0,len(lista),2):
            podlista = []
            podlista.append(lista[i])
            podlista.append(lista[i+1])
            pozycje.append(podlista)
        return pozycje