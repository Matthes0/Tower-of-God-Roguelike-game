def generate_terrain(y, x):
    map_list = [[0] * x for i in range(0, y)]
    for i in range(0, y):
        for j in range(0, x):
            if i == 0 or i == y - 1 or j == 0 or j == x - 1:
                map_list[i][j] = Terrain(i, j, "Indestructible Wall", "#", False)
            else:
                map_list[i][j] = Terrain(i, j, "Floor", ".", True)
    return map_list


class Terrain:
    def __init__(self, x, y, name, char, passable, actor=None, items=list[0]):
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.passable = passable
        self.actor = actor
        self.items = items
