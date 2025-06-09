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


    def draw(self, surface: pygame.Surface,scale):
        surface.blit(self.background_surface, (0,0, self.background_surface.get_width()*scale, self.background_surface.get_height()*scale))
        surface.blit(self.pet_surface, self.pet_rect)



class FallingBock:

    def __init__(self, starting_position_x, starting_position_y, scale = 1):
        self.position = (starting_position_x, starting_position_y)

        self.block_texture = pygame.image.load('Assets/Images/PointsBar/JoyBar/JoyIcon.png').convert_alpha()
        self.original_width = self.block_texture.get_width()
        self.original_height = self.block_texture.get_height()
        self.block_surface = UniwersalneFunkcje.get_single_surface_from_spritesheet(self.block_texture, self.block_texture.get_width(), self.block_texture.get_height(), scale)
        self.scale = scale
        self.falling_speed = 3

    def draw(self, surface: pygame.Surface, scale):

        if self.scale != scale:
            new_block_size = (int(self.original_width*scale), int(self.original_height*scale))
            self.block_surface = pygame.transform.scale(self.block_texture, new_block_size)
            self.scale = scale

        # blok nie porusza się i oczekuje na jego usunięcie w jednymi miejscu poza ekranem
        #if self.position[1] <= surface.get_height(): #Jendak useless
        self.position = (self.position[0], self.position[1] + self.falling_speed * self.scale)


        rect = self.block_surface.get_rect(topleft=self.position)
        surface.blit(self.block_surface, rect)


