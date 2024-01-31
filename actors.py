import item
import screen


def melee_attack(attacker, defender):
    import random
    import math
    hit_chance = attacker.total_hit_modifier + attacker.dexterity + attacker.curse - defender.total_dodge - defender.dexterity + defender.curse
    if hit_chance < 5:
        hit_chance = 5
    roll = random.randint(1, 100)
    if roll <= hit_chance:
        roll_damage = random.uniform(0.50, 1.50)
        damage = math.floor(
            attacker.total_damage * roll_damage) + attacker.strength + attacker.curse - defender.total_soak
        if damage > 0:
            screen.update_chat(f"{attacker.name} hit {defender.name}. It deals {damage} damage.")
            defender.deal_damage(damage)
        else:
            defender.deal_damage(1)
            screen.update_chat(f"{attacker.name} hit {defender.name}. It deals only 1 damage.")
    else:
        screen.update_chat(f"{attacker.name} attack missed {defender.name}.")


class HpRegen:
    def cast(self, caster):
        temp_effect = [4, self]
        caster.temp_effects.append(temp_effect)

    def end_effect(self, target):
        target.heal(target.hp_regen)
        temp_effect = [4, self]
        target.temp_effects.append(temp_effect)


class MpRegen:
    def cast(self, caster):
        temp_effect = [4, self]
        caster.temp_effects.append(temp_effect)

    def end_effect(self, target):
        target.restore_mp(target.mp_regen)
        temp_effect = [4, self]
        target.temp_effects.append(temp_effect)


