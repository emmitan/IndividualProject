import pygame
#from plant import Plant
#from fairy import Fairy

pygame.init()

start = False
screen = pygame.display.set_mode([500, 700])
pygame.display.set_caption("Bloom")
bg = pygame.image.load("sbgFiller.jpg")
bg = pygame.transform.scale(bg, (500, 700))
screen.blit(bg, (0, 0))
pygame.display.flip()

running = True

while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    start = True

  if start == True:
    bg = pygame.image.load("lbgFiller.jpg")
    bg = pygame.transform.scale(bg, (500, 700))
    screen.blit(bg, (0, 0))
    pygame.display.flip()

  else:
    start = False
    bg = pygame.image.load("sbgFiller.jpg")
    bg = pygame.transform.scale(bg, (500, 700))
    screen.blit(bg, (0, 0))
    pygame.display.flip()

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    running = False

pygame.quit()
