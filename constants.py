def points(s):
    with open(f"test{s}.txt", "r") as file:
        temp = file.readlines()

    for i in range(len(temp)):
        temp[i] = tuple(map(int, temp[i].split(',')[:-1])) if s == 2 else tuple(map(float, temp[i].split(', '))) if s == 0 else tuple(map(int, temp[i].split(', ')))
    tuple(temp)
    return temp


colors = (
    (1, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 1, 0),
    (1, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 1, 0),    
)


chair_verticies_vector3 = points(0)

chair_edges_vector2 = points(1)

# chair_faces_vector4 = points(2)
