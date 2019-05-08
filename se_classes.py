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



#Importujemy potrzebne biblioteki
#	obce
import pygame

#	wlasne
from se_config import *


#class Parent(pygame.sprite.Sprite,object):
#	pass

#-----Klasa, od ktorej dziedzicza wszystkie inne (zarowno atrybuty, jak i konstruktor)	
class Parent(pygame.sprite.Sprite,object):

###ATTRIBUTES OF ANYTHING APPEARING ON THE SCREEN####
###Atrybuty wszystkiego, co jest widoczne na ekranie###
	name = ""
	is_sprite = True #Czy klasa ma dziedziczyc z klasy Sprite

#	Koordynaty	
	x = 0
	y = 0
	coords = [x, y]

#	Wymiary, rozmiar	
	x_d = 0
	y_d = 0
	size = [x_d,y_d]

#	Wektor przesuniecia / Predkosc	
	vector = 3

#	Na ktorym ekranie rysowac, metoda ladujaca, metoda rysujaca (ktora 'wprawia obiekt w ruch')
	screen = 0
	make = None
	draw = None

#	To, co przechowuje obiekt ; Grafika obiektu ; Uzyty styl
	stored = None
	graphic = "Resources/bg.bmp"
	style = 0
	
###INICJALIZACJA - Przydzielanie wartosci przekazanych atrybotow
###(Konstruktor)
	def __init__(self,attr_passed): #Przekazane atrybuty = linia w pliku z poziomem
#		Jezeli obiekt ma byc spritem, dziedziczymy z klasy Sprite
		if self.is_sprite:
			pygame.sprite.Sprite.__init__(self)
#		Przypisujemy atrybuty z pliku z poziomem do obiektu...
		for item in attr_passed:
#			...jezeli sa jakies			
			if True is True:
				try:
					self.item[0] = item[1]
				except Exception:
					pass

#-----Klasa okienka-------				
class Screen(Parent,object):

#	Pobieramy rozmiary z pliku z konfiguracja
	x_d = screen_x
	y_d = screen_y
	size = [x_d,y_d]

#	Ekran nie jest sprit-em
	is_sprite = False

	def __init__(self,attr_passed):
		super().__init__(attr_passed)
		self.make = pygame.display.set_mode(self.size)		# W przeciwnym razie, uzyj rozmiarow z pliku z konfiguracja
		
#	def update(self):
		if dynamic_size == True:		# Jezeli rozmiar ma byc dynamiczny:
			image = background_list[self.style]
			foo, bar, foo, bar = pygame.image.load(image).get_rect()
			self.make = pygame.display.set_mode([foo,bar])	# Dopasuj rozmiar do tla

#Klasa obrazka
class Image(Parent,object):
	
	def __init__(self,attr_passed):
		super().__init__(attr_passed) 
		self.make = pygame.image.load(self.graphic).convert()

#Klasa tla
class Background(Image,object):
	
	def __init__(self,attr_passed):
		super().__init__(attr_passed) 
		self.make = pygame.image.load(self.graphic).convert()

#Klasa gracza
class Player(Parent,object):
	
	x_d = 100
	y_d = 100
	
	def __init__(self,attr_passed):
		super().__init__(attr_passed)

		self.make = pygame.Surface([self.x_d, self.y_d])
		self.make.fill((0, 255, 0))

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
		print (self.y + self.y_d)

	def update(self):
		half_screen = screen_y//2	- self.y_d
		half_screen += 100
		
		# SPRAWDZA ORAZ MODYFIKUJE CO KLATKĘ STAN GRACZA
		# AKTUALIZUJE POZYCJE WERTKALNĄ I HORYZONTALNĄ:
		self.x += self.x_vector
		self.y += self.y_vector

		# SPRAWDZA CZY POSTAC JEST UZIEMIONA (kolizje tu jeszcze dodam):
		if self.y + self.y_d >= half_screen:
			self.is_grounded = True
		else:
			self.is_grounded = False

		# GRAWITACJA (lub jak kto woli różnica gęstości xd)
		if self.y_vector == 0:
			self.y_vector = 1
		else:
			self.y_vector += .5
		if self.y >= half_screen - self.y_d and self.y_vector >= 0:
			self.y_vector = 0

