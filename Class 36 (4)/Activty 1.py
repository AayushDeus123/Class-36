import pygame
import random

#Constants for easier adjustments
s_width , s_height = 500 , 400
speed = 5
font_size = 72

#Initialise Pygame
pygame.init()

#Load and transform the background image
bg_image = pygame.transform.scale(pygame.image.load("img.jpg"),(s_width,s_height))

#Load font once at the beginning
font = pygame.font.SysFont('Times New Roman' , font_size)

class Sprite(pygame.sprite.Sprite):
  def __init__(self , color , width , height):
    super().__init__()
    self.image = pygame.Surface([width,height])
    #Background colour of sprite
    self.image.fill(pygame.Color('dodgerblue'))
    pygame.draw.rect(self.image , color , pygame.Rect(0 , 0 , width , height))
    self.rect = self.image.get_rect()
    
  def move(self , x_change , y_change):
    self.rect.x = max(min(self.rect.x + x_change , s_width - self.rect.width) , 0)
    self.rect.y = max(min(self.rect.y + y_change , s_width - self.rect.height) , 0)
    
#Setup
screen = pygame.display.set_mode((s_width , s_height))
pygame.display.set_caption('Sprite Collision')
all_sprites = pygame.sprite.Group()

#Creating the 2 sprites
sprite1 = Sprite(pygame.Color('black') , 20,30)
sprite1.rect.x , sprite1.rect.y = random.randint(0 , s_width - sprite1.rect.width) , random.randint(0 , s_height - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red') , 20,30)
sprite2.rect.x , sprite2.rect.y = random.randint(0 , s_width - sprite2.rect.width) , random.randint(0 , s_height - sprite2.rect.height)
all_sprites.add(sprite2)

#Game loop control variables
running , won = True , False
clock = pygame.time.Clock()

#Main game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
      running = False
      
  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT]) - (keys[pygame.K_LEFT]) * speed
    y_change = (keys[pygame.K_DOWN]) - (keys[pygame.K_UP]) * speed
    sprite1.move(x_change , y_change)
      
  if sprite1.rect.colliderect(sprite2.rect):
    all_sprites.remove(sprite2)
    won = True
        
  #Drawing
  screen.blit(bg_image , (0,0))
  all_sprites.draw(screen)
    
  #Display win message
  if won:
    win_text = font.render('You Win!' , True , pygame.Color('black'))
    screen.blit(win_text , (100,200))
  pygame.display.flip()
  clock.tick(90)

pygame.quit()