
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
