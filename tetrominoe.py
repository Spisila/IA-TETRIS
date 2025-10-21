import pygame, enum

import piece


'''
  O = 0
  I = 1
  S = 2
  Z = 3
  L = 4
  J = 5
  T = 6
'''

class Tetrominoe :

  pieces = []

  type = 0

  def __init__(self, _pivot_coord : tuple, _type : int) :

    if _type == 0 :

      pivot_piece = piece.Piece(_pivot_coord)
      self.pieces.append(pivot_piece)

      p2_coord = (_pivot_coord[0]-1, _pivot_coord[1])
      p2 = piece.Piece(p2_coord)
      self.pieces.append(p2)

      p3_coord = (_pivot_coord[0], _pivot_coord[1] + 1)
      p3 = piece.Piece(p3_coord)
      self.pieces.append(p3)

      p4_coord = (_pivot_coord[0] - 1, _pivot_coord[1] + 1)
      p4 = piece.Piece(p4_coord)
      self.pieces.append(p4)