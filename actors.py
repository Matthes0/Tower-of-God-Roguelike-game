import screen

def melee_attack(attacker, defender):
    import random
    import math
    hit_chance = attacker.weapon.hit_modifier + attacker.dexterity + attacker.curse - defender.armor.dodge - defender.dexterity + defender.curse
    if hit_chance < 5:
        hit_chance = 5
    damage = 0
    roll_damage = 0.0
    roll = random.randint(1,100)
    if roll <= hit_chance:

        roll_damage = random.uniform(0.50, 1.50)
        damage = math.floor(attacker.weapon.damage * roll_damage) + attacker.strength + attacker.curse + defender.curse - defender.armor.soak
        if damage > 0:
            #print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack hit. It deals {damage} damage.", end="")
            defender.deal_damage(damage)
            if defender.is_alive() is True:
                #print(f" Now it's {defender.name} turn.")
                pass
            else:
                #print(f" {defender.name} is dead.")
                pass
        else:
            #print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack hit. It deals only 1 damage.", end="")
            defender.deal_damage(1)
            if defender.is_alive() is True:
                #print(f" Now it's {defender.name} turn.")
                pass
            else:
                #print(f" {defender.name} is dead.")
                pass
    else:
        #print(f"{attacker.name} rolled {roll} on {hit_chance}. Attack missed. Now it's {defender.name} turn.")
        pass
#zakomentowac printy przy testowaniu wielokrotnych walk, odkomentowac przy szczegolowej walce

class Actors:
    def __init__(self, y, x, char, name, max_hp, strength, dexterity, luck, curse):
        self.weapon = None
        self.armor = None
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

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

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
            screen.update_terrain()
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


class Dog(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'd', 'dog', 5, 1, 2, 3, 1)

class Oni(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'oni', 30, 9, 1, 2, 3)