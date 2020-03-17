import pygame, random, math
from pygame import mixer
from player import player

if __name__ == "__main__":

  # Initialize the pygame.
  pygame.init()

  # Title and icon.
  pygame.display.set_caption("Space invaders")
  icon = pygame.image.load("src/ufo.png")

  pygame.display.set_icon(icon)
  # Create the screen.
  screen = pygame.display.set_mode((800, 600))

  # Background image.
  bg = pygame.image.load("src/background.jpg")

  # Background music and sound effects.
  mixer.music.load("src/bgm2.mp3")
  mixer.music.set_volume(0.05)
  mixer.music.play(-1)

  explosion_sound = mixer.Sound("src/explosion.wav")
  explosion_sound.set_volume(0.1)

  bullet_sound = mixer.Sound("src/laser.wav")
  bullet_sound.set_volume(0.08)

  # Player.
  player_img = pygame.image.load("src/ship.png")
  player1 = player(speed = 5, img = player_img)

  # Bullet.
  bullet_img = pygame.image.load("src/bullet.png")
  bullet_x = 0
  bullet_y = 0
  bullet_speed = 8
  bullet_ready = True

  # Enemies.

  enemy_img = []
  enemy_x = []
  enemy_y = []
  enemy_speed = []
  enemy_change = []
  num_of_enemies = 6

  for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("src/enemy.png"))
    enemy_x.append(random.randrange(10, 728))
    enemy_y.append(random.randrange(10, 200))
    enemy_speed.append(3)
    enemy_change.append(enemy_speed[i])


  # Score.
  score_value = 0
  font = pygame.font.Font("src/Freehand.ttf", 32)
  text_x = 10
  text_y = 10

  # Game over.
  game_over_font = pygame.font.Font("src/Freehand.ttf", 64)

  # Limit line.
  limit_line_font = pygame.font.Font("src/Freehand.ttf", 40)

  # Enemy drawing.
  def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

  # Bullet drawing.
  def shoot(x, y):
    global bullet_ready
    bullet_ready = False 
    screen.blit(bullet_img, (x + 20, y - 10))

  # Check if it's a collision.
  def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance <= 55

  # Show score.
  def show_score(x, y):
    score = font.render("Puntos: {}".format(score_value), True, (245, 245, 245))
    screen.blit(score, (x, y))

  # Show score.
  def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (245, 245, 245))
    screen.blit(game_over, (200, 250))

  # Show limit.
  def show_limit(x, y):
    limit_line = limit_line_font.render("----------------------------------------------------------------------------------------------", True, (245, 185, 165))
    screen.blit(limit_line, (x, y))

  # Game loop.
  running = True

  while running:
    
    keys = pygame.key.get_pressed()

    # Load background
    screen.blit(bg, (-2500, -100))

    # Check if exit button has been pressed.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    if keys[pygame.K_LEFT]:
      player1.move_left()

    if keys[pygame.K_RIGHT]:
      player1.move_right()

    

    # Draw enemy.

    for i in range(num_of_enemies):
      enemy_x[i] += enemy_change[i]

      if enemy_x[i] >= 728:
        enemy_change[i] = -enemy_speed[i]
        enemy_y[i] += 15
        if enemy_speed[i] < 5: enemy_speed[i] += 0.5
      elif enemy_x[i] <= 10:
        enemy_change[i] = enemy_speed[i]
        enemy_y[i] += 15
        if enemy_speed[i] < 5: enemy_speed[i] += 0.5

      enemy(enemy_x[i], enemy_y[i], i)

      # Collision detection.
      if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
        bullet_y = player1.get_y()
        bullet_ready = True
        enemy_x[i] = random.randrange(10, 728)
        enemy_y[i] = random.randrange(10, 200)
        enemy_speed[i] = 3
        enemy_change[i] = enemy_speed[i]
        explosion_sound.play()
        score_value += 1

      if enemy_y[i] > 390:
        for j in range(num_of_enemies):
          enemy_y[j] = 2000
        
        game_over_text()
        break


    # Draw player.
    player1.draw(screen)

    # Draw bullet.
    if bullet_ready and keys[pygame.K_SPACE]:
      bullet_sound.play()
      bullet_x = player1.get_x()
      bullet_y = player1.get_y()
      shoot(bullet_x, bullet_y)
      bullet_ready = False  
      

    if bullet_y <= 0:
      bullet_y = player1.get_y()
      bullet_ready = True
    elif bullet_ready == False:
      shoot(bullet_x, bullet_y)
      bullet_y -= bullet_speed
      

    # Show score on the screen.
    show_score(text_x, text_y)

    # Show limit line on the screen.
    show_limit(0, 420)

    # Update screen.
    pygame.display.update()
