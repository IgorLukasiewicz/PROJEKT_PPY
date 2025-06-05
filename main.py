import pygame
import math
from sys import exit
from Button import Button
from UniwersalneFunkcje import *

fps = 60

pygame.init()
scroll = 0
BASE_WIDTH, BASE_HEIGHT = 1280, 720
width, height = 1280, 720
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Echo Pets')

gameState = "menu"

clock = pygame.time.Clock()

pygame.mixer.music.load('Assets/Sounds/Music/cyborg-ninja-kevin-macleod-main-version-7993-03-00 (1) (online-audio-converter.com).wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)

button_list = []

background = None
background_width = 0

def get_window_scale(new_screen_width, new_screen_height):
    scale_x = new_screen_width/BASE_WIDTH
    scale_y = new_screen_height/BASE_HEIGHT
    new_scale = min(scale_x, scale_y)
    return new_scale

def shouldButtonMakeASound():
    for button in button_list:
        button.handle_click()

def closeGame():
    pygame.quit()
    exit()

def changeGamestateToMenu():
    global gameState
    gameState = "menu"
    pygame.mixer.music.load('Assets/Sounds/Music/cyborg-ninja-kevin-macleod-main-version-7993-03-00 (1) (online-audio-converter.com).wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    setup_menu_buttons()

def setup_menu_buttons(window_scale):
    global button_list
    button_list.clear()



    nowa_gra_button = Button(
        text="Nowa Gra",
        font_size=20,
        rect=(width // 2 -  width / 10, height // 2.5 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=afterNewGame,
        scale=window_scale
    )

    wczytaj_gre_button = Button(
        text="Wczytaj Gre",
        font_size=20,
        rect=(width // 2 - width / 10, height //2 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None,
        scale = window_scale
    )

    wyjdz_z_gry_button = Button(
        text="Wyjdz",
        font_size=20,
        rect=(width // 2 - width / 10, height // 1.5 - height / 12, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=closeGame,
        scale=window_scale
    )

    button_list.extend([nowa_gra_button, wczytaj_gre_button, wyjdz_z_gry_button])

def setup_new_game_buttons(window_scale):
    global button_list, wrocDoMenuButton
    button_list.clear()

    wybor1Button = Button(
        text="Wybierz",
        font_size=20,
        rect=(width * 1 / 8.5 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None,
        scale=window_scale
    )

    wybor2Button = Button(
        text="Wybierz",
        font_size=20,
        rect=(width * 1 / 2.67 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None,
        scale=window_scale
    )

    wybor3Button = Button(
        text="Wybierz",
        font_size=20,
        rect=(width * 1 / 1.6 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None,
        scale=window_scale
    )

    wybor4Button = Button(
        text="Wybierz",
        font_size=20,
        rect=(width * 1 / 1.13 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=None,
        scale=window_scale
    )

    wrocDoMenuButton = Button(
        text="",
        font_size=0,
        rect=(width * 1 / 8.5 - (width / 5) / 2, height / 10 - 35, width / 23, height / 12),
        bg_color=(70, 70, 70),
        when_clicked_color=(150, 150, 150),
        text_color=(255, 255, 255),
        func=changeGamestateToMenu,
        nieKlikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/NieKlikniety.png',
        klikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/Klikniety.png'
    )

    button_list.extend([wybor1Button, wybor2Button, wybor3Button, wybor4Button, wrocDoMenuButton])

def afterNewGame():
    global gameState, background, background_width, width, height
    gameState = "nowa gra"
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Assets/Sounds/Music/itty-bitty-8-bit-kevin-macleod-main-version-7983-03-13.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)

    background = pygame.image.load('Assets/Images/Backgrounds/tloWyboru.png').convert()
    background = pygame.transform.scale(background, (width, height))
    background_width = background.get_width()

    setup_new_game_buttons(1)

def draw_main_menu(window):
    global scroll

    bakcground = pygame.image.load('Assets/Images/Backgrounds/juz seruo final.png').convert()
    bakcground = pygame.transform.scale(bakcground, (width, height))
    bakcground_width = bakcground.get_width()

    tiles = math.ceil(width / bakcground_width) + 2

    scroll = (scroll - 2.5) % bakcground_width

    for x in range(-1, tiles - 1):
        window.blit(bakcground, (x * bakcground_width - scroll, 0))


    for button in button_list:
        button.draw(window)


setup_menu_buttons(window_scale=1)

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            scale = get_window_scale(width, height)

            if gameState == "menu":
                setup_menu_buttons(scale)

            elif gameState == "nowa gra":

                background = pygame.image.load('Assets/Images/Backgrounds/tloWyboru.png').convert()
                background = pygame.transform.scale(background, (width, height))

                setup_new_game_buttons(scale)

    if gameState == "menu":
        draw_main_menu(window)

    elif gameState == "nowa gra":
        window.blit(background, (0, 0))
        for button in button_list:
            button.draw(window)

    shouldButtonMakeASound()

    pygame.display.update()
