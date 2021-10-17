# coding=utf-8
import pygame

AIR_RESISTANCE = 2  # сопротивление воздуха

GROUND_RESISTANCE = 6  # сопротивление поверхности
ASPHALT_RESISTANCE = 8  # сопротивление асфальта
GRASS_RESISTANCE = 1.5  # сопротивление травы

ENGINE_FORCE = 30  # тяга мотора
MASS = 50  # масса машины
HANDLEABILITY = 0.05  # угол на который мы поворачиваем машину при повороте

BLACK = (0, 0, 0)

size_screen = (1366, 768)


def draw_vector_beautiful(screen, color, vector, sprite):
    pygame.draw.line(screen, color, sprite.rect.center,
                     (sprite.rect.center[0] + vector.x, sprite.rect.center[1] + vector.y), 3)

    pygame.draw.line(screen, color, (sprite.rect[0], sprite.rect[1] + sprite.rect.height),
                     (sprite.rect.center[0] + vector.x, sprite.rect.center[1] + vector.y), 3)

    pygame.draw.line(screen, color, (sprite.rect[0] + sprite.rect.width, sprite.rect[1]),
                     (sprite.rect.center[0] + vector.x, sprite.rect.center[1] + vector.y), 3)

    pygame.draw.line(screen, color, (sprite.rect[0], sprite.rect[1]),
                     (sprite.rect.center[0] + vector.x, sprite.rect.center[1] + vector.y), 3)

    pygame.draw.line(screen, color, (sprite.rect[0] + sprite.rect.width, sprite.rect[1] + sprite.rect.height),
                     (sprite.rect.center[0] + vector.x, sprite.rect.center[1] + vector.y), 3)
