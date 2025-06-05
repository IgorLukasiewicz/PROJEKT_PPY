import pygame

class UniwersalneFunkcje:

    @staticmethod
    def get_single_surface_from_spritesheet(sheet, sprite_width, sprite_height, scale = 1, position_x = 0, position_y = 0):
        image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0,0), (position_x, position_y, sprite_width, sprite_height))
        if scale != 1:
            image = pygame.transform.scale(image, (int(sprite_width * scale), int(sprite_height * scale)))
        return image

    @staticmethod
    def get_sliced_surface_from_spritesheet(sheet, sprite_width, sprite_height, scale = 1, columns = 1, rows = 1):
        sprites = []
        for row in range(rows):
            row_sprites = []
            for column in range(columns):
                x = column * sprite_width
                y = row * sprite_height
                row_sprites.append(UniwersalneFunkcje.get_single_surface_from_spritesheet(sheet, sprite_width, sprite_height, scale, x, y))
            sprites.append(row_sprites)
        return sprites
