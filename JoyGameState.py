import math

from Pets import Pet, Kameleon
from Funkcje.UniwersalneFunkcje import UniwersalneFunkcje
import pygame



class JoyGame:

    def __init__(self, pet: Pet, screen_width, screen_height, scale = 1):

        self.pet_texture = pygame.image.load(pet.textureBeforeEvolve)
        self.pet_surface = UniwersalneFunkcje.get_single_surface_from_spritesheet(self.pet_texture, self.pet_texture.get_width(), self.pet_texture.get_height(), scale)
        self.original_pet_width = self.pet_texture.get_width()
        self.original_pet_height = self.pet_texture.get_height()
        background_texture = pygame.image.load('Assets/Images/Backgrounds/joy_game_background.png')
        self.background_surface = UniwersalneFunkcje.get_single_surface_from_spritesheet(background_texture,background_texture.get_width(), background_texture.get_height(), scale)
        self.pet_rect = self.pet_surface.get_rect(midbottom=(screen_width/2, screen_height))
        self.falling_blocks = []

        falling_block = FallingBlock(0, 0, scale)
        number_of_blocks = int(math.floor(screen_width/falling_block.block_texture.get_width()))

        for i in range(number_of_blocks):
            if i == 0:
                self.falling_blocks.append(falling_block)
            else:
                new_falling_block = FallingBlock(falling_block.block_texture.get_width()*i, 0, scale)
                self.falling_blocks.append(new_falling_block)



    def draw(self, surface: pygame.Surface,scale):
        surface.blit(self.background_surface, (0,0, self.background_surface.get_width()*scale, self.background_surface.get_height()*scale))
        surface.blit(self.pet_surface, self.pet_rect)
        for fb in self.falling_blocks:
            if fb.set_for_fall:
                fb.draw(surface, scale)



class FallingBlock:

    def __init__(self, starting_position_x, starting_position_y, scale = 1):
        self.position = (starting_position_x, starting_position_y)

        self.block_texture = pygame.image.load('Assets/Images/PointsBar/JoyBar/JoyIcon.png').convert_alpha()
        self.original_width = self.block_texture.get_width()
        self.original_height = self.block_texture.get_height()
        self.block_surface = UniwersalneFunkcje.get_single_surface_from_spritesheet(self.block_texture, self.block_texture.get_width(), self.block_texture.get_height(), scale)
        self.scale = scale
        self.falling_speed = 3
        self.hit_the_bottom = False
        self.set_for_fall = True

    def draw(self, surface: pygame.Surface, scale = 1):
        # pet: Pet):

        if self.scale != scale:
            new_block_size = (int(self.original_width*scale), int(self.original_height*scale))
            self.block_surface = pygame.transform.scale(self.block_texture, new_block_size)
            self.scale = scale

        if self.position[1] <= surface.get_height():
            self.hit_the_bottom = True
            self.set_for_fall = False
            # pet.joy_points += 5

        if self.set_for_fall:
            self.position = (self.position[0], self.position[1] + self.falling_speed * self.scale)


        rect = self.block_surface.get_rect(topleft=self.position)
        surface.blit(self.block_surface, rect)


