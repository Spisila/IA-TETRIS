import pygame, typing 
from typing import Tuple

import grid_cell

class Grid :

  grid_position = ()
  grid_size = ()

  cell_size = 0.0

  cells = []

  pieces = []

  coords_positions_dict = {}

  def __init__(self, _pos : tuple, _size : tuple, _cell_size : float):
    
    self.grid_position = _pos
    self.grid_size = _size
    self.cell_size = _cell_size

  def coordinates_to_position(self, coord_x : int, coord_y : int) -> Tuple[float, float] :

    return self.coords_positions_dict.get((coord_x, coord_y))


  def create_playing_grid(self) :

    for x in range(self.grid_size[0]) :

      for y in range(self.grid_size[1]) : 
        
        cell_pos_x = (self.grid_position[0] + (self.cell_size + 2) * x)
        cell_pos_y = (self.grid_position[1] + (self.cell_size + 2) * y)

        self.coords_positions_dict[(x,y)] = (cell_pos_x, cell_pos_y)

        col = (150,150,150)

        if y < 3 :

          col = (75,75,75)

        self.cells.append(grid_cell.Grid_Cell(cell_pos_x, cell_pos_y, self.cell_size, x, y, col))

  def draw_cells(self, screen) :

    for cell in self.cells :

      c_pos = (self.coordinates_to_position(cell.coord_x, cell.coord_y))

      pygame.draw.rect(screen, (50,50,50), (c_pos[0], c_pos[1], self.cell_size, self.cell_size), 5)


  def draw_pieces(self, screen) :
    
    for piece in self.pieces :

      p_pos = (self.coordinates_to_position(piece.coords[0], piece.coords[1]))

      pygame.draw.rect(screen, (250,50,50), (p_pos[0], p_pos[1], self.cell_size, self.cell_size))