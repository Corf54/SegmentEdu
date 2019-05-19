import pygame, config
pygame.init()
class Menu(object):
    def __init__(self, win):

        #obraz
        win.blit(config.Menu_i, (0,0))

        #przycisk start
        win.blit(config.opcja, (437,370))
        menu_start = config.menu_font.render("START", True, config.K_czionkaMenu)
        win.blit(menu_start, (468,375))

        #przycisk wczytaj
        win.blit(config.opcja, (437, 420))
        menu_wczytaj = config.menu_font.render("WCZYTAJ", True, config.K_czionkaMenu)
        win.blit(menu_wczytaj, (455, 425))

        #przycisk ustawienia
        win.blit(config.opcja, (437, 470))
        menu_ustawienia = config.menu_font.render("USTAWIENIA", True, config.K_czionkaMenu)
        win.blit(menu_ustawienia, (443, 475))

        #przycisk wyjdz
        win.blit(config.opcja, (437, 520))
        menu_wyjdz = config.menu_font.render("WYJDZ", True, config.K_czionkaMenu)
        win.blit(menu_wyjdz, (465,525))

    def o_start(self):
        return 1
    def o_wczytaj(self):
        print("WCZYTAJ")
    def o_ustawienia(self):
        print("USTAWIENIA")
    def o_wyjdz(self):
        print("zapis")
