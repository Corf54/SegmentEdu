import pygame, config, menu, gracz, poziom, zgon
pygame.init()

window = pygame.display.set_mode([config.win_x, config.win_y])
pygame.display.set_caption("EUSEQ: Demo Test")

clock = pygame.time.Clock()

tryb = 0
"""""""""
0 = MENU
1 = USTAWIENIA
2 = GRA
"""""""""

run = True
while run:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if tryb == 0:
        mainMenu = menu.Menu(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 370 and mouse_y < 411:
                    tryb = mainMenu.o_start()
                    all_sprites = pygame.sprite.Group()
                    player = gracz.Player(25, 50)

                    lvl1 = poziom.First
                    list_of_lvls = []
                    list_of_lvls.append(lvl1(player))

                    numer_aktualnego_poziomu = 0
                    aktualny_poziom = list_of_lvls[numer_aktualnego_poziomu]
                    player.poziom = aktualny_poziom

                if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 420 and mouse_y < 457:
                    mainMenu.o_wczytaj()
                if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 470 and mouse_y < 511:
                    mainMenu.o_ustawienia()
                if event.button == 1 and mouse_x > 437 and mouse_x < 548 and mouse_y > 520 and mouse_y < 557:
                    mainMenu.o_wyjdz()
                    run = False
    if tryb == 1:
        all_sprites.add(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                if event.key == pygame.K_d and player.delta_x > 0:
                    player.stop()
                if event.key == pygame.K_a and player.delta_x < 0:
                    player.stop()
            if player.zgon() == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and event.button == 1 and mouse_x >= 444 and mouse_x <= 555 and mouse_y >= 350 and mouse_y <= 387:
                        print("TEST")
                        player.is_dead = False
                        tryb = 0
        if player.rect.right >= 650:
            roznica = player.rect.right - 650
            player.rect.right = 650
            aktualny_poziom.przesuniecie_x(-roznica)
        if player.rect.left  <= 350:
            roznica = 350 - player.rect.left
            player.rect.left = 350
            aktualny_poziom.przesuniecie_x(roznica)
        if player.zgon() == True:
            smierc = zgon.koniec()
            all_sprites.add(smierc)
        aktualny_poziom.display(window)
        all_sprites.draw(window)
        player.update()
    pygame.display.update()
    clock.tick(60)
pygame.quit()