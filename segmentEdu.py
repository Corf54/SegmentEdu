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

# Importujemy potrzebne biblioteki:
# z partii trzecich
import pygame

# wlasne
from se_classes import Game

game = Game()								# Stworzenie instancji gry
game.setup()								# START - przygotowanie do uruchomienia gry

# ----------- Main Program Loop / Glowna Petla Programu ------------
while game.run == True:
	
	game.first__events(1,game.object_dict,game.run)	#Event processing / Czesc 1. - Przetwarzanie wydarzen
	
	game.second__logic()					#Game logic / Czesc 2. - Przetwarzanie logiki gry
	
	game.third__output(game.object_dict)		#Output to player / Czesc 3. - Wysylanie informacji do gracza
	
	
	# UPDATE AND MOVE A FRAME / ZAKTUALIZUJ EKRAN(Y) I ZMIEN KLATKE
	pygame.display.flip()
	game.clock.tick(game.fps)

# ------------------------------------------------------------------

game.quit()		# Wylaczenie gry




















