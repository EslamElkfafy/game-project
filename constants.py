def points(s):
    with open(f"test{s}.txt", "r") as file:
        temp = file.readlines()

    for i in range(len(temp)):
        temp[i] = tuple(map(int, temp[i].split(',')[:-1])) if s == 2 else tuple(map(float, temp[i].split(', '))) if s == 0 else tuple(map(int, temp[i].split(', ')))
    tuple(temp)
    return temp


cube_verticies_vector3 = (
    (1.0000, 1.0000, 1.0000),
    (1.0000, 1.0000, -1.0000),
    (1.0000, -1.0000, 1.0000),
    (1.0000, -1.0000, -1.0000),
    (-1.0000, 1.0000, 1.0000),
    (-1.0000, 1.0000, -1.0000),
    (-1.0000, -1.0000, 1.0000),
    (-1.0000, -1.0000, -1.0000),
    )
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
cube_edges_vector2 = (
    (5, 7),
     (1, 5),
     (0, 1),
     (7, 6),
     (2, 3),
     (4, 5),
     (2, 6),
     (0, 2),
     (7, 3),
     (6, 4),
     (4, 0),
     (3, 1),
    )

cube_faces_vector4 = (
    (0, 4, 6, 2),
    (3, 2, 6, 7),
    (7, 6, 4, 5),
    (5, 1, 3, 7),
    (1, 0, 2, 3),
    (5, 4, 0, 1)
    )
chair_verticies_vector3 = points(0)

chair_edges_vector2 = points(1)

chair_faces_vector4 = points(2)