def is_valid_move(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def dijkstra_pathfinding(start, end):
    rows, cols = 50, 50
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    start_x, start_y = start
    distances[start_x][start_y] = 0

    priority_queue = [(0, start_x, start_y)]

    def get_cost(x, y):
        import main
        cell = main.terrain_map[y][x]
        if cell.name == 'Door' and cell.char != "o" or cell.actor is not None:
            return 2
        elif cell.char == "#":
            return float('inf')
        else:
            return 1

    while priority_queue:
        import heapq
        cost, x, y = heapq.heappop(priority_queue)

        if visited[x][y]:
            continue

        visited[x][y] = True

        if (x, y) == end:
            break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if not is_valid_move(new_x, new_y, rows, cols) or visited[new_x][new_y]:
                continue

            new_cost = cost + get_cost(new_x, new_y)

            if new_cost < distances[new_x][new_y]:
                distances[new_x][new_y] = new_cost
                heapq.heappush(priority_queue, (new_cost, new_x, new_y))

    # Reconstruct the path
    path = []
    x, y = end

    while (x, y) != start:
        path.append((x, y))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid_move(new_x, new_y, rows, cols) and distances[x][y] == distances[new_x][new_y] + get_cost(x, y):
                x, y = new_x, new_y
                break

    path.append(start)
    return path[::-1]


class Actors:
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed=1.0):
        # attributes
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.luck = luck
        self.curse = curse
        self.speed = speed

        # stats depending on attributes
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.max_mp = max_mp
        self.current_mp = self.max_mp
        self.total_damage = 0
        self.total_hit_modifier = 0
        self.total_dodge = 0
        self.total_soak = 0
        # others
        self.y = y
        self.x = x
        self.char = char
        self.name = name
        self.hp_regen = 1
        self.mp_regen = 1
        self.backpack = []
        self.weapon = None
        self.head = None
        self.body = None
        self.legs = None
        self.cape = None
        self.ring_1 = None
        self.ring_2 = None
        self.amulet = None

        self.current_turn = 0
        self.temp_effects = []
        self.const_effects = []
        regenerating_hp = HpRegen()
        regenerating_hp.cast(self)
        regenerating_mana = MpRegen()
        regenerating_mana.cast(self)
        import main
        main.turn_list.append(self)

    def tick_temp_effects(self):
        for effect in self.temp_effects:
            effect[0] -= 1
            if effect[0] == 0:
                effect[1].end_effect(self)

    def get_name(self, attrib):
        match attrib:
            case "weapon":
                if self.weapon is None:
                    return "None"
                return self.weapon.name
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
            case "cape":
                if self.cape is None:
                    return "None"
                return self.cape.name
            case "ring_1":
                if self.ring_1 is None:
                    return "None"
                return self.ring_1.name
            case "ring_2":
                if self.ring_2 is None:
                    return "None"
                return self.ring_2.name
            case "amulet":
                if self.amulet is None:
                    return "None"
                return self.amulet.name

    def equip(self, item, ring=0):
        if item.type == "weapon":
            self.deequip("weapon")
            self.weapon = item
            self.total_damage += self.weapon.damage
            self.total_hit_modifier += self.weapon.hit_modifier
            item.is_worn = True
        elif item.type == "cape":
            self.deequip("cape")
            self.cape = item
            self.modify_stat(item.stat, item.increase)
            item.is_worn = True
        elif item.type == "head":
            self.deequip("head")
            self.head = item
            self.total_dodge += self.head.dodge
            self.total_soak += self.head.soak
            item.is_worn = True
        elif item.type == "legs":
            self.deequip("legs")
            self.legs = item
            self.total_dodge += self.legs.dodge
            self.total_soak += self.legs.soak
            item.is_worn = True
        elif item.type == "body":
            self.deequip("body")
            self.body = item
            self.total_dodge += self.body.dodge
            self.total_soak += self.body.soak
            item.is_worn = True
        elif item.type == "ring":
            if ring == 0:
                if item.is_worn and item == self.ring_2:
                    self.deequip("ring_2")
                self.deequip("ring_1")
                self.ring_1 = item
                self.modify_stat(item.stat, item.increase)
                item.is_worn = True
            else:
                if item.is_worn and item == self.ring_1:
                    self.deequip("ring_1")
                self.deequip("ring_2")
                self.ring_2 = item
                self.modify_stat(item.stat, item.increase)
                item.is_worn = True
        elif item.type == "amulet":
            self.deequip("amulet")
            self.amulet = item
            self.modify_stat(item.stat, item.increase)
            item.is_worn = True

    def deequip(self, type):
        if type == "weapon":
            if self.weapon is not None:
                self.total_damage -= self.weapon.damage
                self.total_hit_modifier -= self.weapon.hit_modifier
                self.weapon.is_worn = False
                self.weapon = None
        elif type == "cape":
            if self.cape is not None:
                self.modify_stat(self.cape.stat, -self.cape.increase)
                self.cape.is_worn = False
                self.cape = None
        elif type == "head":
            if self.head is not None:
                self.total_dodge -= self.head.dodge
                self.total_soak -= self.head.soak
                self.head.is_worn = False
                self.head = None
        elif type == "legs":
            if self.legs is not None:
                self.total_dodge -= self.legs.dodge
                self.total_soak -= self.legs.soak
                self.legs.is_worn = False
                self.legs = None
        elif type == "amulet":
            if self.amulet is not None:
                self.modify_stat(self.amulet.stat, -self.amulet.increase)
                self.amulet.is_worn = False
                self.amulet = None
        elif type == "body":
            if self.body is not None:
                self.total_dodge -= self.body.dodge
                self.total_soak -= self.body.soak
                self.body.is_worn = False
                self.body = None
        elif type == "ring_1":
            if self.ring_1 is not None:
                self.modify_stat(self.ring_1.stat, -self.ring_1.increase)
                self.ring_1.is_worn = False
                self.ring_1 = None
        elif type == "ring_2":
            if self.ring_2 is not None:
                self.modify_stat(self.ring_2.stat, -self.ring_2.increase)
                self.ring_2.is_worn = False
                self.ring_2 = None

    def is_alive(self):
        if self.current_hp > 0:
            return True
        else:
            return False

    def die(self):
        import main, random
        if self == main.player:
            screen.death_screen()
        else:
            main.tower_points += random.randint(1, 100)
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
        if self.current_mp > self.max_mp:
            self.current_mp = self.max_mp

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
            case "dexterity":
                self.dexterity += amount
            case "intelligence":
                self.intelligence += amount
            case "luck":
                self.luck += amount
            case "curse":
                self.curse += amount
            case "hp_regen":
                self.hp_regen += amount
            case "mp_regen":
                self.mp_regen += amount
            case "damage":
                self.total_damage += amount
            case "hit_modifier":
                self.total_hit_modifier += amount
            case "dodge":
                self.total_dodge += amount
            case "soak":
                self.total_soak += amount
            case "max_hp":
                self.max_hp += amount
            case "max_mp":
                self.max_mp += amount


