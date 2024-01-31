import random


class Item:
    def __init__(self, type, name, is_worn=False):
        self.type = type
        self.name = name
        self.is_worn = is_worn
def random_item():
    kind = random.randint(1,8)
    match kind:
        case 1:
            item_rolled = random.randint(1, 3)
            match item_rolled:
                case 1:
                    return LeatherArmor()
                case 2:
                    return MailArmor()
                case 3:
                    return PlateArmor()
        case 2:
            item_rolled = random.randint(1, 5)
            match item_rolled:
                case 1:
                    return LongSword()
                case 2:
                    return Warhammer()
                case 3:
                    return Dagger()
                case 4:
                    return ExplosiveCrystal()
                case 5:
                    return Longbow()
        case 3:
            item_rolled = random.randint(1,5)
            match item_rolled:
                case 1:
                    return RingOfStrength()
                case 2:
                    return RingOfDexterity()
                case 3:
                    return RingOfIntelligence()
                case 4:
                    return RingOfLuck()
                case 5:
                    return RingOfCurse()
        case 4:
            item_rolled = random.randint(1, 4)
            match item_rolled:
                case 1:
                    return AmuletOfHpRegeneration()
                case 2:
                    return AmuletOfMpRegeneration()
                case 3:
                    return AmuletOfHealth()
                case 4:
                    return AmuletOfMana()
        case 5:
            item_rolled = random.randint(1, 2)
            match item_rolled:
                case 1:
                    return CapeOfProtection()
                case 2:
                    return CapeOfDodge()
        case 6:
            item_rolled = random.randint(1, 3)
            match item_rolled:
                case 1:
                    return LeatherLegs()
                case 2:
                    return MailLegs()
                case 3:
                    return PlateLegs()
        case 7:
            item_rolled = random.randint(1, 3)
            match item_rolled:
                case 1:
                    return LeatherHelmet()
                case 2:
                    return MailHelmet()
                case 3:
                    return PlateHelmet()
        case 8:
            item_rolled = random.randint(1, 7)
            match item_rolled:
                case 1:
                    return HealingPotion()
                case 2:
                    return ManaPotion()
                case 3:
                    return StrengthPotion()
                case 4:
                    return DexterityPotion()
                case 5:
                    return IntelligencePotion()
                case 6:
                    return LuckPotion()
                case 7:
                    return CursePotion()



class Weapon(Item):
    def __init__(self, name, damage, hit_modifier):
        super().__init__("weapon", name)
        self.damage = damage
        self.hit_modifier = hit_modifier


class Body(Item):
    def __init__(self, name, dodge, soak):
        super().__init__("body", name)
        self.dodge = dodge
        self.soak = soak


class LeatherArmor(Body):
    def __init__(self):
        super().__init__("Leather Armor", 10, 2)

class MailArmor(Body):
    def __init__(self):
        super().__init__("Mail Armor", 0, 4)

class PlateArmor(Body):
    def __init__(self):
        super().__init__("Plate Armor", -10, 8)


class Hide(Body):
    def __init__(self):
        super().__init__("Hide", 3, 1)


class Jelly_Body(Body):
    def __init__(self):
        super().__init__("Jelly body", 2, 4)


class Claws(Weapon):
    def __init__(self):
        super().__init__("Claws",  2, 75)


class Warhammer(Weapon):
    def __init__(self):
        super().__init__("Warhammer",  12, 25)


class LongSword(Weapon):
    def __init__(self):
        super().__init__("Long Sword",  6, 50)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Long Sword", 2, 80)
class Tentacle(Weapon):
    def __init__(self):
        super().__init__("Tentacle",  3, 75)


class Ranged(Item):
    def __init__(self, name, damage, hit_modifier):
        super().__init__("ranged", name)
        self.damage = damage
        self.hit_modifier = hit_modifier
class Longbow(Ranged):
    def __init__(self):
        super().__init__("Longbow",  2, 60)
class ExplosiveCrystal(Ranged):
    def __init__(self):
        super().__init__("Explosive Crystal",  0,1)
class Helmet(Item):
    def __init__(self, name, dodge, soak):
        super().__init__("head", name)
        self.dodge = dodge
        self.soak = soak
class LeatherHelmet(Helmet):
    def __init__(self):
        super().__init__("Leather Helmet", 5, 0)
