import random


class Item:
    def __init__(self, type, name):
        self.name = name


class Body(Item):
    def __init__(self, name, dodge, soak):
        super().__init__("body", name)
        self.dodge = dodge
        self.soak = soak


class Weapon(Item):
    def __init__(self, name, one_handed, damage, hit_modifier):
        super().__init__("weapon", name)
        self.damage = damage
        self.hit_modifier = hit_modifier
        self.one_handed = one_handed


class PlateArmor(Body):
    def __init__(self):
        super().__init__("Plate Armor", 0, 7)


class LeatherArmor(Body):
    def __init__(self):
        super().__init__("Leather Armor", 10, 2)


class Hide(Body):
    def __init__(self):
        super().__init__("Hide", 3, 1)


class Jelly_Body(Body):
    def __init__(self):
        super().__init__("Jelly body", 2, 4)


class Claws(Weapon):
    def __init__(self):
        super().__init__("Claws", True, 2, 75)


class Warhammer(Weapon):
    def __init__(self):
        super().__init__("Warhammer", False, 12, 25)


class LongSword(Weapon):
    def __init__(self):
        super().__init__("Long Sword", True, 6, 50)


class Tentacle(Weapon):
    def __init__(self):
        super().__init__("Tentacle", True, 3, 75)


# rings
def generate_increase():
    import main
    rand = random.randint(0, 100)
    rand_with_bonus = rand + main.player.luck + main.current_level * 5
    if rand == 100:
        return 15
    elif rand_with_bonus < 60:
        return random.randint(1, 3)
    elif rand_with_bonus < 100:
        return random.randint(4, 6)
    elif rand_with_bonus < 110:
        return random.randint(7, 9)
    else:
        return 10


class Ring(Item):
    def __init__(self, name, stat, increase):
        super().__init__("ring", name)
        self.stat = stat
        self.increase = increase


class RingOfDexterity(Ring):
    def __init__(self):
        increase = generate_increase()
        super().__init__(f"+{increase} Ring of Dexterity", "dexterity", increase)


class RingOfStrength(Ring):
    def __init__(self):
        increase = generate_increase()
        super().__init__(f"+{increase} Ring of Strength", "strength", increase)


class RingOfIntelligence(Ring):
    def __init__(self):
        increase = generate_increase()
        super().__init__(f"+{increase} Ring of Intelligence", "intelligence", increase)


class RingOfLuck(Ring):
    def __init__(self):
        increase = generate_increase()
        super().__init__(f"+{increase} Ring of Luck", "luck", increase)


class RingOfCurse(Ring):
    def __init__(self):
        increase = generate_increase()
        super().__init__(f"+{increase} Ring of Curse", "curse", increase)


# amulets
class Amulet(Item):
    def __init__(self, name):
        super().__init__("neck", name)


class AmuletOfProtection(Amulet):
    def __init__(self):
        super().__init__("Amulet of Protection")


class AmuletOfHealth(Amulet):
    def __init__(self):
        super().__init__("Amulet of Health")


class AmuletOfRegeneration(Amulet):
    def __init__(self):
        super().__init__("Amulet of Regeneration")


class AmuletOfMana(Amulet):
    def __init__(self):
        super().__init__("Amulet of Mana")


# capes
class Cape(Item):
    def __init__(self, name, dodge, soak):
        super().__init__("back", name)
        self.dodge = dodge
        self.soak = soak


class CapeOfDodge(Cape):
    def __init__(self):
        super().__init__("Cape of Dodge", 3, 0)


class Consumable(Item):
    def __init__(self, name):
        super().__init__("consumable", name)


class HealingPotion(Consumable):
    def __init__(self):
        super().__init__("Healing Potion")


class ManaPotion(Consumable):
    def __init__(self):
        super().__init__("Mana Potion")


class StrengthPotion(Consumable):
    def __init__(self):
        super().__init__("Strength Potion")


class DexterityPotion(Consumable):
    def __init__(self):
        super().__init__("Dexterity Potion")


class Intelligence(Consumable):
    def __init__(self):
        super().__init__("Intelligence Potion")


class LuckPotion(Consumable):
    def __init__(self):
        super().__init__("Luck Potion")


class CursePotion(Consumable):
    def __init__(self):
        super().__init__("Curse Potion")


class Runestone(Consumable):
    pass
