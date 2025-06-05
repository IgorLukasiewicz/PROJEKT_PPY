import pygame
from UniwersalneFunkcje import *

class Button:

    def __init__(self, text, font_size, rect, bg_color, when_clicked_color, text_color, func, scale=1.25, nieKlikniety=None, klikniety=None):

        # 1280 -> 1920
        # 720 -> 1080
        #
        # zmienna = obecna szerokość / nowa szerokość



        self.text = text
        self.font = pygame.font.Font("Assets/Fonts/Daydream.ttf", font_size)
        self.rect = pygame.Rect(rect)
        self.bg_color = bg_color
        self.when_clicked_color = when_clicked_color
        self.text_color = text_color
        self.click_sound = pygame.mixer.Sound('Assets/Sounds/SFX/8-bit-denied-alert-swoop-1-00-00 (online-audio-converter.com).wav')
        self.click_sound.set_volume(0.25)
        self.was_clicked = False
        self.func = func

        btn_texture_spritesheet = pygame.image.load("Assets/Images/ButtonFinalFinal(ale juz serio)/Button.png")
        buttons = UniwersalneFunkcje.get_sliced_surface_from_spritesheet(btn_texture_spritesheet, 208, 48,
                                                                         scale*1.25, 2, 1)

        # Ładowanie tekstur
        self.image_normal = buttons[0][0] #nonoe
        self.image_hover = buttons[0][1]

        if nieKlikniety:
            self.image_normal = pygame.image.load(nieKlikniety).convert_alpha()
            self.image_normal = pygame.transform.scale(self.image_normal, (self.rect.width, self.rect.height))

        if klikniety:
            self.image_hover = pygame.image.load(klikniety).convert_alpha()
            self.image_hover = pygame.transform.scale(self.image_hover, (self.rect.width, self.rect.height))

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)

        # Jeśli podano tekstury, rysuj odpowiednią
        if self.image_normal and self.image_hover:
            surface.blit(self.image_hover if is_hovered else self.image_normal, self.rect.topleft)


        else:
            color = self.when_clicked_color if is_hovered else self.bg_color
            pygame.draw.rect(surface, color, self.rect)

        # Rysowanie tekstu
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

    def handle_click(self):
        if self.is_clicked():
            if not self.was_clicked:
                self.click_sound.play()
                self.was_clicked = True
                pygame.time.wait(250)
                if self.func:
                    self.func()
        else:
            self.was_clicked = False
