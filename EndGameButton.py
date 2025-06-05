from Button import Button
import pygame

class EndGameButton(Button):

    def __init__(self, text, font_size, rect, bg_color, when_clicked_color, text_color, func, scale=1.25, nieKlikniety=None, klikniety=None):
        super().__init__(text, font_size, rect, bg_color, when_clicked_color, text_color, func, scale, nieKlikniety, klikniety)

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