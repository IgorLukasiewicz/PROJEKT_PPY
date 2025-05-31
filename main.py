import pygame
import math
from sys import exit
from Button import Button

fps = 60

pygame.init()
scroll = 0
width, height = 1280, 720
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Echo Pets')

clock = pygame.time.Clock()

pygame.mixer.music.load('Assets/Sounds/Music/cyborg-ninja-kevin-macleod-main-version-7993-03-00 (1) (online-audio-converter.com).wav')
pygame.mixer.music.play(-1) # nieskonczona petla bo -1
pygame.mixer.music.set_volume(0.25) #ustawienei glosnosci

button_list = [] # lista przycisków  wszystkich


# SPRAWDZAMY CZY PRZYCISK POWINIEN WYDAC DZWIEK
def shouldButtonMakeASound():
    for button in button_list:
        button.handle_click()




# ZMIENIANIE ROZMAROW GUZIKA W PRZYPADKU RESIZE
def buttonResize():
    for button in button_list:
        button.draw(window)


def closeGame():
    pygame.quit()
    exit()

# MENU STARTOWE
def draw_main_menu(window):
    nowa_gra_button = Button(
        text="Nowa Gra",
        font_size=20,
        rect=(width // 2 -  width / 10, height // 2.5 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None
    )

    wczytaj_gre_button = Button(
        text="Wczytaj Gre",
        font_size=20,
        rect=(width // 2 - width / 10, height //2 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func = None
    )

    wyjdz_z_gry_buttom = Button(
        text="Wyjdz",
        font_size=20,
        rect=(width // 2 - width / 10, height // 1.5 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func = closeGame
    )

    global scroll # global dlatego, że scroll musi byc jako pole globalne ale musimy zmodyfikowac go w metodzie

    bakcground = pygame.image.load('Assets/Images/Backgrounds/juz seruo final.png').convert() # TU ZMIENIASZ TLO
    bakcground = pygame.transform.scale(bakcground, (width, height))
    bakcground_width = bakcground.get_width()

    tiles = math.ceil(width / bakcground_width) + 2 # ceil zaokrągla wynik w górę do najbliższej liczby całkowitej, bo nie możemy narysować 2.56 kafelka — potrzebujemy całych.

    scroll = (scroll - 2.5) % bakcground_width  # przesuwamy i zawijamy scroll

    for x in range(-1, tiles - 1):
        window.blit(bakcground, (x * bakcground_width - scroll, 0))  # przesuwamy tło w lewo


    nowa_gra_button.draw(window)
    wczytaj_gre_button.draw(window)
    wyjdz_z_gry_buttom.draw(window)

    button_list.append(nowa_gra_button)
    button_list.append(wczytaj_gre_button)
    button_list.append(wyjdz_z_gry_buttom)



#MAIN PETLA
while True:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    draw_main_menu(window)
    shouldButtonMakeASound()


    pygame.display.update()

