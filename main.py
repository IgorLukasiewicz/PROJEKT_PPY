from Przyciski.EndGameButton import EndGameButton
import math
from Przyciski.Button import Button
from Funkcje.UniwersalneFunkcje import  *
from Przyciski.TextField import TextField
from PointsBar import *


from Pets.Pet import Pet
from Pets.Kameleon import Kameleon
from Pets.Papuga import Papuga
from Pets.Pingwin import Pingwin
from Pets.Wieloryb import Wieloryb



fps = 60

pygame.init()
scroll = 0
BASE_WIDTH, BASE_HEIGHT = 1280, 720
width, height = 1280, 720

textField = ""
textFieldText= "" #TUTAJ ZAPISUJE TEKST W NICKU, NIGDZIE INDZIEJ NIE BĘDZIEMY UŻYWAC TEGO WIĘC

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

pet = ""

pet_Type = ""



def get_window_scale(new_screen_width, new_screen_height):
    scale_x = new_screen_width/BASE_WIDTH
    scale_y = new_screen_height/BASE_HEIGHT
    new_scale = min(scale_x, scale_y)
    return new_scale

def shouldButtonMakeASound():
    for button in button_list:
        button.handle_click()

def closeGame(): # ========================================================== NIE WYWAlA BŁĘDU =======================================================================
    pygame.quit()
    exit()

