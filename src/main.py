import pygame
#from plant import Plant
#from fairy import Fairy

pygame.init()

start = False
screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption("Bloom")
bg = pygame.image.load("sbgFiller.jpg")
screen.blit(bg, (0, 0))
pygame.display.flip()

running = True

while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    start = True

  if start == True:
    bg = pygame.image.load("lbgFiller.jpg")
    screen.blit(bg, (0, 0))
    pygame.display.flip()

  else:
    bg = pygame.image.load("sbgFiller.jpg")
    screen.blit(bg, (0, 0))
    pygame.display.flip()

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    running = False

pygame.quit()
