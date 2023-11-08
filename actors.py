import screen


class Actors:

    def __init__(self, y, x, char):
        self.y = y
        self.x = x
        self.char = char

    def move(self, win, y, x):
        import main
        if y == 0 and x == 0:
            screen.update_chat(win, "You waited.")
        elif main.terrain_map[self.y + y][self.x + x].passable:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.update_terrain(win, main.terrain_map, main.map_height, main.map_width)
            screen.update_chat(win, "You walked.")
        else:
            screen.update_chat(win, "You tried to walk into the wall.")
