# A python module to create an icosahedron and recusively subdivide the faces to generate a graph of a sphere.

class Face:
  parentIndex = 0
  index = 0
  a = 0
  b = 0
  c = 0
  done = False
  children = []

  def __init__(self, done=False, parentIndex=0, index=0, a=0, b=0, c=0, children=[]):
    self.parentIndex = parentIndex
    self.index = index
    self.done = done
    self.a = a
    self.b = b
    self.c = c

count = 0
icosahedron = [
  Face(a=4, b=1, c=5),
  Face(7, 0, 2),
  Face(9, 3, 1),
  Face(11, 2, 4),
  Face(0, 13, 3),
  Face(14, 6, 0),
  Face(15, 5, 7),
  Face(1, 8, 6),
  Face(16, 7, 9),
  Face(2, 10, 8),
  Face(17, 9, 11),
  Face(3, 12, 10),
  Face(13, 11, 18),
  Face(12, 4, 14),
  Face(5, 19, 13),
  Face(6, 16, 19),
  Face(8, 15, 17),
  Face(10, 18, 16),
  Face(19, 17, 12),
  Face(18, 14, 15)
]

def generate_set(parent_face_set):
  full_list_of_faces = []
  count = 0

  for i in len(parent_face_set):
    parent_face_set[i].children = subdivide_face(parent_face_set[i])
    count += 4

    # If neighbor A is done, connect it, etc.
    if parent_face_set[parent_face_set[i].a].done:
      connect_by_rule(parent_face_set[i], parent_face_set[parent_face_set[i]].a, "A")

    if parent_face_set[parent_face_set[i].b].done:
      connect_by_rule(parent_face_set[i], parent_face_set[parent_face_set[i]].b, "B")

    if parent_face_set[parent_face_set[i].c].done:
      connect_by_rule(parent_face_set[i], parent_face_set[parent_face_set[i]].c, "C")

    parent_face_set[i].done = True


  for i in len(parent_face_set):
    for x in len(parent_face_set[i].children):
      full_list_of_faces.append(parent_face_set[i].children[x])

  return full_list_of_faces


def icosahedron():
  return icosahedron


# Will return 4 Faces that makeup a given face
def subdivide_face(face):
  parentIndex = face.index
  return [
    Face(parentIndex, count, count + 2, count + 1, count + 3, False),
    Face(parentIndex, count + 1, 0, count, 0, False),
    Face(parentIndex, count + 2, count, 0, 0, False),
    Face(parentIndex, count + 3, 0, 0, count, False)
  ]

def connect_by_rule(faceOne, faceTwo, rule):
  if rule == "A":
    # 1a1
    faceOne.children[1].a = faceTwo.children[1].index
    faceTwo.children[1].a = faceOne.children[1].index
    # 3a3
    faceOne.children[3].a = faceTwo.children[3].index
    faceTwo.children[3].a = faceOne.children[3].index
  elif rule == "B":
    # 2b2
    faceOne.children[2].b = faceTwo.children[2].index
    faceTwo.children[2].b = faceOne.children[2].index
    # 3b3
    faceOne.children[3].b = faceTwo.children[3].index
    faceTwo.children[3].b = faceOne.children[3].index
  elif rule == "C":
    # 2c2
    faceOne.children[2].c = faceTwo.children[2].index
    faceTwo.children[2].c = faceOne.children[2].index
    # 1c1
    faceOne.children[1].c = faceTwo.children[1].index
    faceTwo.children[1].c = faceOne.children[1].index
