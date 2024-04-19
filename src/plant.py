import pygame

pygame.init()

class Plant:
  def __init__(self, x, y):
    self.x, self.y = x, y
    #self.grow = grow
    x = 0
    y = 0
    

  def display(self):
    plant = pygame.image.load("plant.png")
    pygame.transform.scale(plant, (50,50))
  def clicks(self):
    clicks = 0
    clicks += 1
    print("clicks: ", clicks)
