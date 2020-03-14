class player:
  def __init__(self, x = 370, y = 480, speed = 0.8, img = None):
    self.x = x
    self.y = y
    self.speed = speed
    self.img = img

  def draw(self, screen):
    screen.blit(self.img, (self.x, self.y))

  def move_left(self):
    if self.x > 10:
      self.x -= self.speed
  
  def move_right(self):
    if self.x < 728:
      self.x += self.speed

  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y

  def get_speed(self):
    return self.speed