import random



def generate_terrain(y, x, type_of_gen, level = 0):
    map_list = [[0] * x for i in range(0, y)]
    for i in range(0, y):
        for j in range(0, x):
            map_list[i][j] = IndestructibleWall(i, j)
    match type_of_gen:
        case "lobby":
            for i in range(12, 19):
                for j in range(12, 19):
                    map_list[i][j] = Floor(i, j)
            for i in range(12, 19):
                for j in range(22, 29):
                    map_list[i][j] = Floor(i, j)
            for i in range(12, 19):
                for j in range(1, 8):
                    map_list[i][j] = Floor(i, j)

            for i in range(22, 29):
                for j in range(12, 19):
                    map_list[i][j] = Floor(i, j)
            for i in range(1, 8):
                for j in range(12, 19):
                    map_list[i][j] = Floor(i, j)
            for i in range(14, 17):
                for j in range(1, 29):
                    map_list[i][j] = Floor(i, j)
            for i in range(1, 29):
                for j in range(14, 17):
                    map_list[i][j] = Floor(i, j)
            map_list[15][4] = Upstairs(15, 4, 0)
        case "1":
            min_size = 4
            max_size = 10
            rooms_count = random.randint(3,10)
            rooms = []
            for room in range(rooms_count):
                placed = 0
                while placed == 0:
                    tmp_height = random.randint(min_size, max_size)
                    y = random.randint(1, 50 - 2 - tmp_height)
                    tmp_width = random.randint(min_size, max_size)
                    x = random.randint(1, 50 - 2 - tmp_width)
                    tmp_room = Room(y, x, tmp_height, tmp_width)
                    if any(tmp_room.intersects(other_room) for other_room in rooms):
                        continue
                    for i in range(tmp_room.y1, tmp_room.y2):
                        for j in range(tmp_room.x1, tmp_room.x2):
                            map_list[i][j] = Floor(i, j)
                            placed = 1
                if len(rooms) > 0:
                    middle_prev_y = int((rooms[len(rooms)-1].y1+rooms[len(rooms)-1].y2)/2)
                    middle_prev_x = int((rooms[len(rooms)-1].x1+rooms[len(rooms)-1].x2)/2)
                    middle_curr_x = int((tmp_room.x1+tmp_room.x2)/2)
                    middle_curr_y = int((tmp_room.y1+tmp_room.y2)/2)
                    prev_y = -1
                    prev_x = -1
                    door_placed = False
                    for x, y in corridor(middle_prev_y,middle_prev_x, middle_curr_y,middle_curr_x):
                        if prev_y != -1 and prev_x != -1 and map_list[prev_y][prev_x].name == "Floor" and map_list[y][x].char == "#" and door_placed is False:
                            map_list[y][x] = Door(y,x)
                            door_placed = True
                        else:
                            map_list[y][x] = Floor(y, x)
                        prev_y = y
                        prev_x = x
                rooms.append(tmp_room)
            while True:
                y = random.randint(1, 50-2)
                x = random.randint(1, 50-2)
                if map_list[y][x].passable is True:
                    map_list[y][x] = Downstairs(y,x, level)
                    break
            while True:
                y = random.randint(1, 50-2)
                x = random.randint(1, 50-2)
                if map_list[y][x].passable is True and map_list[y][x].name != "Downstairs":
                    map_list[y][x] = Upstairs(y,x, level)
                    break
    return map_list

def corridor(middle_prev_y,middle_prev_x, middle_curr_y,middle_curr_x):

    if random.random() < 0.5:
        corner_x, corner_y = middle_curr_x, middle_prev_y
    else:
        corner_x, corner_y = middle_prev_x, middle_curr_y
    for x, y in bresenham(middle_prev_x,middle_prev_y,corner_x,corner_y):
        yield x, y
    for x, y in bresenham(corner_x, corner_y, middle_curr_x,middle_curr_y):
        yield x, y


def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
class Room:
    def __init__(self, y, x, height, width):
        self.y1 = y
        self.y2 = y + height
        self.x1 = x
        self.x2 = x + width

    def intersects(self, other) -> bool:
        return (
                self.x1 <= other.x2
                and self.x2 >= other.x1
                and self.y1 <= other.y2
                and self.y2 >= other.y1
        )



def can_place_item(y, x):
    import main, screen
    if x > main.map_width or y > main.map_height:
        screen.update_chat(f"Can't place item at {y},{x} because it is out of bounds")
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can place item at {y},{x}")
        return 1
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can't place item at {y},{x} because there are too many items")
        return 2.
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place item at {y},{x} because {main.terrain_map[y][x].name} is a terrain here")
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(
            f"Can't place item at {y},{x} because there are too many items and {main.terrain_map[y][x].name} is a terrain here")
        return 2
    else:
        screen.update_chat("Something went wrong during can_place_item")
    return 0


def can_place_actor(y, x):
    import main, screen
    if x > main.map_width - 1 or y > main.map_height - 1:
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
        screen.update_chat(
            f"Can't place actor at {y},{x} because {main.terrain_map[y][x].actor.char} is here and {main.terrain_map[y][x].name} is a terrain here")
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
    def __init__(self, y, x, name, char, passable, actor=None):
        self.items = []
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.passable = passable
        self.actor = actor
        self.visible = False
        self.see_through = True


class DestructibleWall(Terrain):

    def __init__(self, y, x):
        super().__init__(y, x, "Destructible Wall", "#", False)
        self.see_through = False


class IndestructibleWall(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Indestructible Wall", "#", False)
        self.see_through = False


class Floor(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Floor", ".", True)


class Door(Terrain):
    def __init__(self, y, x, open=False):
        super().__init__(y, x, "Door", "D", False)
        self.open = open
        self.see_through = False


class Upstairs(Terrain):
    def __init__(self, y, x, level):
        super().__init__(y, x, "Upstairs", "<", True)
        self.level = level


class Downstairs(Terrain):
    def __init__(self, y, x, level):
        super().__init__(y, x, "Downstairs", ">", True)
        self.level = level


class FireWall(Terrain):
    pass


class Mud(Terrain):
    def __init__(self, y, x):
        super().__init__(y, x, "Mud", "~", True)
