import pygame

pygame.init()

start = False
screen = pygame.display.set_mode([500,700])
pygame.display.set_caption("Bloom")
#bg = pygame.image.load("bg.png")
#bg = pygame.transform.scale(bg, (500,700))
#screen.blit(bg, (0,0))
pygame.display.flip()

running = True

while running:
  if pygame.key.get_pressed()[pygame.K_SPACE]:
    start = True

  if start == True:
    
    pass

  else:
    start = False
    pass

for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()
