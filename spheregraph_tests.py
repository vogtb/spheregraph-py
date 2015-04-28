import spheregraph

def test_face_references(level_count, expected_count):
  index_list = [False] * expected_count
  previous_level = spheregraph.get_icosahedron()
  current_level = []

  for level in range(1, level_count):
    current_level = spheregraph.generate_set(previous_level)
    previous_level = current_level

  for face in current_level:
    index_list[face.a] += 1
    index_list[face.b] += 1
    index_list[face.c] += 1

  for neighbor_count in index_list:
    if neighbor_count != 3:
      print("Test expected each face to be referenced 3 times, got: %d" % neighbor_count)


test_face_references(2, 80) # 20
test_face_references(3, 320)
test_face_references(4, 1280)
test_face_references(5, 5120)