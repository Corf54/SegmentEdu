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

# ------LIST OF CONTENTS / SPIS TRESCI -----------
#	lines 26-201 - Classes other than Game
#	lines 203+ - classes_dict and Game class
#
# Atrybuty obiektow sa zapisane w pliku z konfiguracja!

#Importujemy potrzebne biblioteki
#	obce
import pygame

#	wlasne
from se_config import *

#-----Klasa, od ktorej dziedzicza wszystkie inne (zarowno atrybuty, jak i konstruktor)	
class Parent(pygame.sprite.Sprite,object):
	
	# ---- Atrybuty obiektow -----
	#	Parent
	### ATTRIBUTES OF ANYTHING APPEARING ON THE SCREEN		####
	### Atrybuty wszystkiego, co jest widoczne na ekranie	###
	name = ""
	is_sprite = True #Czy klasa ma dziedziczyc z klasy Sprite

	#	Koordynaty	
	x = 0
	y = 0

	#	Wymiary	
	x_delta = 0
	y_delta = 0

	#	Wektor przesuniecia / Predkosc ; Przesunięcie/Krok dla funkcji range	itp	; Przesuniecie pomiedzy obiektami i iterator
	vector = 3
	step = [20, 5]
	step_macro = [0, -50]
	step_macro_i = 1
	
	#	To, co przechowuje obiekt ; Grafika obiektu ; Uzyty styl
	stored = None
	graphic = "Resources/bg.bmp"
	style = 0
	
	#	Na ktorym ekranie rysowac, grafika do narysowania 
	screen = 0
	make = None
	
###INICJALIZACJA - Przydzielanie wartosci przekazanych atrybotow
###(Konstruktor)
	def __init__(self,line):		# Przekazane atrybuty = linia w pliku z poziomem
		self.make = pygame.image.load(self.graphic)#.convert()		# Domyslny make
		if type(line) is list: 
			line_iterate = iter(line)
			next(line_iterate)			# Pomin pierwszy element (nazwe klasy)
			
			for item in line_iterate:			# Przypisujemy atrybuty z pliku z poziomem do obiektu
				item = item.split(":")				# Nazwa atrybutu : atrybut (zrob liste)
				if len(item[1]) > 1: item[1] = item[1].split(",")			# Podziel atrybuty, jezeli sa lista
				print(item)
				setattr(self,item[0],item[1])	# Przypisz

#-----Klasa okienka-------				
class Screen(Parent,object):

#	Pobieramy rozmiary z pliku z konfiguracja
	x_delta = screen_x
	y_delta = screen_y
	size = [x_delta,y_delta]
	size_dynamic = True
	style = 0

#	Ekran nie jest sprit-em
	is_sprite = False
		
	def update(self):
		if self.size_dynamic == True:		# Jezeli rozmiar ma byc dynamiczny:
			image = background_list[self.style]
			foo, bar, foo, bar = pygame.image.load(image).get_rect()
			self.make = pygame.display.set_mode([foo,bar])	# Dopasuj rozmiar do tla
			
	def __init__(self,line):
		super().__init__(line)
		self.make = pygame.display.set_mode(self.size)		# Uzyj rozmiarow z pliku z konfiguracja
		self.update()
		
#Klasa obrazka
class Image(Parent,object):
	
	def __init__(self,line):
		super().__init__(line) 

#Klasa tla
class Background(Image,object):
	
	def __init__(self,line):
		super().__init__(line) 

