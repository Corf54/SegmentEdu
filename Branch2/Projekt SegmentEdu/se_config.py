#   SegmentEdu - educational, general-development tool for beginner programmers and lifelong-learners
#   Copyright (C) 2019 Krzysztof Hoszowski and the SegmentEdu Team
#   Contact: Email - krzysztof.wlodzimierz@protonmail.com
#   SegmentEdu Team - Authors of SegmentEdu: Krzysztof Hoszowski, Jakub Cupiał
#
#   This file is part of SegmentEdu.
#
#   SegmentEdu is free software: you can redistribute it and/or modify
#   it only under the terms of the GNU General Public License version 3 as published by
#   the Free Software Foundation.
#
#   SegmentEdu is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with SegmentEdu.  If not, see <https://www.gnu.org/licenses/>.
#
#
#

# ---- Zmienne nadrzedne ------
# Default Resolution / Domyslna rozdzielczosc
screen_x = 1280
screen_y = 720

#Localization / Lokalizacja
localization = "localization_PL-1.txt"

#Styles / Style - whether or not to import from them / czy importowac z nich, czy tez nie
styles = False

#Tablice do przechowywania parametrow obiektow i samych obiektow
object_parameters = {}
object_dict = {}

#Loop until done / Powtarzaj dopoty gra nie zostanie zamknieta
run = True

#Framerate / Ilosc klatek na sekunde
fps = 30

#Poziom do zaladowania
level_path = "Levels/menu.txt"

# ---- Constants / Stale ------
pi = 3.141592653

#Colors / Kolory
black		= ( 0, 0, 0,)
white		= ( 255, 255, 255)
color_menu		= ( 0, 128, 0)

#Fonty
font = None, 23

#Title / Tytul
title = "SegmentEdu Alpha 0.5"

# ---- Zmienne obiektow ------
default = 0				# Ktory element domyslnie wyciagac z tablicy
debug_default = 0		# ... jak powyzej dla narzedzi niskiego poziomu (nie dla end-user)

	
# Screen
# Whether or not to set window size dynamically / Czy ustawic rozmiar okna dynamiczna
# ( depending on background resolution )			/ (zaleznie od rozmiaru tla)
screen_size_dynamic = True


# ---- Grafiki obiektow -----
# KEY / LEGENDA #
# 1 - Menu
# 2 - Greek, Antique


# Backgrounds / Tla
background_list = [
"Resources/bg.bmp",
"Resources/bg.bmp"
]

#Platformy
platform_list = [
"Resources/bg.bmp"
]



######## MERGE #########
import pygame
pygame.init()

K_czionkaMenu = (0,128,0)
K_czarny = (0,0,0)
K_niebo = (151,196,229)

Menu_i = pygame.image.load("Resources/MainMenu.jpg")
option = pygame.image.load("Resources/Option.png")

platforma = pygame.image.load("Resources/dol.png")

menu_font = pygame.font.Font(None, 23)

win_x = 1000
win_y = 600

p_predkosc = 5







