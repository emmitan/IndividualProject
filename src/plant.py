import pygame

pygame.init()

class Plant:
  def __init__(self, x, y, species, grow):
    self.x, self.y, self.species = x, y, species
    self.grow = grow
