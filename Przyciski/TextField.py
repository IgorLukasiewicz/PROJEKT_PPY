import pygame
from Funkcje.UniwersalneFunkcje import *

class TextField:
    def __init__(self, font_size, rect,func, text_color, scale=1.25,text = None,custom_spritesheet=None):
        pygame.font.init()
        self.font = pygame.font.Font("Assets/Fonts/Daydream.ttf", font_size)
        self.rect = pygame.Rect(rect)
        self.text = ""
        self.active = False
        self.text_color = text_color
        self.scale = scale
        self.func = func
        self.text = text


        texture_path = custom_spritesheet or "Assets/Images/ButtonFinalFinal(ale juz serio)/Button.png"
        texture = pygame.image.load(texture_path).convert_alpha()

        fields = UniwersalneFunkcje.get_sliced_surface_from_spritesheet(texture, 208, 48, self.scale, 2, 1)
        self.image_inactive = fields[0][0]
        self.image_active = fields[0][1]

        self.image_inactive = pygame.transform.scale(self.image_inactive, (self.rect.width, self.rect.height))
        self.image_active = pygame.transform.scale(self.image_active, (self.rect.width, self.rect.height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.func()
            elif len(self.text) < 9:
                self.text += event.unicode
            if len(self.text) == 9:
                pygame.mixer.Sound("Assets/Sounds/SFX/interface-denied-access-betacut-1-00-01.wav").play()
    def draw(self, surface):
        surface.blit(self.image_active if self.active else self.image_inactive, self.rect.topleft)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 30, self.rect.centery))
        surface.blit(text_surface, text_rect)
