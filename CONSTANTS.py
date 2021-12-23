import pygame


FPS = 50
WIDTH, HEIGHT = 500, 500
MAP = []
BOX = '#'

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

tile_width = tile_height = 50