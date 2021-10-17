# -*- coding: utf-8 -*-

from domain.PhysicalSprite import PhysicalSprite
from utils.vector import Vector
from domain.constans import *
from domain.track import Track

# def draw_vector(screen, color, start_pos, vector):
#     pygame.draw.line(screen, color, start_pos, (start_pos[0] + vector.x, start_pos[1] + vector.y), 5)

pygame.init()
screen = pygame.display.set_mode(size_screen)
clock = pygame.time.Clock()
done = False
# pygame.display.toggle_fullscreen()

sprite = PhysicalSprite((300, 100), MASS, 'data/bull2.png')
sprite2 = PhysicalSprite((200, 100), MASS, 'data/bull2.png')
track = Track((0, 0), 'data/track2_2.png')

sprite.velocity = Vector(0.0, 0.0)
sprite.set_direction(Vector(10.0, 0.0))

sprite2.velocity = Vector(0.0, 0.0)
sprite2.set_direction(Vector(10.0, 0.0))

k_up = False
k_down = False
k_left = False
k_right = False

# video = pygame.movie.Movie('data/video.mpg')
# video.set_display(screen)
# video.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                k_down = True
            if event.key == pygame.K_UP:
                k_up = True
            if event.key == pygame.K_LEFT:
                k_left = True
            if event.key == pygame.K_RIGHT:
                k_right = True
            # if event.key == pygame.K_LALT:
            #     pygame.display.toggle_fullscreen()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                k_down = False
            if event.key == pygame.K_UP:
                k_up = False
            if event.key == pygame.K_LEFT:
                k_left = False
            if event.key == pygame.K_RIGHT:
                k_right = False

    if k_up:
        sprite.add_force(sprite.get_direction() * ENGINE_FORCE)
    if k_down:
        sprite.add_force(sprite.get_direction() * -ENGINE_FORCE)
    if k_left:
        sprite.rotate(-HANDLEABILITY)
        #sprite.image = pygame.transform.rotate(sprite.image, 0.05)
    if k_right:
        sprite.rotate(HANDLEABILITY)

    velocity_dir_proj = sprite.get_direction() * Vector.scalar(sprite.velocity, sprite.get_direction())
    velocity_dir_ort = sprite.velocity - velocity_dir_proj
    sprite.add_force(velocity_dir_proj * (-1 * AIR_RESISTANCE))
    sprite.add_force(velocity_dir_ort * (-1 * GROUND_RESISTANCE))

    velocity_dir_proj_2 = sprite2.get_direction() * Vector.scalar(sprite2.velocity, sprite2.get_direction())
    velocity_dir_ort_2 = sprite2.velocity - velocity_dir_proj_2
    sprite2.add_force(velocity_dir_proj_2 * (-1 * AIR_RESISTANCE))
    sprite2.add_force(velocity_dir_ort_2 * (-1 * GROUND_RESISTANCE))

    if pygame.sprite.collide_mask(track, sprite):
        GROUND_RESISTANCE = ASPHALT_RESISTANCE
    else:
        GROUND_RESISTANCE = GRASS_RESISTANCE

    if sprite.a % 3 == 0:
        sprite.path_car.append(sprite.rect.center)
        sprite.path_car_vector.append((sprite.rect.center[0] + sprite.get_direction().x * 35,
                                       sprite.rect.center[1] + sprite.get_direction().y * 35))
    if len(sprite.path_car) >= 50:
        sprite.path_car.pop(0)
        sprite.path_car_vector.pop(0)
    sprite.a += 1

    if sprite.rect.centery <= 20:
        # sprite.velocity = Vector(0.0, 0.0)
        # sprite.rect.y +=1
        sprite.rect.centery = 20
    if sprite.rect.centerx <= 20:
        sprite.rect.centerx = 20

    if sprite.rect.centerx >= size_screen[0] - 20:
        sprite.rect.centerx = size_screen[0] - 20
    if sprite.rect.centery >= size_screen[1] - 20:
        sprite.rect.centery = size_screen[1] - 20

    sprite.update()
    #sprite2.update()

    screen.fill((0, 160, 0))

    screen.blit(track.image, track.rect)

    for i in range(1, len(sprite.path_car)):
        pygame.draw.line(screen, (0, 0, 255), sprite.path_car[i], sprite.path_car[i - 1], 6)
    for i in range(1, len(sprite.path_car_vector)):
        pygame.draw.line(screen, (255, 0, 0), sprite.path_car_vector[i], sprite.path_car_vector[i - 1], 6)

    sprite.clear_forces()
    sprite2.clear_forces()

    screen.blit(sprite.image, sprite.rect)
    draw_vector_beautiful(screen, (255, 0, 255), sprite2.get_direction() * 40, sprite2)
    screen.blit(sprite2.image, sprite2.rect)
    draw_vector_beautiful(screen, (255, 0, 255), sprite.get_direction() * 40, sprite)

    pygame.display.flip()
    clock.tick(40)

pygame.quit()
