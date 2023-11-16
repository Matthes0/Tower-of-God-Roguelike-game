import screen


def melee_attack(attacker, defender):
    import random
    from math import floor
    attack_pool = floor(attacker.dexterity / 3) + attacker.weapon.hit_modifier + floor(attacker.curse / 3)
    attack_success = 0
    dodge_success = 0
    damage_success = 0
    soak_success = 0
    for die in range(0, attack_pool):
        roll = random.randint(1, 10)
        match roll:
            case 1:
                attack_success -= 1
            case range(6, 9):
                attack_success += 1
            case 10:
                attack_success += 2
    if attack_success > 0:
        dodge_pool = floor(defender.dexterity / 3) + defender.armor.dodge - floor(defender.curse / 3)
        if dodge_pool > 0:
            for die in range(0, dodge_pool):
                roll = random.randint(1, 10)
                match roll:
                    case 1:
                        dodge_success -= 1
                    case range(6, 9):
                        dodge_success += 1
                    case 10:
                        dodge_success += 2
            if dodge_success < attack_success:
                damage_pool = floor(attacker.strength / 3) + attacker.weapon.damage + floor(attacker.curse / 3)
                soak_pool = floor(defender.armor.soak - defender.curse / 3)
                for die in range(0, damage_pool):
                    roll = random.randint(1, 10)
                    match roll:
                        case 1:
                            damage_success -= 1
                        case range(6, 9):
                            damage_success += 1
                        case 10:
                            damage_success += 2
                for die in range(0, soak_pool):
                    roll = random.randint(1, 10)
                    match roll:
                        case 1:
                            soak_success -= 1
                        case range(6, 9):
                            soak_success += 1
                        case 10:
                            soak_success += 2
                damage = damage_success - soak_success
                if damage > 0:
                    defender.current_hp -= damage


class Actors:
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        self.weapon = None
        self.armor = None
        self.y = y
        self.x = x
        self.char = char
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mp = max_mp
        self.current_mp = max_mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.luck = luck
        self.curse = curse

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor


class Player(Actors):

    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse)

    def move(self, y, x):
        import main
        if y == 0 and x == 0:
            screen.update_chat("You waited.")
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][
            self.x + x].actor is None:
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
