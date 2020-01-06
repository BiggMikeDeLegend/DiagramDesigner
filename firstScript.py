import pygame
import math

pygame.init()

clock = pygame.time.Clock()
Running = True

pygame.display.set_caption("Unnamed Program")

display_width = 700
display_height = 700

display = pygame.display.set_mode((display_width,display_height))

width = 6
last_pos = 0

while Running:
    mouse_position = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(display,(255,255,255),mouse_position, math.floor(width/2))
        if last_pos != 0:
            pygame.draw.line(display,(255,255,255), last_pos, mouse_position, width)
    pygame.display.update()
    last_pos = mouse_position

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            Running = False

    clock.tick(120)

pygame.quit()
quit()