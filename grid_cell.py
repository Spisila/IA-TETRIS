import pygame

class Grid_Cell() :

  position_x = 0.0
  position_y = 0.0

  coord_x = 0
  coord_y = 0

  size = 0.0

  col = ()

  def __init__(self, pos_x : float, pos_y : float, _size : float, x_coord : int, y_coord : int, _color) -> None:
    
    self.position_x = pos_x
    self.position_y = pos_y
    self.size = _size
    self.coord_x = x_coord
    self.coord_y = y_coord
    self.col = _color
  
    