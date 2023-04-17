import pygame
from tqdm import trange, tqdm

# CONSTANTES
MAX_ITERATION = 500
XMIN, XMAX, YMIN, YMAX = -2, +0.5, -1.25, +1.25
LARGEUR, HAUTEUR = 500, 500 # taille de la fenêtre en pixels

pygame.init()
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Fractale de Mandelbrot")


for y in range(HAUTEUR):
  for x in range(LARGEUR):
    cx = (x * (XMAX - XMIN) / LARGEUR + XMIN)
    cy = (y * (YMIN - YMAX) / HAUTEUR + YMAX)
    xn = 0
    yn = 0
    n = 0
    while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION:
      tmp_x = xn
      tmp_y = yn
      xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
      yn = 2 * tmp_x * tmp_y + cy
      n = n + 1
    if n == MAX_ITERATION:
      screen.set_at((x, y), (0, 0, 0)) 
    else:
      screen.set_at((x, y), (255, 255, 255))
pygame.display.flip()
loop = True
while loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      loop = False
      
pygame.quit()
