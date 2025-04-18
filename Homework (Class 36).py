import pygame
import random

s_width, s_height = 500, 400
speed = 5
font_size = 72

pygame.init()

font = pygame.font.SysFont('Times New Roman', font_size)

color_cycle = [pygame.Color('green'), pygame.Color('blue'), pygame.Color('yellow'), pygame.Color('purple')]
current_color_index = 0

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('white'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.color = color

    def change_color(self, new_color):
        self.color = new_color
        self.image.fill(pygame.Color('white'))
        pygame.draw.rect(self.image, new_color, pygame.Rect(0, 0, self.rect.width, self.rect.height))

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, s_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, s_height - self.rect.height), 0)

screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Sprite Collision')
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(color_cycle[current_color_index], 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, s_width - sprite1.rect.width), random.randint(0, s_height - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, s_width - sprite2.rect.width), random.randint(0, s_height - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT]) - (keys[pygame.K_LEFT]) * speed
    y_change = (keys[pygame.K_DOWN]) - (keys[pygame.K_UP]) * speed
    sprite1.move(x_change, y_change)

    if sprite1.rect.colliderect(sprite2.rect):
        current_color_index = (current_color_index + 1) % len(color_cycle)
        sprite1.change_color(color_cycle[current_color_index])
        sprite2.rect.x, sprite2.rect.y = random.randint(0, s_width - sprite2.rect.width), random.randint(0, s_height - sprite2.rect.height)

    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()