#Klasa przycisku
class Button(Parent,object):

	x_d = 50
	y_d = 50
	
	def __init__(self,attr_passed):
		super().__init__(attr_passed)
		self.make = pygame.image.load(self.graphic).convert()
		
	def push():
		return stored
		
#Klasa menu glownego
class Menu(Parent,object):
	
	buttons = []
	b_coords = [[40,40],[40,60],[40,80],[40,100]]
	b_size = [[]]
	b_stored = ["Gra","Ustawienia","Credits","Wyjdz"]
	
	
	def __init__(self,attr_passed):
		super().__init__(attr_passed)
		self.b_attributes = [0,0,0,self.b_coords,0,0,self.b_size,0,0,0,self.b_stored]
		for i in range(len(self.buttons)):
			buttons.append(Button)
	
# Classes in dict and list (for iterating) / Klasy w slowniku i liscie (do iteracji)

classes_dict = {'Image':Image,'Player':Player}	# Nie zawiera Screen i Game!


class Game(object):		#KLASA SAMEJ GRY
	
	clock = pygame.time.Clock()			# Obiekt zmienajacy klatke na ekranie
	run = True									# Gra trwa, dopoty ta zmienna zawiera True
	object_dict = {}							# Slownik ze wszystkimi obiektami (poza gra i ekranami)
	screen_list = []							# Lista wszystkich ekranow
	fps = fps									# Klatki na sekunde z pliku z konfiguracja
	
# 	Function that initializes all objects in a level / Funkcja ktora inicjalizuje wszystkie obiekty w poziomie
	def init_objects(self,level,object_dict):
	#	Zmienne pomocnicze
		level = open(level,'r')
		
	#	Konstrukcja ekranow i sprite-ow na podstawie danych z pliku
		for line in level:
				if line[0] is '#': continue
#				line.split(",")
				class_now = line.strip()
				if class_now == "Screen":
					object_now = Screen(line)
					self.screen_list.append(object_now)
				else:
					object_now = classes_dict[class_now](line)	#Konstruujemy obiekt z przekazanymi parametrami
					self.object_dict[class_now].add(object_now)
		
	def setup(self):
		
		pygame.init()								# Start pygame

		pygame.display.set_caption(title)	# Tytul okna
		
		#Obiekty beda przechowywane w slowniku:
		for key in classes_dict:
			self.object_dict[key] = pygame.sprite.Group()
		
		self.init_objects(level_path,object_dict)		# Skontruuj obiekty z danego poziomu i zapisz je

###### MAIN PROGRAM LOOP / GLOWNA PETLA PROGRAMU #######

	def first__events(self,tryb,object_dict,run):
			i = -1
			for player in object_dict['Player']:		# Wyciągamy poszczegolnego gracza z grupy
				i+=1
				for event in pygame.event.get():					# Wyjscie z gry
					if event.type == pygame.QUIT:
						self.run = False
						break
						
					if tryb == 0:										# Menu glowne
						mouse_x, mouse_y = pygame.mouse.get_pos()
						mainMenu = menu.Menu(window)
						if event.type == pygame.MOUSEBUTTONUP:
							if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 370 and mouse_y < 411:
								tryb = mainMenu.o_start()
							if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 420 and mouse_y < 457:
								mainMenu.o_wczytaj()
							if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 470 and mouse_y < 511:
								mainMenu.o_ustawienia()
							if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 520 and mouse_y < 557:
								mainMenu.o_wyjdz()
								self.run = False
					if tryb == 1:									# Tryb gry
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								tryb = 0
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
				player.update()




	def second__logic(self):
		pass

	# Funkcja rysująca
	def third__output(self,object_dict):
		for key in object_dict: # Dla kazdego klucza/rodziny:
			
# -------- Rysowanie obiektow ---------
			for item in object_dict[key]: # Dla poszczegolnego obiektu:
				screen_no = item.screen		# Ekran, na ktory obrazek rysujemy
				#Wybierz dany ekran z listy i zblituj na niego obecny obrazek
				self.screen_list[screen_no].make.blit(item.make,(item.x,item.y))

	# Funkcja wylaczajaca gre i silnik
	def quit(self):
		#if self.run is False:
		if True is True:
			pygame.quit()


















