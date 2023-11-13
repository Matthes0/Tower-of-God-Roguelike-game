import main, screen


def can_place_item(y, x):
    if x > main.map_width or y > main.map_height:
        screen.update_chat(f"Can't place item at {y},{x} because it is out of bounds")
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can place item at {y},{x}")
        return 1
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is True:
        screen.update_chat(f"Can't place item at {y},{x} because there are too many items")
    elif len(main.terrain_map[y][x].items) < 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place item at {y},{x} because {main.terrain_map[y][x].name} is a terrain here")
    elif len(main.terrain_map[y][x].items) >= 2 and main.terrain_map[y][x].passable is False:
        screen.update_chat(f"Can't place item at {y},{x} because there are too many items and "
                           f"{main.terrain_map[y][x].name} is a terrain here")
    else:
        screen.update_chat("Something went wrong during can_place_item")
    return 0

def can_place_actor(y, x):
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
        screen.update_chat(f"Can't place actor at {y},{x} because {main.terrain_map[y][x].actor.char} is here and "
                           f"{main.terrain_map[y][x].name} is a terrain here")
        return 2
    else:
        screen.update_chat("Something went wrong during can_place_actor")
    return 0

def print_actors_and_items():
    pass


def player_coordinates():
    pass
