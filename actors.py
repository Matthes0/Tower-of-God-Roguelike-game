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
            attacker.weapon.damage * roll_damage) + attacker.strength + attacker.curse - defender.armor.soak
        if damage > 0:
            if is_printing == 1:
                print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack hit. It deals {damage} damage.", end="")
            defender.deal_damage(damage)
            screen.update_chat(f"{attacker.name} hit {defender.name}. It deals {damage} damage.")
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
            screen.update_chat(f"{attacker.name} hit {defender.name}. It deals only 1 damage.")
            if defender.is_alive() is True:
                if is_printing == 1:
                    print(f" Now it's {defender.name} turn.")
            else:
                if is_printing == 1:
                    print(f" {defender.name} is dead.")
    else:
        screen.update_chat(f"{attacker.name} attack missed {defender.name}.")
        if is_printing == 1:
            print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack missed. Now it's {defender.name} turn.")


class Actors:
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed=1.0):
        self.left_hand = None
        self.right_hand = None
        self.armor = None
        self.head = None
        self.body = None
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
        self.max_mp = max_mp
        self.current_mp = max_mp
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.luck = luck
        self.curse = curse
        self.current_turn = 0
        self.speed = speed
        import main
        main.turn_list.append(self)
        self.temp_effects = []

    def tick_temp_effects(self):
        for effect in self.temp_effects:
            effect[0] -= 1
            if effect[0] == 0:
                effect[1].buff(self)


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
            case "legs":
                if self.legs is None:
                    return "None"
                return self.legs.name
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

    def die(self):
        import main
        main.terrain_map[self.y][self.x].actor = None
        screen.update_chat(f"{self.name} is dead.")
        if self in main.turn_list:
            main.turn_list.remove(self)

    def can_cast(self, cost):
        if self.current_mp >= cost:
            self.drain_mp(cost)
            return True
        screen.update_chat("Not enough mana.")
        return False

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def restore_mp(self, amount):
        self.current_mp += amount
        if self.current_mp > self.max_hp:
            self.current_hp = self.max_hp

    def drain_mp(self, amount):
        self.current_mp -= amount
        if self.current_mp < 0:
            self.current_mp = 0

    def deal_damage(self, amount):
        self.current_hp -= amount
        if self.is_alive() is False:
            self.current_hp = 0
            self.die()
    def modify_stat(self, stat, amount):
        match stat:
            case "strength":
                self.strength += amount
class Player(Actors):
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse)
        self.known_spells = []
        self.speed = 1.5
        import magic
        spell1 = magic.Smite()
        self.known_spells.append(spell1)
        spell2 = magic.Heal()
        self.known_spells.append(spell2)
        spell3 = magic.Pyroblast()
        self.known_spells.append(spell3)
        spell4 = magic.Heroism()
        self.known_spells.append(spell4)

    def move(self, y, x):
        import main
        if y == 0 and x == 0:
            screen.update_chat("You waited.")
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][self.x + x].actor is None:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.calculate_circle(self, 100)
            screen.update_terrain()

            if main.terrain_map[self.y][self.x].items is not None and bool(main.terrain_map[self.y][self.x].items):
                tmp = "You walked. There are items on this tile: "
                for thing in main.terrain_map[self.y][self.x].items:
                    tmp = tmp + thing.name + ", "
                tmp = tmp[:len(tmp) - 2]
                screen.update_chat(tmp)
            else:
                screen.update_chat("You walked.")
        elif main.terrain_map[self.y + y][self.x + x].name == "Door":
            main.terrain_map[self.y + y][self.x + x].passable = True
            main.terrain_map[self.y + y][self.x + x].char = 'o'
            screen.update_chat("You opened the door.")
        elif main.terrain_map[self.y + y][self.x + x].passable is False:
            screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].name}.")
        elif main.terrain_map[self.y + y][self.x + x].actor is not None:
            # screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].actor.name}.")
            melee_attack(self, main.terrain_map[self.y + y][self.x + x].actor)

class Hostile(Actors):
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed)
    def move(self, y, x):
        import main
        if x == 0 and y == 0:
            pass
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][self.x + x].actor is None:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.update_terrain()
        elif main.terrain_map[self.y + y][self.x + x].actor is not None:
            melee_attack(self, main.terrain_map[self.y + y][self.x + x].actor)



class Human(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'human', 10, 10, 5, 5,5, 5, 0)


class HumanWithPlateArmorAndWarhammer(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Human with plate armor and warhammer', 10, 10, 5, 5, 5, 5, 0)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.PlateArmor())


class HumanWithLeatherArmorAndLongsword(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Human with leather armor and longsword', 10, 10, 5, 5, 5, 5, 0, 1.0)
        self.equip_weapon(item.LongSword())
        self.equip_armor(item.LeatherArmor())


class Dog(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'd', 'Dog', 5, 0, 1, 2, 2,3, 1)
        self.equip_weapon(item.Claws())
        self.equip_armor(item.Hide())


class GreenJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Green Jelly', 9, 0, 2, 2,3, 5, 1)
        self.equip_weapon(item.Tentacle())
        self.equip_armor(item.Jelly_Body())


class BlueJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Blue Jelly', 18, 0, 3, 5, 3, 5, 1)
        self.equip_weapon(item.Tentacle())
        self.equip_armor(item.Jelly_Body())


class Oni(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'oni', 60, 0, 15, 3, 2, 5, 3)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.Hide())


class TowerMaster(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'Tower Master', 250, 0, 45, 45, 30, 15, 15)
        self.equip_weapon(item.Warhammer())
        self.equip_armor(item.Hide())
