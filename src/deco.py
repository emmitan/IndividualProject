import pygame

pygame.init()

class Deco:
  def __init__(self, x, y, bought, coin):
    self.x, self.y, self.coin = x, y, coin
    self.bought = bought
    bought = False

  def bought(bought):
    #mouse listener
    if pygame.mouse.get_pressed()[0]:
      pass

    #if mouse clicked on img + enough money:
      #bought = True
      #coin -= gnome

    #if mouse click on img + not enough money:
      #bought = False
      #load error msg
    pass
    
  def display(x, y):
    #load products
    #gnome = pygame.image.load("gnome.png")
    #birdbath = pygame.image.load("birdbath.png")
    #bench = pygame.image.load("bench.png")
    #wheelbarrow = pygame.image.load("wheelbarrow.png")

    #price for each product:
    #gnome = 20
    #birdbath = 45
    #bench = 60
    #wheelbarrow = 80
    
    #display products
    #x = 0
    #y = 0
    #hv products set to x + 10, etc.
    #screen.blit(gnome, (x,y))
    #screen.blit(birdbath, (x,y))
    #screen.blit(bench, (x,y))
    #screen.blit(wspin, (x,y))
    #screen.blit(fountain, (x,y))
    #screen.blit(wheelbarrow, (x,y))
    
    pass
