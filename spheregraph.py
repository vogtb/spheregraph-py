# A python module to create an icosahedron and recusively subdivide the faces to generate a graph of a sphere.

class Face:
  parentIndex = 0
  index = 0
  a = 0
  b = 0
  c = 0
  done = False
  children = []

  def __init__(self, index, a, b, c):
    self.index = index
    self.a = a
    self.b = b
    self.c = c

icosahedron = [
  Face(0, 4, 1, 5),
  Face(1, 7, 0, 2),
  Face(2, 9, 3, 1),
  Face(3, 11, 2, 4),
  Face(4, 0, 13, 3),
  Face(5, 14, 6, 0),
  Face(6, 15, 5, 7),
  Face(7, 1, 8, 6),
  Face(8, 16, 7, 9),
  Face(9, 2, 10, 8),
  Face(10, 17, 9, 11),
  Face(11, 3, 12, 10),
  Face(12, 13, 11, 18),
  Face(13, 12, 4, 14),
  Face(14, 5, 19, 13),
  Face(15, 6, 16, 19),
  Face(16, 8, 15, 17),
  Face(17, 10, 18, 16),
  Face(18, 19, 17, 12),
  Face(19, 18, 14, 15)
]

