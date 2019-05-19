import pygame, config, platforma
pygame.init()

class Level(object):
    def __init__(self,player):
        self.lista_platform = pygame.sprite.Group()
        self.player = player
        self.p_x = 0
    def update(self):
        self.lista_platform.update()
    def display(self, win):
        win.fill(config.K_niebo)
        self.lista_platform.draw(win)
    def przesuniecie_x(self, roznica_graniczna):
        self.p_x += roznica_graniczna
        for platform in self.lista_platform:
            platform.rect.x += roznica_graniczna
class First(Level):
    def __init__(self, player):
        super().__init__(player)
        pos = platforma.Platform()
        pozycje = pos.lvl1()
        for i in pozycje:
            plat = platforma.Platform()
            plat.rect.x = i[0]
            plat.rect.y = i[1]
            self.lista_platform.add(plat)