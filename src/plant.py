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
    pygame.transform.scale(plant, (100, 100))
    screen.blit(plant, (self.x, self.y))
    pygame.display.flip()

  #def clicks(self):
   # clicks = 0
    #if pygame.mouse.get_pressed()[0] == True:
     # if self.x < pygame.mouse.get_pos(
     # )[0] < self.x + 100 and self.y < pygame.mouse.get_pos(
      #)[1] < self.y + 100:
       # clicks += 1
       # return clicks

    #else:
     # clicks = 0
      #return clicks
