import pygame

pygame.init()
surface = pygame.display.get_surface()
col = (255, 255, 255)
center = (surface.get_width() / 2, surface.get_height() / 2)
radius = 5

class Plant:
  def __init__(self, x, y):
    self.x, self.y = x, y
    #self.grow = grow
    x = 0
    y = 0
    

  def display(self):
    pygame.draw.circle(surface, col, center, radius)

  def clicks(self):
    clicks = 0
    clicks += 1
    print("clicks: ", clicks)