class Player(Actors):
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse)
        self.known_spells = []
        self.player_level = 1

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
            if main.terrain_map[self.y][self.x].char == "<":
                screen.update_chat(f"There are {main.terrain_map[self.y][self.x].name}. Press 'l' to go up.")
            elif main.terrain_map[self.y][self.x].char == ">":
                screen.update_chat(f"There are {main.terrain_map[self.y][self.x].name}. Press 'l' to go down.")
            if main.terrain_map[self.y][self.x].items is not None and bool(main.terrain_map[self.y][self.x].items):
                screen.update_chat("There are items on this tile. Press ',' to look them up")
        elif main.terrain_map[self.y + y][self.x + x].name == "Gate to the Tower of God":
            if main.tower_key > 0:
                main.tower_key -= 1
                main.terrain_map[self.y + y][self.x + x].passable = True
                main.terrain_map[self.y + y][self.x + x].char = 'o'
                screen.update_chat("You opened the gate.")
            else:
                screen.update_chat("You don't have a key. Complete other towers first.")
        elif main.terrain_map[self.y + y][self.x + x].passable is False:
            if main.terrain_map[self.y + y][self.x + x].name == "Door":
                main.terrain_map[self.y + y][self.x + x].passable = True
                main.terrain_map[self.y + y][self.x + x].char = 'o'
                screen.update_chat("You opened the door.")
            else:
                screen.update_chat(f"You tried to walk into the {main.terrain_map[self.y + y][self.x + x].name}.")

        elif main.terrain_map[self.y + y][self.x + x].actor is not None:
            melee_attack(self, main.terrain_map[self.y + y][self.x + x].actor)

    def pick_item(self, id):
        import main
        if main.terrain_map[self.y][self.x].items is not None:
            item = main.terrain_map[self.y][self.x].items[id]
            self.backpack.append(item)
            main.terrain_map[self.y][self.x].items.remove(item)


class Hostile(Actors):
    def __init__(self, y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed=1.0):
        super().__init__(y, x, char, name, max_hp, max_mp, strength, dexterity, intelligence, luck, curse, speed)

    def move(self, y, x):
        import main
        if x == 0 and y == 0:
            pass
        elif main.terrain_map[self.y + y][self.x + x].name == "Door" and main.terrain_map[self.y + y][
            self.x + x].passable is False:
            main.terrain_map[self.y + y][self.x + x].passable = True
            main.terrain_map[self.y + y][self.x + x].char = 'o'
        elif main.terrain_map[self.y + y][self.x + x].passable and main.terrain_map[self.y + y][
            self.x + x].actor is None:
            main.terrain_map[self.y][self.x].actor = None
            self.y += y
            self.x += x
            main.terrain_map[self.y][self.x].actor = self
            screen.update_terrain()
        elif main.terrain_map[self.y + y][self.x + x].actor is not None and main.terrain_map[self.y + y][
            self.x + x].actor == main.player:
            melee_attack(self, main.terrain_map[self.y + y][self.x + x].actor)


class HumanWithPlateArmorAndWarhammer(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Armed Human', 10, 10, 5, 5, 5, 5, 0, 0.8)
        self.equip(item.Warhammer())
        self.equip(item.PlateArmor())


class HumanWithLeatherArmorAndLongsword(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'H', 'Fast Human', 10, 10, 5, 5, 5, 5, 0, 1.0)
        self.equip(item.LongSword())
        self.equip(item.LeatherArmor())


class Dog(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'd', 'Dog', 5, 0, 1, 2, 2, 3, 1, 1.5)
        self.equip(item.Claws())
        self.equip(item.Hide())


class GreenJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Green Jelly', 9, 0, 2, 2, 3, 5, 1)
        self.equip(item.Tentacle())
        self.equip(item.Jelly_Body())


class BlueJelly(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'j', 'Blue Jelly', 18, 0, 3, 5, 3, 5, 1)
        self.equip(item.Tentacle())
        self.equip(item.Jelly_Body())


class Oni(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'O', 'oni', 60, 0, 15, 3, 2, 5, 3)
        self.equip(item.Warhammer())
        self.equip(item.Hide())


class TowerMaster1(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'T', 'Aspiring Master', 50, 0, 15, 20, 20, 10, 15)
        self.equip(item.Dagger())
        self.equip(item.Hide())


class TowerMaster2(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'T', 'Trial Master', 100, 0, 25, 45, 30, 15, 15)
        self.equip(item.LongSword())
        self.equip(item.MailArmor())


class TowerMaster3(Hostile):
    def __init__(self, y, x):
        super().__init__(y, x, 'T', 'Tower Master', 150, 0, 35, 45, 30, 15, 15)
        self.equip(item.Warhammer())
        self.equip(item.PlateArmor())
