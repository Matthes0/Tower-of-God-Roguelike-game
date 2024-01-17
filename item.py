class Item:
    def __init__(self, y, x, name):
        self.y = y
        self.x = x
        self.name = name


class Armor(Item):
    def __init__(self, y, x, name, dodge, soak):
        super().__init__(y, x, name)
        self.dodge = dodge
        self.soak = soak


class Weapon(Item):
    def __init__(self, y, x, name, one_handed, damage, hit_modifier):
        super().__init__(y, x, name)
        self.damage = damage
        self.hit_modifier = hit_modifier
        self.one_handed = one_handed


class PlateArmor(Armor):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Plate Armor", 0, 7)


class LeatherArmor(Armor):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Leather Armor", 10, 2)


class Hide(Armor):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Hide", 3, 1)


class Jelly_Body(Armor):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Jelly body", 2, 4)


class Claws(Weapon):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Claws", True, 2, 75)


class Warhammer(Weapon):
    def __init__(self, y=-1, x=-1):
        super().__init__(y,x, "Warhammer", False, 12, 25)


class LongSword(Weapon):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Long Sword", True, 6, 50)


class Tentacle(Weapon):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Tentacle", True, 3, 75)


# rings
class Ring(Item):
    def __init__(self, y, x, name):
        super().__init__(y, x, name)


class RingOfDexterity(Ring):
    def __init__(self):
        super().__init__(-1, -1, "Ring of Dexterity")


class RingOfStrength(Ring):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Ring of Strength")


class RingOfIntelligence(Ring):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Ring of Intelligence")


class RingOfLuck(Ring):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Ring of Luck")


class RingOfCurse(Ring):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Ring of Curse")


# amulets
class Amulet(Item):
    def __init__(self, y, x, name):
        super().__init__(y, x, name)


class AmuletOfProtection(Amulet):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Ring of Curse")


class AmuletOfHealth(Amulet):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Amulet of Health")


class AmuletOfRegeneration(Amulet):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Amulet of Regeneration")


class AmuletOfMana(Amulet):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Amulet of Mana")


class AmuletOfSeeingInvisible(Amulet):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Amulet of Seeing Invisible")


# capes
class Cape(Item):
    def __init__(self, y, x, name, dodge, soak):
        super().__init__(y, x, name)
        self.dodge = dodge
        self.soak = soak


class CapeOfDodge(Cape):
    def __init__(self, y = -1, x = -1):
        super().__init__(y, x, "Cape of Dodge", 3, 0)


class Consumable(Item):
    def __init__(self, y, x, name):
        super().__init__(y, x, name)
class HealingPotion(Consumable):
    def __init__(self, y = -1, x = -1):
        super().__init__(y,x, "Healing Potion")


class ManaPotion(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Mana Potion")
class StrengthPotion(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Strength Potion")

class DexterityPotion(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Dexterity Potion")
class Intelligence(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Intelligence Potion")
class LuckPotion(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Luck Potion")
class CursePotion(Consumable):
    def __init__(self, y=-1, x=-1):
        super().__init__(y, x, "Curse Potion")

class Runestone(Consumable):
    pass