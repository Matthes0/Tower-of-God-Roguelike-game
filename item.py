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
    def __init__(self, on_map, y, x, name, one_handed, damage, hit_modifier):
        super().__init__(on_map, y, x, name)
        self.damage = damage
        self.hit_modifier = hit_modifier
        self.one_handed = one_handed


class PlateArmor(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Plate Armor", 0, 7)


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Leather Armor", 10, 2)


class Hide(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Hide", 3, 1)
class Jelly_Body(Armor):
    def __init__(self):
        super().__init__(False, -1, -1, "Jelly body", 2, 4)

class Claws(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Claws", True, 2, 75)


class Warhammer(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Warhammer", False, 12, 25)


class LongSword(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Long Sword", True, 6, 50)


class Tentacle(Weapon):
    def __init__(self):
        super().__init__(False, -1, -1, "Tentacle", True, 3, 75)

# rings
class Ring(Item):
    def __init__(self, on_map, y, x, name):
        super().__init__(on_map, y, x, name)


class RingOfDexterity(Ring):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Dexterity")


class RingOfStrength(Ring):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Strength")


class RingOfIntelligence(Ring):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Intelligence")


class RingOfLuck(Ring):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Luck")


class RingOfCurse(Ring):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Curse")


# amulets
class Amulet(Item):
    def __init__(self, on_map, y, x, name):
        super().__init__(on_map, y, x, name)


class AmuletOfProtection(Amulet):
    def __init__(self):
        super().__init__(False, -1, -1, "Ring of Curse")


class AmuletOfHealth(Amulet):
    def __init__(self):
        super().__init__(False, -1, -1, "Amulet of Health")


class AmuletOfRegeneration(Amulet):
    def __init__(self):
        super().__init__(False, -1, -1, "Amulet of Regeneration")


class AmuletOfMana(Amulet):
    def __init__(self):
        super().__init__(False, -1, -1, "Amulet of Mana")


class AmuletOfSeeingInvisible(Amulet):
    def __init__(self):
        super().__init__(False, -1, -1, "Amulet of Seeing Invisible")


# capes
class Cape(Item):
    def __init__(self, on_map, y, x, name, dodge, soak):
        super().__init__(on_map, y, x, name)
        self.dodge = dodge
        self.soak = soak


class CapeOfDodge(Cape):
    def __init__(self):
        super().__init__(False, -1, -1, "Cape of Dodge", 3, 0)