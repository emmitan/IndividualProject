import pygame

pygame.init()
screen = pygame.display.set_mode([700, 500])

class Plant:
  def __init__(self, x, y):
    self.x, self.y = x, y
    #self.grow = grow
    x = 0
    y = 0
    

  def display(self, x, y):
    self.x = x
    self.y = y
    plant = pygame.image.load("plant.png")
    pygame.transform.scale(plant, (100,100))
    screen.blit(plant, (self.x, self.y))
    pygame.display.flip()
    
  def clicks(self): 
    clicks = 0
    clicks += 1
    print("clicks: ", clicks)
