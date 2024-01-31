import input_handler
import screen


class Spell:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Heal(Spell):
    def __init__(self):
        super().__init__("Heal", 10)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            screen.update_chat(f"You cast heal. It heals you for {caster.intelligence * 2}.")
            caster.heal(caster.intelligence * 2)
            return True
        return False

class Smite(Spell):
    def __init__(self):
        super().__init__("Smite", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            if target is not None:
                target.deal_damage(caster.intelligence)
                screen.update_chat(f"You cast smite. It deals {caster.intelligence} damage.")
                return True
        return False


class DrainLife(Spell):
    def __init__(self):
        super().__init__("Drain Life", 15)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            target.deal_damage(caster.intelligence)
            caster.heal(int(caster.intelligence/2))
            screen.update_chat(f"You cast drain life. It deals {caster.intelligence} damage and heal you for {int(caster.intelligence/2)}.")
            return True
        return False



class Shoot(Spell):

    def __init__(self):
        super().__init__("Shoot", 2)
    def cast(self, caster):
        if caster.weapon.name == "Longbow":
            if caster.can_cast(self.cost) is True:
                target = input_handler.targetting(caster)
                target.melee_attack(caster,target)
                return True
            return False
        screen.update_chat("Equip ranged weapon first.")
        return False

class ThrowCrystal(Spell):
    def __init__(self):
        super().__init__("Throw Crystal", 25)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            targets = input_handler.targetting(caster, "aoe")
            screen.update_chat(f"You {self.name}. It deals {caster.intelligence * 2} damage to {len(targets)} targets.")
            for target in targets:
                target.deal_damage(caster.intelligence * 2)
            return True
        return False



class Shatter(Spell):
    def __init__(self):
        super().__init__("Shatter", 15)
    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target_y_x = input_handler.targetting(caster, "wall")
            import main, terrain
            main.terrain_map[target_y_x[0]][target_y_x[1]] = terrain.Floor()
            screen.update_chat("You destroyed a wall.")
            return True
        return False

class Heroism(Spell):
    def __init__(self):
        super().__init__("Heroism", 10)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            caster.modify_stat("strength", 10)
            screen.update_chat("You cast heroism. You feel stronger for a while.")
            temp_effect = [5, self]
            caster.temp_effects.append(temp_effect)
            return True
        return False
    def end_effect(self, target):
        target.modify_stat("strength", -10)
