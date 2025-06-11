import math
import random

from pygame import Surface

from Pets import Pet, Kameleon
from Funkcje.UniwersalneFunkcje import UniwersalneFunkcje
import pygame
from random import randint


class JoyGame:

    def __init__(self, pet, screen_width, screen_height, scale = 1):

        # background
        self.background_original_texture = pygame.image.load('Assets/Images/Backgrounds/joy_game_background.png')
        self.background_surface = pygame.transform.smoothscale(self.background_original_texture, (screen_width, screen_height))
        self.pet_name = pet
        self.screen_base_width = screen_width
        self.screen_base_height = screen_height

        # pet
        self.pet_position_x = int(screen_width/2)
        self.pet_original_texture = pygame.image.load(f"Assets/Images/PetsTxt/BeforeEvolution/{pet}.png")
        self.pet_original_width = 80
        self.pet_original_height = 80
        self.pet_original_speed = 10 #bardzo szybki pet
        self.pet_speed = self.pet_original_speed

        self.pet_surface = pygame.transform.smoothscale(self.pet_original_texture, (self.pet_original_width, self.pet_original_height))

        self.pet_rect = self.pet_surface.get_rect()
        self.pet_rect.midbottom = (self.pet_position_x , screen_height)

        # ogarnianie bloków

        falling_block = FallingBlock(0, screen_height, scale)
        self.falling_blocks = []

        self.number_of_blocks = int(math.floor(screen_width/falling_block.block_texture.get_width()))

        for i in range(self.number_of_blocks):
            if i == 0:
                self.falling_blocks.append(falling_block)
            else:
                new_falling_block = FallingBlock(falling_block.block_texture.get_width()*i, screen_height, scale)
                self.falling_blocks.append(new_falling_block)



    def resize(self, surface: pygame.Surface, scale):
        # background
        self.background_surface = pygame.transform.smoothscale(self.background_original_texture,(surface.get_width(), surface.get_height()))

        # pet
        new_pet_width = int(self.pet_original_width*scale)
        new_pet_height = int(self.pet_original_height*scale)

        self.pet_surface = pygame.transform.smoothscale(self.pet_original_texture, (new_pet_width, new_pet_height))
        self.pet_rect = self.pet_surface.get_rect()
        self.pet_rect.midbottom = (int(self.pet_position_x * surface.get_width() / self.screen_base_width), surface.get_height())

        for falling_block in self.falling_blocks:
            falling_block.resize(scale, surface)

        self.pet_speed = int(self.pet_original_speed*scale)

    def change_pet(self, pet_name):
        if self.pet_name != pet_name:
            self.pet_original_texture = pygame.image.load(f"Assets/Images/PetsTxt/BeforeEvolution/{pet_name}.png").convert_alpha()
            self.pet_name = pet_name

            old_size = self.pet_surface.get_size()
            old_position = self.pet_rect.midbottom

            self.pet_surface = pygame.transform.smoothscale(
                self.pet_original_texture, old_size
            )
            self.pet_rect = self.pet_surface.get_rect()
            self.pet_rect.midbottom = old_position


    def draw(self, surface: pygame.Surface,scale):
        # blity
        surface.blit(self.background_surface, (0,0))
        surface.blit(self.pet_surface, self.pet_rect)

        # bloki
        for fb in self.falling_blocks:
            if fb.set_for_fall:
                fb.draw(surface, scale)



    # Moc przyjaźni, aktywacja!
    # co sekundę losuje blok, który jeśli nie spada i nie jest aktywny to go aktywuje i ustawi na górze
    def activate_falling_blocks(self, frame_counter):
        if frame_counter == 15:
            activate_block_number = random.randint(0, self.number_of_blocks-1)
            if not self.falling_blocks[activate_block_number].set_for_fall:
                self.falling_blocks[activate_block_number].set_for_fall = True
                self.falling_blocks[activate_block_number].hit = False
                self.falling_blocks[activate_block_number].position_y = 0

    def move_pet_left(self, surface: pygame.Surface):
        pet_position_x = self.pet_rect.x-self.pet_speed
        if  pet_position_x>=0:
            self.pet_rect = self.pet_rect.move(-self.pet_speed,0)
        else:
            self.pet_rect.midbottom = (surface.get_width(), surface.get_height())

    def move_pet_right(self, surface: pygame.Surface):
        pet_position_x = self.pet_rect.x + self.pet_speed
        if pet_position_x <= surface.get_width():
            self.pet_rect = self.pet_rect.move(self.pet_speed, 0)
        else:
            self.pet_rect.midbottom = (0, surface.get_height())

    def collision(self):
        for block in self.falling_blocks:
            if self.pet_rect.colliderect(block.block_rect) and not block.hit:
                block.hit = True
                return True
        return False





class FallingBlock:

    def __init__(self, starting_position_x, starting_position_y, scale = 1):

        self.position_x, self.position_y = starting_position_x, starting_position_y
        self.block_texture = pygame.image.load('Assets/Images/PointsBar/JoyBar/JoyIcon.png').convert_alpha()

        self.original_width = self.block_texture.get_width()
        self.original_height = self.block_texture.get_height()

        self.block_surface = pygame.Surface((self.original_width, self.original_height), pygame.SRCALPHA)
        self.block_rect = self.block_surface.get_rect(topleft=(self.position_x, self.position_y))
        self.block_surface.blit(self.block_texture, (0,0))

        self.scale = scale
        self.falling_speed = 5
        self.hit = False
        self.set_for_fall = True


    def resize(self, scale, surface: pygame.Surface, base_surface_width = 1280, base_surface_height = 720):
        self.position_x = self.position_x*surface.get_width()/base_surface_width
        self.position_y = self.position_y*surface.get_height()/base_surface_height

        new_block_width = int(self.original_width*scale)
        new_block_height = int(self.original_height*scale)

        self.block_surface = pygame.transform.smoothscale(self.block_texture, (new_block_width, new_block_width))
        self.block_rect = self.block_surface.get_rect()
        self.block_rect.topleft = (self.position_x, self.position_y)

    def draw(self, surface: pygame.Surface, scale = 1):

        if self.position_y >= surface.get_height():
            self.hit = True
            self.set_for_fall = False

        surface.blit(self.block_surface, self.block_rect)
        self.position_y += self.falling_speed
        self.block_rect.topleft = (self.position_x, self.position_y)



