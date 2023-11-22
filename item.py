class Item:
    def __init__(self, on_map, y, x, name):
        self.on_map = on_map
        self.y = y
        self.x = x
        self.name = name


class Armor(Item):
    def __init__(self, on_map, y, x, name, dodge, soak):
        super().__init__(on_map, y, x, name)
        self.dodge = dodge
        self.soak = soak


class Weapon(Item):
    def __init__(self, on_map, y, x, name, damage, hit_modifier):
        super().__init__(on_map, y, x, name)
        self.damage = damage
        self.hit_modifier = hit_modifier


class PlateArmor(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Plate Armor", 0, 5)


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Leather Armor", 10, 2)


class Hide(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Hide", 3, 1)


class Claws(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Claws", 2, 75)


class Warhammer(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Warhammer", 10, 25)


class LongSword(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Long Sword", 4, 50)
