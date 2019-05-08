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

#Default Resolution / Domyslna rozdzielczosc
screen_x = 1280
screen_y = 720

#Localization / Lokalizacja
locale = "localization_PL-1.txt"

#Styles / Style - whether or not to import from them / czy importowac z nich, czy tez nie
styles = False

#Backgrounds / Tla
background_list = [
"Resources/bg.bmp",		#Menu
"Resources/bg.bmp"		#Greek, Antique
]

# Whether or not to set window size dynamically / Czy ustawic rozmiar okna dynamiczna
# ( depending on background resolution )			/ (zaleznie od rozmiary tla)
dynamic_size = True

# --------- Constants / Stale -----------
pi = 3.141592653

#Colors / Kolory
black		= ( 0, 0, 0,)
white		= ( 255, 255, 255)

#Displays / Ekrany
#screen = classes.Screen(['s',])

#Title / Tytul
title = "SegmentEdu Alpha 0.5"

# ------ Variables / Zmienne -------

#Tablice do przechowywania parametrow obiektow i samych obiektow
object_parameters = {}
object_dict = {}

#Loop until done / Powtarzaj dopoty gra nie zostanie zamknieta
run = True

#Framerate / Ilosc klatek na sekunde
fps = 30

#Przykladowy poziom do zaladowania
level_path = "Levels/menu.txt"