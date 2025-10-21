import pygame

class Piece :

  position = ()
  coords = ()
  size = 0.0

  def __init__(self, _coords : tuple) -> None:
    self.coords = _coords
