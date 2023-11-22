def generate_terrain(y, x):
    map_list = [[0] * x for i in range(0, y)]
    for i in range(0, y):
        for j in range(0, x):
            if i == 0 or i == y - 1 or j == 0 or j == x - 1:
                map_list[i][j] = IndestructibleWall(i, j)
            else:
                map_list[i][j] = Floor(i, j)
    return map_list

def can_place_item(y, x):
    import main, screen
    if x > main.map_width or y > main.map_height:
        screen.update_chat(f"Can't place item at {y},{x} because it is out of bounds")
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can place item at {y},{x}")
        return 1
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can't place item at {y},{x} because there are too many items")
        return 2
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place item at {y},{x} because {main.terrain_map[y][x].name} is a terrain here")
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place item at {y},{x} because there are too many items and {main.terrain_map[y][x].name} is a terrain here")
        return 2
    else:
        screen.update_chat("Something went wrong during can_place_item")
    return 0

def can_place_actor(y, x):
    import main, screen
    if x > main.map_width-1 or y > main.map_height-1:
        screen.update_chat(f"Can't place actor at {y},{x} because it is out of bounds")
    elif main.terrain_map[y][x].actor is None and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can place actor at {y},{x}")
        return 1
    elif main.terrain_map[y][x].actor is not None and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can't place actor at {y},{x} because {main.terrain_map[y][x].actor.char} is here")
        return 2
    elif main.terrain_map[y][x].actor is None and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place actor at {y},{x} because {main.terrain_map[y][x].name} is a terrain here")
    elif main.terrain_map[y][x].actor is not None and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place actor at {y},{x} because {main.terrain_map[y][x].actor.char} is here and {main.terrain_map[y][x].name} is a terrain here")
        return 2
    else:
        screen.update_chat("Something went wrong during can_place_actor")
    return 0

def print_actors_and_items():
    import main, screen
    for i in range(main.map_height):
        for j in range(main.map_width):
            if main.terrain_map[i][j].actor is not None:
                screen.update_chat(f"{main.terrain_map[i][j].actor.name}, y:{i},x:{j}")
            else:
                if hasattr(main.terrain_map[i][j], "items") and len(main.terrain_map[i][j].items) > 0:
                    for item in main.terrain_map[i][j].items:
                        screen.update_chat(f"{item.name}, y:{i},x:{j}")



def place_actor(actor):
    import main, screen
    main.terrain_map[actor.y][actor.x].actor = actor
    screen.update_terrain()


def delete_actor(y, x):
    import main, screen
    main.terrain_map[y][x].actor = None
    screen.update_terrain()


def place_item(item):
    import main, screen
    main.terrain_map[item.y][item.x].items.append(item)
    screen.update_terrain()


def delete_item(y, x):
    import main, screen
    main.terrain_map[y][x].items.pop()
    screen.update_terrain()


class Terrain:
    def __init__(self, y, x, name, char, passable, actor=None, items=None):
        if items is None:
            items = list()
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.passable = passable
        self.actor = actor
        self.items = items


class DestructibleWall(Terrain):

    def __init__(self, y, x):
        super().__init__(y, x, "Destructible Wall", "#", False)


class IndestructibleWall(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Indestructible Wall", "#", False)


class Floor(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Floor", ".", True)


class Door(Terrain):
    def __init__(self, y, x, open=False):
        super().__init__(y, x, "Door", "D", True)
        self.open = open
