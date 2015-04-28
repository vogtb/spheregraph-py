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
  Face(a=7, b=0, c=2),
  Face(a=9, b=3, c=1),
  Face(a=11, b=2, c=4),
  Face(a=0, b=13, c=3),
  Face(a=14, b=6, c=0),
  Face(a=15, b=5, c=7),
  Face(a=1, b=8, c=6),
  Face(a=16, b=7, c=9),
  Face(a=2, b=10, c=8),
  Face(a=17, b=9, c=11),
  Face(a=3, b=12, c=10),
  Face(a=13, b=11, c=18),
  Face(a=12, b=4, c=14),
  Face(a=5, b=19, c=13),
  Face(a=6, b=16, c=19),
  Face(a=8, b=15, c=17),
  Face(a=10, b=18, c=16),
  Face(a=19, b=17, c=12),
  Face(a=18, b=14, c=15)
]

def generate_set(parent_face_set):
  full_list_of_faces = []
  count = 0

  def connect_by_rule(face_one_index, face_two_index, rule):
    if rule == "A":
      parent_face_set[face_one_index].children[1].a = parent_face_set[face_two_index].children[1].index
      parent_face_set[face_two_index].children[1].a = parent_face_set[face_one_index].children[1].index
      parent_face_set[face_one_index].children[3].a = parent_face_set[face_two_index].children[3].index
      parent_face_set[face_two_index].children[3].a = parent_face_set[face_one_index].children[3].index
    elif rule == "B":
      parent_face_set[face_one_index].children[2].b = parent_face_set[face_two_index].children[2].index
      parent_face_set[face_two_index].children[2].b = parent_face_set[face_one_index].children[2].index
      parent_face_set[face_one_index].children[3].b = parent_face_set[face_two_index].children[3].index
      parent_face_set[face_two_index].children[3].b = parent_face_set[face_one_index].children[3].index
    elif rule == "C":
      parent_face_set[face_one_index].children[2].c = parent_face_set[face_two_index].children[2].index
      parent_face_set[face_two_index].children[2].c = parent_face_set[face_one_index].children[2].index
      parent_face_set[face_one_index].children[1].c = parent_face_set[face_two_index].children[1].index
      parent_face_set[face_two_index].children[1].c = parent_face_set[face_one_index].children[1].index

  for i in range(0, len(parent_face_set)):
    parent_face_set[i].children = subdivide_face(i, count)
    count += 4

    # If neighbor A is done, connect it, etc.
    if parent_face_set[parent_face_set[i].a].done:
      connect_by_rule(i, parent_face_set[i].a, "A")
    if parent_face_set[parent_face_set[i].b].done:
      connect_by_rule(i, parent_face_set[i].b, "B")
    if parent_face_set[parent_face_set[i].c].done:
      connect_by_rule(i, parent_face_set[i].c, "C")
    parent_face_set[i].done = True

  for i in range(0, len(parent_face_set)):
    full_list_of_faces.extend(parent_face_set[i].children)

  return full_list_of_faces


def get_icosahedron():
  return icosahedron


# Will return 4 Faces that makeup a given face
def subdivide_face(face_index, count):
  return [
    Face(parentIndex=face_index, index=count, a=count+2, b=count+1, c=count+3),
    Face(parentIndex=face_index, index=count+1, a=0, b=count, c=0),
    Face(parentIndex=face_index, index=count+2, a=count, b=0, c=0),
    Face(parentIndex=face_index, index=count+3, a=0, b=0, c=count)
  ]

