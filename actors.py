import screen


class Actors:

    def __init__(self, y, x, char):
        self.y = y
        self.x = x
        self.char = char


class Playable(Actors):
    def __init__(self, y, x, char, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char)
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mp = max_mp
        self.current_mp = max_mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.luck = luck
        self.curse = curse


class Player(Playable):

    def __init__(self, y, x, char, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, max_hp, max_mp, strength, dexterity, intelligence, luck, curse)

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
            screen.update_chat(win, f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].name}.")


class Hostile(Playable):
    pass
