import pygame

# Initialize the pygame
pygame.init()

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("src/ufo.png")

pygame.display.set_icon(icon)
# Create the screen
screen = pygame.display.set_mode((800, 600))


# Player
player_img = pygame.image.load("src/ship.png")
player_x = 370
player_y = 480
player_speed = 0.8
player_x_change = 0

# Enemy
enemy_img = pygame.image.load("src/ufo.png")
enemy_x = 10
enemy_y = 50
enemy_speed = 0.2
enemy_change = 0

def player(x, y):
  screen.blit(player_img, (x, y))

def enemy(x, y):
  screen.blit(enemy_img, (x, y))


# Game loop
running = True

while running:
  # Change background color - RGB
  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # If keystroke is pressed, check whether it's left or right
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player_x_change = -player_speed

      if event.key == pygame.K_RIGHT:
        player_x_change = player_speed
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player_x_change = 0

  # Draw player
  player_x += player_x_change
  
  if player_x < 10: player_x = 10
  if player_x > 728: player_x = 728

  player(player_x, player_y)

  # Drar enemy

  enemy_x += enemy_change

  if enemy_x >= 758:
    enemy_change = -enemy_speed
    enemy_y += 15
    if enemy_speed < 0.8: enemy_speed += 0.02
  elif enemy_x <= 10:
    enemy_change = enemy_speed
    enemy_y += 15
    if enemy_speed < 0.8: enemy_speed += 0.02

  enemy(enemy_x, enemy_y)

  # Update changes
  pygame.display.update()
