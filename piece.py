import pygame

class Piece :

  position = ()
  coords = ()
  size = 0.0

  def __init__(self, _coords : tuple, pos : tuple, _size : float):
    self.coords = _coords
    self.position = pos
    self.size = _size

  def draw(self, screen) :

    pygame.draw.rect(screen, (152,50,50), (self.position[0], self.position[1], self.size, self.size))
    