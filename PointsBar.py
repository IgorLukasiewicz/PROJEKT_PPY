from Funkcje.UniwersalneFunkcje import UniwersalneFunkcje
import pygame
import math



class PointsBar:

    green_bar_texture = None
    red_bar_texture = None

    def __init__(self, name, points, bar_icon_path, rect, scale = 1):

        if not PointsBar.green_bar_texture:
            PointsBar.green_bar_texture = pygame.image.load('Assets/Images/PointsBar/GreenBar.png').convert_alpha()
        if not PointsBar.red_bar_texture:
            PointsBar.red_bar_texture = pygame.image.load('Assets/Images/PointsBar/RedBar.png').convert_alpha()

        self.name = name
        self.points = points
        self.rect = rect
        self.scale = scale

        bar_icon_texture = pygame.image.load(bar_icon_path).convert_alpha()
        self.bar_icon = UniwersalneFunkcje.get_single_surface_from_spritesheet(bar_icon_texture, bar_icon_texture.get_width(), bar_icon_texture.get_height(), scale)
        self.red_bar_surface = UniwersalneFunkcje.get_single_surface_from_spritesheet(PointsBar.red_bar_texture, PointsBar.red_bar_texture.get_width(), PointsBar.red_bar_texture.get_height(), scale)
        self.green_bar_surface = UniwersalneFunkcje.get_sliced_surface_from_spritesheet(PointsBar.green_bar_texture, PointsBar.green_bar_texture.get_width()/4, PointsBar.green_bar_texture.get_height(), scale, 4, 1)


    def draw(self, surface):
        x, y, w, h = self.rect

        surface.blit(self.bar_icon, self.rect)

        x +=self.bar_icon.get_width()
        y += 4*self.scale
        surface.blit(self.red_bar_surface, (x, y, w, h))


        number_of_green_bars = math.ceil(self.points/5)
        y+=self.scale

        if number_of_green_bars == 1:
            x += self.scale
            surface.blit(self.green_bar_surface[0][0], (x, y, w, h))
        elif number_of_green_bars > 1:
            for i in range(number_of_green_bars):
                if i == 0:
                    x += self.scale
                    green_bar_rect = (x, y, w, h)
                    surface.blit(self.green_bar_surface[0][1], (x, y, w, h))
                elif i == number_of_green_bars-1 :
                    x += self.green_bar_surface[0][0].get_width()-self.scale
                    green_bar_rect = (x, y, w, h)
                    surface.blit(self.green_bar_surface[0][3], (x, y, w, h))
                else:
                    x += self.green_bar_surface[0][0].get_width() - self.scale
                    green_bar_rect = (x, y, w, h)
                    surface.blit(self.green_bar_surface[0][2], (x, y, w, h))