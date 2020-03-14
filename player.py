class player:
  def __init__(x = 370, y = 480, speed = 0.8, img = ""):
    self.x = x
    self.y = y
    self.speed = speed
    self.img = img

  def draw(screen):
    screen.blit(self.img, self.x, self.y)

  def move_left():
    if self.x > 10:
      x -= self.speed
  
  def move_right():
    if self.x < 728:
      x += self.speed