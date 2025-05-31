import pygame

class Button:
    def __init__(self, text, font_size, rect, bg_color, when_clicked_color, text_color, func):
        self.text = text
        self.font = pygame.font.Font("Assets/Fonts/Daydream.ttf", font_size)
        self.rect = pygame.Rect(rect)  # rect to krotka (x, y, szerokość, wysokość)
        self.bg_color = bg_color
        self.when_clicked_color = when_clicked_color
        self.text_color = text_color
        self.click_sound =  pygame.mixer.Sound('Assets/Sounds/SFX/8-bit-denied-alert-swoop-1-00-00 (online-audio-converter.com).wav')
        self.click_sound.set_volume(0.25)
        self.was_clicked = False
        self.func = func

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos() # pozycja myszki
        color = self.when_clicked_color if self.rect.collidepoint(mouse_pos) else self.bg_color #sprawdza czy myszka jest nad przyciskiem, jezeli tak to zmienia kolor na when_clicked_color, collidepoint pozwala sprawdzić czy jakieś współrzędne zawierają się w prostokącie (obiekcie klasy Rect)
        pygame.draw.rect(surface, color, self.rect)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self): # bedzie sluzyc do tego zeby przypisywac akcje / metody
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]


    def handle_click(self):
        if self.is_clicked():
            if not self.was_clicked:
                self.click_sound.play()
                self.was_clicked = True

                pygame.time.wait(250)
                self.func()
        else:
            self.was_clicked = False

