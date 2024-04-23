import pygame
from plant import Plant
#from fairy import Fairy

pygame.init()

start = False
clicks = 0
screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption("Bloom")
bg = pygame.image.load("sbgFiller.jpg")
bg = pygame.transform.scale(bg, (700, 500))
screen.blit(bg, (0, 0))
p = Plant(0, 0)
pygame.display.flip()

running = True

while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    start = True

  if start == True:
    bg = pygame.image.load("lbgFiller.jpg")
    bg = pygame.transform.scale(bg, (700, 500))
    screen.blit(bg, (0, 0))
    p.display(100, 100)
    pygame.display.flip()

  else:
    start = False
    bg = pygame.image.load("sbgFiller.jpg")
    bg = pygame.transform.scale(bg, (700, 500))
    screen.blit(bg, (0, 0))
    pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      #mouse_pos = pygame.mouse.get_pos()
      #if p.x < mouse_pos[0] < p.x + 100 and p.y < mouse_pos[1] < p.y + 100:
        clicks += 1
        print("clicks: ", clicks)

pygame.quit()