class MailHelmet(Helmet):
    def __init__(self):
        super().__init__("Mail Helmet", 0, 1)
class PlateHelmet(Helmet):
    def __init__(self):
        super().__init__("Plate Helmet", -7, 3)
class Legs(Item):
    def __init__(self, name, dodge, soak):
        super().__init__("legs", name)
        self.dodge = dodge
        self.soak = soak
class LeatherLegs(Legs):
    def __init__(self):
        super().__init__("Leather Helmet", 5, 0)
class MailLegs(Helmet):
    def __init__(self):
        super().__init__("Mail Helmet", 0, 1)
class PlateLegs(Helmet):
    def __init__(self):
        super().__init__("Plate Helmet", -7, 3)

def generate_increase(type):
    import main
    if type == "ring":
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
    if type == "amulet":
        rand = random.randint(0, 100)
        rand_with_bonus = rand + main.player.luck + main.current_level * 5
        if rand == 100:
            return 5
        elif rand_with_bonus < 60:
            return 1
        elif rand_with_bonus < 100:
            return 2
        else:
            return 3
    if type == "potion":
        rand = random.randint(0, 100)
        rand_with_bonus = rand + main.player.luck + main.current_level * 5
        if rand == 100:
            return 15
        elif rand == 1:
            return -10
        elif rand_with_bonus < 60:
            return random.randint(-5, -1)
        elif rand_with_bonus < 100:
            return random.randint(1, 4)
        elif rand_with_bonus < 110:
            return random.randint(5, 7)
        else:
            return 10



class Ring(Item):
    def __init__(self, name, stat, increase):
        super().__init__("ring", name)
        self.stat = stat
        self.increase = increase


class RingOfDexterity(Ring):
    def __init__(self):
        increase = generate_increase("ring")
        super().__init__(f"+{increase} Ring of Dexterity", "dexterity", increase)


class RingOfStrength(Ring):
    def __init__(self):
        increase = generate_increase("ring")
        super().__init__(f"+{increase} Ring of Strength", "strength", increase)


class RingOfIntelligence(Ring):
    def __init__(self):
        increase = generate_increase("ring")
        super().__init__(f"+{increase} Ring of Intelligence", "intelligence", increase)


class RingOfLuck(Ring):
    def __init__(self):
        increase = generate_increase("ring")
        super().__init__(f"+{increase} Ring of Luck", "luck", increase)


class RingOfCurse(Ring):
    def __init__(self):
        increase = generate_increase("ring")
        super().__init__(f"+{increase} Ring of Curse", "curse", increase)


# amulets
class Amulet(Item):
    def __init__(self, name, stat, increase):
        super().__init__("amulet", name)
        self.stat = stat
        self.increase = increase

class AmuletOfHealth(Amulet):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Amulet of Health", "max_hp", increase * 10)


class AmuletOfMana(Amulet):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Amulet of Mana", "max_mp", increase * 10)


class AmuletOfHpRegeneration(Amulet):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Amulet of HP Regeneration", "hp_regen", increase)


class AmuletOfMpRegeneration(Amulet):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Amulet of MP Regeneration", "mp_regen", increase)


# capes
class Cape(Item):
    def __init__(self, name, stat, increase):
        super().__init__("cape", name)
        self.stat = stat
        self.increase = increase


class CapeOfDodge(Cape):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Cape of Dodge", "dodge", increase)

class CapeOfProtection(Cape):
    def __init__(self):
        increase = generate_increase("amulet")
        super().__init__(f"+{increase} Cape of Protection", "soak", increase)


class Consumable(Item):
    def __init__(self, name, stat, increase):
        super().__init__("consumable", name)
        self.stat = stat
        self.increase = increase

class HealingPotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "max_hp", generate_increase("consumable"))


class ManaPotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "max_mp", generate_increase("consumable"))


class StrengthPotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "strength", generate_increase("consumable"))


class DexterityPotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "dexterity", generate_increase("consumable"))


class IntelligencePotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "intelligence", generate_increase("consumable"))


class LuckPotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "luck", generate_increase("consumable"))


class CursePotion(Consumable):
    def __init__(self):
        super().__init__("Unidentified Potion", "curse", generate_increase("consumable"))
