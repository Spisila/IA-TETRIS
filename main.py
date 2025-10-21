import pygame, sys, typing, random
from pygame.locals import *
from typing import Tuple

import grid_cell, piece

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

GRID_START_X = 600
GRID_START_Y = 150

GRID_SIZE_X = 10
GRID_SIZE_Y = 20

CELL_SIZE = 30

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = 60
frames_per_sec = pygame.time.Clock()

cells = []
pieces = []

coords_positions_dict = {}




def ready() -> None :

  for x in range(GRID_SIZE_X) :

    for y in range(GRID_SIZE_Y) : 
      
      cell_pos_x = (GRID_START_X + ( CELL_SIZE + 2) * x)
      cell_pos_y = (GRID_START_Y + ( CELL_SIZE + 2) * y)

      coords_positions_dict[(x,y)] = (cell_pos_x, cell_pos_y)
      cells.append(grid_cell.Grid_Cell( cell_pos_x, cell_pos_y, CELL_SIZE, x, y))
  
  ran_c: grid_cell = random.choice(cells)
  pos = (ran_c.position_x, ran_c.position_y)

  p = piece.Piece((ran_c.coord_x, ran_c.coord_y), pos, CELL_SIZE)


  pieces.append(p)




def update() -> None :

  while True :

    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit

    display.fill((20,20,80))

    for i in range(len(cells)) :

      cells[i].draw(display)

    for i in range(len(pieces)) :

      pieces[i].draw(display)

    pygame.display.update()
    frames_per_sec.tick(fps)
  

def coordinates_to_position(coord_x : int, coord_y : int) -> Tuple[float, float] :

  return coords_positions_dict.get((coord_x, coord_y))

ready()

update()