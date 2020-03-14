import pygame
import math
from player import player
# Initialize the pygame.
pygame.init()

# Title and icon.
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("src/ufo.png")

pygame.display.set_icon(icon)
# Create the screen.
screen = pygame.display.set_mode((800, 600))

# Background.
bg = pygame.image.load("src/background.jpg")

# Player.
player_img = pygame.image.load("src/ship.png")
player1 = player(speed = 5, img = player_img)

# Bullet.
bullet_img = pygame.image.load("src/bullet.png")
bullet_x = 0
bullet_y = 0
bullet_ready = True

# Enemy.
enemy_img = pygame.image.load("src/enemy.png")
enemy_x = 10
enemy_y = 50
enemy_speed = 3
enemy_change = 0

# Enemy drawing.
def enemy(x, y):
  screen.blit(enemy_img, (x, y))

# Bullet drawing.
def shoot(x, y):
  global bullet_ready
  bullet_ready = False 
  screen.blit(bullet_img, (x + 20, y - 10))

# Check if it's a collision.
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
  distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
  return distance <= 60


# Game loop.
running = True

while running:
  # Change background color - RGB.
  keys = pygame.key.get_pressed()
  screen.blit(bg, (0, 0))

  # Check if exit button has been pressed.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if keys[pygame.K_LEFT]:
    player1.move_left()

  if keys[pygame.K_RIGHT]:
    player1.move_right()

  # Collision detection.
  collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
  if collision:
    bullet_y = player1.get_y()
    bullet_ready = True
    enemy_x = 10
    enemy_y = 10

  # Draw enemy.
  enemy_x += enemy_change

  if enemy_x >= 728:
    enemy_change = -enemy_speed
    enemy_y += 15
    if enemy_speed < 0.8: enemy_speed += 0.05
  elif enemy_x <= 10:
    enemy_change = enemy_speed
    enemy_y += 15
    if enemy_speed < 0.8: enemy_speed += 0.05

  enemy(enemy_x, enemy_y)

  # Draw player.
  player1.draw(screen)

  # Draw bullet.
  if bullet_ready and keys[pygame.K_SPACE]:
    bullet_x = player1.get_x()
    bullet_y = player1.get_y()
    shoot(bullet_x, bullet_y)
    bullet_ready = False  

  if bullet_y <= 0:
    bullet_y = player1.get_y()
    bullet_ready = True
  elif bullet_ready == False:
    shoot(bullet_x, bullet_y)
    bullet_y -= 5
    

  # Update screen.
  pygame.display.update()