#Klasa gracza
class Player(Parent,object):
	
	x_delta = 25
	y_delta = 50													
	collision_lines=[screen_y//2	- y_delta + 100]		# Lines the object collides with - ground
	throwJob = False			#EasterEgg						# Used to quit a loop related to collision lines in update method
	
	
	def __init__(self,line):
		super().__init__(line)

		self.make = pygame.Surface([self.x_delta, self.y_delta])
		self.make.fill((0, int(self.style), 0))

		self.x_vector = 0
		self.y_vector = 0

		self.delta_jump = 10
		self.is_grounded = True

	def prawo(self):
		self.x_vector = self.vector

	def lewo(self):
		self.x_vector = -self.vector

	def stop(self):
		self.x_vector = 0

	def skok(self):
		if self.is_grounded == True:
			self.y_vector = -10
		print (self.y + self.y_delta)

	def update(self):
		
		# SPRAWDZA ORAZ MODYFIKUJE CO KLATKĘ STAN GRACZA
		# AKTUALIZUJE POZYCJE WERTKALNĄ I HORYZONTALNĄ:
		self.x += self.x_vector
		self.y += self.y_vector
		
		# SPRAWDZA CZY POSTAC JEST UZIEMIONA (kolizje tu jeszcze dodam):
		for item in self.collision_lines:
			if self.throwJob == True:
				break
			if self.y + self.y_delta >= item:
				self.is_grounded = True
				self.throwJob = True
			else:
				self.is_grounded = False

		# GRAWITACJA (lub jak kto woli różnica gęstości xd)
			if self.y_vector == 0:
				self.y_vector = 1
			else:
				self.y_vector += .5
			if self.y >= item - self.y_delta and self.y_vector >= 0:
				self.y_vector = 0
		self.throwJob = False

#Klasa przycisku
class Button(Parent,object):

	x_delta = 50
	y_delta = 50
	
	def make_distance(self):
		for value in self.x:
			value += step_macro[0]*step_macro_i
		for value in self.y:
			value += step_macro[0]*step_macro_i
		step_macro_i += 1
		
	def make_elements(self):
		self.make[0] = pygame.image.load(self.make[0])
		self.make[1] = pygame.font.Font(*font).render(self.make[1],True,color_menu)
	
	def __init__(self,line):
		super().__init__(line)
		if self.make is list:			#Zakladamy, ze przekazano tylko ponad jeden make!
			list(self.x)
			list(self.y)
			list(self.screen)
			make_distance()
			for i in range(len(self.make)):
				self.x.append(self.x + self.step[0])
				self.y.append(self.y + self.step[1])
				self.screen.append(self.screen)
				print (self.screen)
			make_elements()
		
	def push():
		return stored
		
#Klasa menu glownego
class Menu(Parent,object):

	def __init__(self,line):
		super().__init__(line)

	def start(self,mode):
		mode = 1		# Przechodzi do trybu gry
		
	def load(self):
		mode = 2		# Przechodzi do trybu wczytywania
		
	def settings(self):
		mode = 3		# Przechodzi do ustawien
		
	def quit(self,run):
		print("Zapisuje* (nie zaimplementowane)")
		run = False
		
		
class Platform(pygame.sprite.Sprite):		#MERGE
    def __init__(self):
        super().__init__()

        self.image = platforma
        self.rect = self.image.get_rect()
    def lvl1(self):
        pozycje_plik = open("Levels/LVL_1/platforms.map").read()
        lista = list(pozycje_plik.split())
        lista = list(map(int,lista))
        pozycje = []
        for i in range(0,len(lista),2):
            podlista = []
            podlista.append(lista[i])
            podlista.append(lista[i+1])
            pozycje.append(podlista)
        return pozycje
        
class Level(object):			#MERGE
	def __init__(self,player):
		self.lista_platform = pygame.sprite.Group()
		self.player = player
		self.p_x = 0
	def update(self):
		self.lista_platform.update()
	def display(self, win):
		win.fill(K_niebo)
		self.lista_platform.draw(win)
	def przesuniecie_x(self, roznica_graniczna):
		self.p_x += roznica_graniczna
		for platform in self.lista_platform:
			platform.rect.x += roznica_graniczna
class First(Level):		#MERGE
	def __init__(self, player):
		super().__init__(player)
		pos = Platform()
		pozycje = pos.lvl1()
		for i in pozycje:
			plat = Platform()
			plat.rect.x = i[0]
			plat.rect.y = i[1]
			self.lista_platform.add(plat)
	
# Classes in dict and list (for iterating) / Klasy w slowniku i liscie (do iteracji) - sprite-y

classes_dict = {'Image':Image,'Player':Player,'Button':Button}	# Pozostale klasy: Screen, Menu, Game


class Game(object):		#KLASA SAMEJ GRY
	
	clock			= pygame.time.Clock()			# Obiekt zmienajacy klatke na ekranie
	run			= True								# Gra trwa, dopoty ta zmienna zawiera True
	object_dict	= {}									# Slownik ze wszystkimi obiektami (poza gra i ekranami)
	screen_list	= []									# Lista wszystkich ekranow
	menu_list	= []									# Lista wszystkich menu
	fps			= fps									# Klatki na sekunde z pliku z konfiguracja
	mode			= 0									# Wybrany tryb gry
	
# 	Function that initializes all objects in a level / Funkcja ktora inicjalizuje wszystkie obiekty w poziomie
	def init_objects(self,level,object_dict):
	#	Zmienne pomocnicze
		level = open(level,'r')
		
	#	Konstrukcja ekranow, menu i sprite-ow na podstawie danych z pliku
		for line in level:
				if line[debug_default] is '#': continue
				line = line.strip().replace(" ","").split(';')

				if type(line) is list:
					class_now = line[debug_default]
				else:
					class_now = line

				if class_now == "Screen":
					object_now = Screen(line)
					self.screen_list.append(object_now)
				elif class_now == "Menu":
					object_now = Menu(line)
					self.menu_list.append(object_now)
				else:		# Konstruujemy sprite-y
					object_now = classes_dict[class_now](line)	# Konstruujemy obiekt z przekazanymi parametrami
					pygame.sprite.Sprite.__init__(object_now)		# Dziedzicz z klasy Sprite
					self.object_dict[class_now].add(object_now)
		
	def __init__(self):
		
		pygame.init()								# Start pygame

		pygame.display.set_caption(title)	# Tytul okna
		
		#Obiekty beda przechowywane w slowniku: (wypelniamy slownik pustymi grupami)
		for key in classes_dict:
			self.object_dict[key] = pygame.sprite.Group()
		
		self.init_objects(level_path,object_dict)		# Skontruuj obiekty z danego poziomu i zapisz je

###### MAIN PROGRAM LOOP / GLOWNA PETLA PROGRAMU #######

	# PRZETWARZANIE INPUTU
	def first__events(self,mode,object_dict,run):
			i = -1														# iterator
			mouse_x, mouse_y = pygame.mouse.get_pos()			# Pobierz pozycje myszy
			
			for player in object_dict['Player']:		# Wyciągamy poszczegolnego gracza z grupy
				i+=1
				for event in pygame.event.get():					# Wyjscie z gry
					if event.type == pygame.QUIT:
						self.run = False
						break

#						"""""""""	Tryby
#						0 = MENU
#						1 = GRA
#						2 = WCZYTAJ
#						3 = USTAWIENIA
#						"""""""""
						
					if self.mode == 0:										# Tryb menu
						for menu in self.menu_list:
							if event.type == pygame.MOUSEBUTTONUP:
								for button in self.button_list:			# Przycisk zwraca, jezeli klikniemy w jego obrebie
									if button.x < mouse_x < button.x + button.x_delta and button.y < mouse_y < button.y + button.y_delta:
										button.push()
								
					if self.mode == 1:									# Tryb platformowy
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								self.mode = 0
							if event.key == pygame.K_d:
								player.prawo()
							if event.key == pygame.K_a:
								player.lewo()
							if event.key == pygame.K_SPACE:
								player.skok()
								
						if event.type == pygame.KEYUP:
							if event.key == pygame.K_d:
								player.stop()
							if event.key == pygame.K_a:
								player.stop()	
								

	# LOGIKA GRY
	def second__logic(self,object_dict):		
		
		#for player in object_dict['Player']:		# Wyciągamy poszczegolnego gracza z grupy
		if True is False:
		
			if (player.x + player.x_delta) >= 650:
				roznica = (player.x + player.x_delta) - 650
				player.x = 650 - player.x_delta
#				self.aktualny_poziom.przesuniecie_x(-roznica)
							
			if player.x	<= 350:
				roznica = 350 - player.x
				player.x = 350
#				self.aktualny_poziom.przesuniecie_x(roznica)

	# RYSOWANIE NA EKRANIE
	def third__output(self,object_dict):
		for key in object_dict: # Dla kazdego klucza/rodziny:
			
# -------- Rysowanie obiektow ---------
			for item in object_dict[key]: 							# Dla poszczegolnego obiektu:
				if type(item.make) is list:									# Jezeli jest wiele elementow do zblitowania
					for i in range(len(item.make)):
						screen = self.screen_list[item.screen[i]].make		# Wybieramy Surface ekranu, na ktory blitujemy
						screen.blit(item.make[i],(item.x[i],item.y[i]))				# Zblituj obecny przedmiot
				else:															# Jezeli jest jeden element do zblitowania
					screen = self.screen_list[item.screen].make		# ibidem
					screen.blit(item.make,(item.x,item.y))				# ibidem


















