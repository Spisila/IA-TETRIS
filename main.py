import pygame, sys, random
from pygame.locals import *
from typing import Tuple

import grid, grid_cell, piece, tetrominoe


pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

GRID_START_X = 600
GRID_START_Y = 25

GRID_SIZE_X = 10
GRID_SIZE_Y = 23

CELL_SIZE = 30

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = 60
frames_per_sec = pygame.time.Clock()

gravity_ticks = 50

active_tetrominoe = tetrominoe.Tetrominoe((5,5), 0)

current_grid = grid.Grid((GRID_START_X, GRID_SIZE_Y), (GRID_SIZE_X, GRID_SIZE_Y), CELL_SIZE)



def ready() -> None :

  current_grid.create_playing_grid()

  for i in range(len(active_tetrominoe.pieces)) :

    current_grid.pieces.append(active_tetrominoe.pieces[i])







def update() -> None :

  gravity_ticks_counter = 0

  while True :
    
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit

    display.fill((20,20,80))

    current_grid.draw_cells(display)
    current_grid.draw_pieces(display)

    # ------------------------------- #

    gravity_ticks_counter += 1

    if gravity_ticks_counter >= gravity_ticks :
      
      for piece in active_tetrominoe.pieces :
        piece.coords = (piece.coords[0], piece.coords[1] + 1)
      
      gravity_ticks_counter = 0

    pygame.display.update()
    frames_per_sec.tick(fps)
  


ready()
update()