def changeGamestateToMenu(window_scale=1):
    global gameState
    global textFieldText
    gameState = "menu"
    pygame.mixer.music.load('Assets/Sounds/Music/cyborg-ninja-kevin-macleod-main-version-7993-03-00 (1) (online-audio-converter.com).wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    setup_menu_buttons(window_scale)
    textFieldText = ""


def runGame():
    global button_list
    global gameState
    global background

    button_list.clear()

    gameState = "playing"

    background = pygame.image.load(pet.backgroundTexture).convert()
    background = pygame.transform.scale(background, (width, height))

    window.blit(background, (0, 0))

    pet_texture = pygame.image.load(pet.textureBeforeEvolve).convert_alpha()
    pet_texture = pygame.transform.scale(pet_texture, (int(width * 0.2 * 1.5), int(height * 0.3 * 1.5)))

    pet_x = (width - pet_texture.get_width()) // 2
    pet_y = int(height // 2 - pet_texture.get_height() // 2)

    window.blit(pet_texture, (pet_x, pet_y))

    wrocDoMenuButton = Button(
        text="",
        font_size=0,
        rect=(width - width / 23, 5 * width/BASE_WIDTH, width / 23, height / 12),  # prawy górny róg
        text_color=(255, 255, 255),
        func=changeGamestateToMenu,
        nieKlikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/NieKlikniety.png',
        klikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/Klikniety.png'
    )

    nakarmButton = Button(
        text="Nakarm",
        font_size=int(25 * width / BASE_WIDTH),
        rect=(width * 1 / 5 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_kameleona,
        scale=get_window_scale(width, height)
    )

    bawSie = Button(
        text="Baw sie",
        font_size=int(25 * width / BASE_WIDTH),
        rect=(width * 1 / 1.27 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_kameleona,
        scale=get_window_scale(width, height)
    )





    font = pygame.font.Font("Assets/Fonts/Daydream.ttf", int(80 * width / BASE_WIDTH))
    text_surface = font.render(textFieldText, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 12))

    button_list.extend([wrocDoMenuButton, nakarmButton, bawSie])



    pygame.display.update()
    window.blit(text_surface, text_rect)




def setup_menu_buttons(window_scale):
    global button_list
    button_list.clear()



    nowa_gra_button = Button(
        text="Nowa Gra",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width // 2 -  width / 10, height // 2.5 - height / 12, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=afterNewGame,
        scale=window_scale
    )

    wczytaj_gre_button = Button(
        text="Wczytaj Gre",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width // 2 - width / 10, height //2 - height / 12, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=None,
        scale = window_scale
    )

    wyjdz_z_gry_button = EndGameButton(
        text="Wyjdz",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width // 2 - width / 10, height // 1.5 - height / 12, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=closeGame,
        scale=window_scale
    )

    button_list.extend([nowa_gra_button, wczytaj_gre_button, wyjdz_z_gry_button])

def poWyborze(text):
    global gameState
    global textField
    global button_list
    global textFieldText
    global background


    background = pygame.image.load('Assets/Images/Backgrounds/wpisywanieNickuIMozeCosJescze.png').convert()
    background = pygame.transform.scale(background, (width, height))

    button_list.clear()
    gameState = "makePet"
    window.blit(background, (0, 0))


    tf_width = width * 0.4
    tf_height = height * 0.15


    tf_x = (width - tf_width) // 2
    tf_y = (height - tf_height) // 2


    textField = TextField(
        font_size=int(50 * width / BASE_WIDTH),
        rect=(tf_x, tf_y, tf_width, tf_height),
        text_color=pygame.Color("white"),
        custom_spritesheet=None,
        func=runGame,
        text=textFieldText
    )

    wrocDoMenuButton = Button(
        text="",
        font_size=0,
        rect=(width * 1 / 8.5 - (width / 5) / 2, height / 10 - 35, width / 23, height / 12),
        text_color=(255, 255, 255),
        func=changeGamestateToMenu,
        nieKlikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/NieKlikniety.png',
        klikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/Klikniety.png'
    )

    button_list.append(wrocDoMenuButton)


def wybierz_kameleona(zebyDzialal):
    global pet_Type, pet
    pet_Type = "kameleon"
    pet = Kameleon()
    poWyborze("")

def wybierz_pingwina(zebyDzialal):
    global pet_Type, pet
    pet_Type = "pingwin"
    pet = Pingwin()
    poWyborze("")

def wybierz_wieloryba(zebyDzialal):
    global pet_Type, pet
    pet_Type = "wieloryb"
    pet = Wieloryb()
    poWyborze("")

def wybierz_papuge(zebyDzialal):
    global pet_Type, pet
    pet_Type = "papuga"
    pet = Papuga()
    poWyborze("")



def setup_new_game_buttons(window_scale):
    global button_list, wrocDoMenuButton
    button_list.clear()

    wybor1Button = Button(
        text="Wybierz",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width * 1 / 8.5 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_kameleona,
        scale=window_scale
    )

    wybor2Button = Button(
        text="Wybierz",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width * 1 / 2.67 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_pingwina,
        scale=window_scale
    )

    wybor3Button = Button(
        text="Wybierz",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width * 1 / 1.6 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_wieloryba,
        scale=window_scale
    )

    wybor4Button = Button(
        text="Wybierz",
        font_size=int(20 * width / BASE_WIDTH),
        rect=(width * 1 / 1.13 - (width / 5) / 2, height / 1.2 - (height / 12) / 2, width / 5, height / 12),
        text_color=(255, 255, 255),
        func=wybierz_kameleona,
        scale=window_scale
    )

    wrocDoMenuButton = Button(
        text="",
        font_size=0,
        rect=(width * 1 / 8.5 - (width / 5) / 2, height / 10 - 35, width / 23, height / 12),
        text_color=(255, 255, 255),
        func=changeGamestateToMenu,
        nieKlikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/NieKlikniety.png',
        klikniety='Assets/Images/ButtonFinalFinal(ale juz serio)/PrzejdzDoMenuButton/Klikniety.png'
    )

    button_list.extend([wybor1Button, wybor2Button, wybor3Button, wybor4Button, wrocDoMenuButton])



def afterNewGame(window_scale):
    global gameState, background, background_width, width, height
    gameState = "nowa gra"
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Assets/Sounds/Music/itty-bitty-8-bit-kevin-macleod-main-version-7983-03-13.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)

    background = pygame.image.load('Assets/Images/Backgrounds/tloWyboru.png').convert()
    background = pygame.transform.scale(background, (width, height))
    background_width = background.get_width()

    setup_new_game_buttons(window_scale)

def draw_main_menu(window, window_scale):
    global scroll

    bakcground = pygame.image.load('Assets/Images/Backgrounds/juz seruo final.png').convert()
    bakcground = pygame.transform.scale(bakcground, (width, height))
    bakcground_width = bakcground.get_width()

    tiles = math.ceil(width / bakcground_width) + 2

    scroll = (scroll - 2.5) % bakcground_width

    for x in range(-1, tiles - 1):
        window.blit(bakcground, (x * bakcground_width - scroll, 0))

    setup_menu_buttons(window_scale)

    for button in button_list:
        button.draw(window)



setup_menu_buttons(window_scale=1)

frameCounter = 0

while True:
    clock.tick(fps)



    for event in pygame.event.get():
        scale = get_window_scale(width, height)
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

            if gameState == "makePet":
                poWyborze(textFieldText)

            if gameState =="playing":
                runGame()


        if gameState == "makePet" and textField:
                textField.handle_event(event)

    if gameState == "menu":
        draw_main_menu(window, scale)

    elif gameState == "nowa gra":
        window.blit(background, (0, 0))
        for button in button_list:
            button.draw(window)

    elif gameState == "makePet":
        textField.draw(window)
        textFieldText = textField.text
        font = pygame.font.Font("Assets/Fonts/Daydream.ttf", int(50 * width/BASE_WIDTH))
        text_surface = font.render("Podaj nazwe Peta", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, height // 3.2))
        window.blit(text_surface, text_rect)

        for button in button_list:
            button.draw(window)

    else:
        frameCounter += 1

        if frameCounter == 120:
            newPoints = pet.joy_points - 1
            pet.joy_points = newPoints
            frameCounter = 0

        if isinstance(pet, Pet):
            joy = pet.joy_points
        bar_path = 'Assets/Images/PointsBar/SatietyBar/HungerIcon.png'
        bar = PointsBar("test", 75, bar_path, (0, 0, 249, 48), 1 * width / BASE_WIDTH)
        bar.draw(window)

        bar_path = 'Assets/Images/PointsBar/JoyBar/JoyIcon.png'
        bar = PointsBar("test", pet.joy_points, bar_path, (0, 50 * width / BASE_WIDTH, 249, 48), 1 * width / BASE_WIDTH)
        bar.draw(window)

        for button in button_list:
            button.draw(window)

    shouldButtonMakeASound()

    pygame.display.update()