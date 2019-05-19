import pygame, config
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self ,x ,y):
        super().__init__()
        self.graczprawo = config.gracz_prawo

        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300

        self.delta_x = 0
        self.delta_y = 0

        self.delta_jump = 10
        self.is_grounded = None
        self.is_dead = False

        self.poziom = None

    def prawo(self):
        self.delta_x = config.p_predkosc

    def lewo(self):
        self.delta_x = -config.p_predkosc

    def stop(self):
        self.delta_x = 0

    def skok(self):
        if self.is_grounded == True:
            self.delta_y = -10
    def zgon(self):
        if self.is_dead == False:
            return False
        if self.is_dead == True:
            return True
    def update(self):
        # SPRAWDZA ORAZ MODYFIKUJE CO KLATKĘ STAN GRACZA
        # AKTUALIZUJE POZYCJE WERTKALNĄ I HORYZONTALNĄ:
        # KOLIZJE I PRZEMIESZCZENIE:
        if self.is_dead == False:
            self.rect.x += self.delta_x
            kolizje = pygame.sprite.spritecollide(self, self.poziom.lista_platform, False)
            for kolizja_x in kolizje:
                if self.delta_x > 0:
                    self.rect.right = kolizja_x.rect.left
                elif self.delta_x < 0:
                    self.rect.left = kolizja_x.rect.right
            self.rect.y += self.delta_y
            kolizje = pygame.sprite.spritecollide(self, self.poziom.lista_platform, False)
            for kolizja_y in kolizje:
                if self.delta_y > 0:
                    self.rect.bottom = kolizja_y.rect.top
                elif self.delta_y < 0:
                    self.rect.top = kolizja_y.rect.bottom
                self.delta_y = 0
            # TEST NA GLEBE :D
            if len(kolizje) > 0 and self.delta_y == 0:
                self.is_grounded = True
            else:
                self.is_grounded = False
            # GRAWITACJA
            if self.delta_y == 0:
                self.delta_y = 1
            else:
                self.delta_y += .5
        # ŚMIERC *_*
        if self.rect.y + self.image.get_height() >= config.win_y:
            self.is_dead = True
            self.rect.x = self.rect.x
            self.rect.y = self.rect.x