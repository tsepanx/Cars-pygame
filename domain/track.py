import pygame


class Track(pygame.sprite.Sprite):
    def __init__(self, pos, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image.set_colorkey((255, 255, 255))
