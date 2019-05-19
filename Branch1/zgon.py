import pygame, config
pygame.init()

class koniec(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = config.death
        self.rect = self.image.get_rect()

        self.image.blit(config.opcja, (444,350))
        zgon_napis = config.menu_font.render("BACK", True, config.K_czionkaMenu)
        self.image.blit(zgon_napis, (477, 355))

