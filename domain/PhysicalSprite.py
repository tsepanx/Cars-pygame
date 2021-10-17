import pygame
from utils.vector import Vector
from math import cos, sin, degrees


class PhysicalSprite(pygame.sprite.Sprite):
    __direction = Vector(0.0, 0.0)
    position = Vector(0, 0)
    velocity = Vector(0.0, 0.0)
    acceleration = Vector(0.0, 0.0)
    forces = []

    path_car = []
    path_car_vector = []
    a = 0

    def __init__(self, pos, mass, filename):
        pygame.sprite.Sprite.__init__(self)
        self.mass = mass * 1.0
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 0, 255))
        # self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.image.set_colorkey((255, 255, 255))

    def add_force(self, force):
        self.forces.append(force)

    def clear_forces(self):
        self.forces = []

    def update(self):
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        self.velocity.add(self.acceleration)
        self.acceleration.clear()
        for force in self.forces:
            self.acceleration.add(force / self.mass)

    def get_direction(self):
        return self.__direction.get_direction()

    def set_direction(self, vector):
        self.__direction = vector.get_direction()

    def rotate(self, angle):
        self.__direction.normalize()
        x = self.__direction.x
        y = self.__direction.y
        res_x = x * cos(angle) - y * sin(angle)
        res_y = x * sin(angle) + y * cos(angle)
        self.__direction.x = res_x
        self.__direction.y = res_y
        self.image = pygame.transform.rotate(self.image, degrees(angle))
