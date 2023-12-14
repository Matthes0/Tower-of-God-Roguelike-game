import item
import screen


def melee_attack(attacker, defender, is_printing=0):
    import random
    import math
    hit_chance = attacker.weapon.hit_modifier + attacker.dexterity + attacker.curse - defender.armor.dodge - defender.dexterity + defender.curse
    if hit_chance < 5:
        hit_chance = 5
    roll = random.randint(1, 100)
    if roll <= hit_chance:

        roll_damage = random.uniform(0.50, 1.50)
        damage = math.floor(
            attacker.weapon.damage * roll_damage) + attacker.strength + attacker.curse + defender.curse - defender.armor.soak
        if damage > 0:
            if is_printing == 1:
                print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack hit. It deals {damage} damage.", end="")
            defender.deal_damage(damage)
            if defender.is_alive() is True:
                if is_printing == 1:
                    print(f" Now it's {defender.name} turn.")
            else:
                if is_printing == 1:
                    print(f" {defender.name} is dead.")
        else:
            if is_printing == 1:
                print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack hit. It deals only 1 damage.", end="")
            defender.deal_damage(1)
            if defender.is_alive() is True:
                if is_printing == 1:
                    print(f" Now it's {defender.name} turn.")

            else:
                if is_printing == 1:
                    print(f" {defender.name} is dead.")
    else:
        if is_printing == 1:
            print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack missed. Now it's {defender.name} turn.")


class Actors:
    def __init__(self, y, x, char, name, max_hp, strength, dexterity, luck, curse):
        self.left_hand = None
        self.right_hand = None
        self.armor = None
        self.head = None
        self.body = None
        self.hands = None
        self.legs = None
        self.back = None
        self.ring_1 = None
        self.ring_2 = None
        self.neck = None
        self.weapon = None
        self.backpack = []
        self.equipment = []
        self.y = y
        self.x = x
        self.char = char
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.dexterity = dexterity
        self.luck = luck
        self.curse = curse

    def get_name(self, attrib):
        match attrib:
            case "left_hand":
                if self.left_hand is None:
                    return "None"
                return self.left_hand.name
            case "right_hand":
                if self.right_hand is None:
                    return "None"
                return self.right_hand.name
            case "head":
                if self.head is None:
                    return "None"
                return self.head.name
            case "body_armor":
                if self.body is None:
                    return "None"
                return self.body.name
            case "hands":
                if self.hands is None:
                    return "None"
                return self.hands.name
            case "legs":
                if self.legs is None:
                    return "None"
                return self.hands.name
            case "back":
                if self.back is None:
                    return "None"
                return self.back.name
            case "ring_1":
                if self.ring_1 is None:
                    return "None"
                return self.ring_1.name
            case "ring_2":
                if self.ring_2 is None:
                    return "None"
                return self.ring_2.name
            case "neck":
                if self.neck is None:
                    return "None"
                return self.neck.name

    def equip_weapon(self, weapon):
        if weapon.one_handed:
            self.left_hand = weapon
        else:
            self.left_hand = weapon
            self.right_hand = weapon
        self.weapon = weapon

    def deequip_weapons(self):
        self.left_hand = None
        self.right_hand = None

    def equip_armor(self, armor):
        self.body = armor
        self.armor = armor

    def pick_item(self):
        import main
        if main.terrain_map[self.y][self.x].items is not None:
            for item in main.terrain_map[self.y][self.x].items:
                self.backpack.append(item)
                screen.update_chat(f"You picked up {item.name}.")
            main.terrain_map[self.y][self.x].items.clear()

    def is_alive(self):
        if self.current_hp > 0:
            return True
        else:
            return False

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def deal_damage(self, amount):
        self.current_hp -= amount
        if self.is_alive() is False:
            self.current_hp = 0


class Player(Actors):

    def __init__(self, y, x, char, name, max_hp, strength, dexterity, luck, curse):
        super().__init__(y, x, char, name, max_hp, strength, dexterity, luck, curse)

    def move(self, y, x):
        import main
        if y == 0 and x == 0:
            screen.update_chat("You waited.")
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][self.x + x].actor is None:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.calculate_circle(self, 4.5)
            screen.update_terrain()

            if main.terrain_map[self.y][self.x].items is not None and bool(main.terrain_map[self.y][self.x].items):
                tmp = "You walked. There are items on this tile: "
                for thing in main.terrain_map[self.y][self.x].items:
                    tmp = tmp + thing.name + ", "
                tmp = tmp[:len(tmp) - 2]
                screen.update_chat(tmp)
            else:
                screen.update_chat("You walked.")
        elif main.terrain_map[self.y + y][self.x + x].passable is False:
            screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].name}.")
        elif main.terrain_map[self.y + y][self.x + x].actor is not None:
            screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].actor.name}.")


class Hostile(Actors):
    def __init__(self, y, x, char, name, max_hp, strength, dexterity, luck, curse):
        super().__init__(y, x, char, name, max_hp, strength, dexterity, luck, curse)


class Human(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'human', 10, 5, 5, 5, 0)


class HumanWithPlateArmorAndWarhammer(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Human with plate armor and warhammer', 10, 5, 5, 5, 0)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.PlateArmor())


class HumanWithLeatherArmorAndLongsword(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Human with leather armor and longsword', 10, 5, 5, 5, 0)
        self.equip_weapon(item.LongSword())
        self.equip_armor(item.LeatherArmor())


class Dog(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'd', 'dog', 5, 1, 2, 3, 1)
        self.equip_weapon(item.Claws())
        self.equip_armor(item.Hide())


class GreenJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Green Jelly', 9, 2, 3, 5, 1)
        self.equip_weapon(item.Tentacle())
        self.equip_armor(item.Jelly_Body())


class BlueJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Blue Jelly', 18, 3, 5, 5, 1)
        self.equip_weapon(item.Tentacle())
        self.equip_armor(item.Jelly_Body())


class Oni(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'oni', 60, 15, 3, 5, 3)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.Hide())


class TowerMaster(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'Tower Master', 250, 45, 45, 15, 15)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.Hide())
