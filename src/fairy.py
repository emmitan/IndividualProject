import pygame

pygame.init()
screen = pygame.display.set_mode([700, 500])


class Fairy:

  def __init__(self, x, y, speed):
    self.x, self.y, self.speed = x, y, speed
    x = 0
    y = 0
  
  def display(self, x, y):
    self.x = x
    self.y = y
    #load imgs
    #jerry = pygame.image.load("jerry.png")
    #jerry = pygame.transform.scale(jerry, (50,50))
    #thimble = pygame.image.load("thimble.png")
    #thimble = pygame.transform.scale(thimble, (50,50))
    #petunia = pygame.image.load("petunia.png")
    #petunia = pygame.transform.scale(petunia, (50,50))
    gnome = pygame.image.load("gnome.png")
    gnome = pygame.transform.scale(gnome, (50, 50))

    #display imgs
    #screen.blit(jerry, (x, y))
    #screen.blit(thimble, (x, y))
    #screen.blit(petunia, (x, y))
    screen.blit(gnome, (x, y))
    pygame.display.flip()

    #jerry: brownie, geraniums
    #thimble: pixie, pansy
    #petunia: gnome, petunia

    #if imgs are with the plant
