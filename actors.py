import screen


class Actors:

    def __init__(self, y, x, char, name):
        self.y = y
        self.x = x
        self.char = char
        self.name = name


class Playable(Actors):
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, name)
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

    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse)

    def move(self, y, x):
        import main
        if y == 0 and x == 0:
            screen.update_chat("You waited.")
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][self.x + x].actor is None:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.update_terrain()
            screen.update_chat("You walked.")
        elif main.terrain_map[self.y + y][self.x + x].passable is False:
            screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].name}.")
        elif main.terrain_map[self.y + y][self.x + x].actor is not None:
            screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].actor.name}.")



class Hostile(Actors):
    def __init__(self, y, x, char, name):
        super().__init__(y, x, char, name)


class Human(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Human')


class Dog(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'd', 'dog')
