import input_handler


class Spell:
    def __init__(self, name, school, cost):
        self.name = name
        self.cost = cost
        self.school = school


class Holy(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "holy", cost)


class Heal(Holy):
    def __init__(self):
        super().__init__("Heal", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            screen.update_chat("You cast heal. It heals you for 10.")
            caster.heal(10)
            return True
        return False

class Smite(Holy):
    def __init__(self):
        super().__init__("Smite", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            if target is not None:
                if target.current_hp < target.max_hp / 2:
                    target.deal_damage(5 * 2)
                    screen.update_chat("You cast smite. It deals 10 damage.")
                else:
                    target.deal_damage(5)
                    screen.update_chat("You cast smite. It deals 5 damage.")
                return True
            else:
                caster.restore_mp(self.cost)
        return False


class HolyIntervention(Holy):
    def __init__(self):
        super().__init__("Holy Intervention", 10)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            pass
            # if someone would die in next few turns he get healed and get small boost for a while


class Death(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "death", cost)


class DrainLife(Death):
    def __init__(self):
        super().__init__("Drain Life", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            target.deal_damage(6)
            caster.heal(6)
            screen.update_chat("You cast drain life. It deals 6 damage and heal you for 6.")
            return True
        return False

class Blindness(Death):
    def __init__(self):
        super().__init__("Blindness", 8)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            # tutaj jeszcze zrobic aby target miał debuff do celności
            screen.update_chat("You cast Blindness.")
            return True
        return False

class RaiseDead(Death):
    def __init__(self):
        super().__init__("Raise Dead", 12)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            # target = input_handler.targetting(caster)
            # tutaj wybieranie miejsca do przyzwania zombie
            screen.update_chat("You cast Raise Dead.")
            return True
        return False

class Fire(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "fire", cost)


class Spark(Fire):

    def __init__(self):
        super().__init__("Spark", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            target.deal_damage(5)
            screen.update_chat("You cast Spark. It deals 5 damage.")
            return True
        return False

class Pyroblast(Fire):
    def __init__(self):
        super().__init__("Pyroblast", 15)
        self.damage = 9

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            targets = input_handler.targetting(caster, "aoe")
            screen.update_chat(f"You cast {self.name}. It deals {self.damage} damage to {len(targets)}.")
            for target in targets:
                target.deal_damage(self.damage)
            return True
        return False

class FlameWall(Fire):
    pass


class Nature(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "nature", cost)


class CreateMud(Nature):
    pass


class RaiseTerrain(Nature):
    pass


class Shatter(Nature):
    pass


class Poison(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "poison", cost)


class Infect(Poison):
    pass


class AccelerateCirculation(Poison):
    pass


class Contagion(Poison):
    pass


class Battle(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "battle", cost)


class Heroism(Battle):
    def __init__(self):
        super().__init__("Heroism", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            caster.modify_stat("strength", 5)
            screen.update_chat("You cast heroism. You feel stronger.")
            temp_effect = [5, self]
            caster.temp_effects.append(temp_effect)
            return True
        return False
    def end_effect(self, target):
        target.modify_stat("strength", -5)




class BladeStorm(Battle):
    pass


class Bloodlust(Battle):
    pass


class Transformation(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "transformation", cost)


class BladeHands(Transformation):
    pass


class NativeForm(Transformation):
    pass


class TitanForm(Transformation):
    pass
