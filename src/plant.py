import pygame

pygame.init()

class Plant:
  def __init__(self, x, y, series, grow):
    self.x, self.y, self.series = x, y, series
    self.grow = grow
