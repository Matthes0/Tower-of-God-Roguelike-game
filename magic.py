import input_handler


class Spell:
    def __init__(self, name, school):
        self.name = name
        self.school = school


class Poison(Spell):
    def __init__(self, name):
        super().__init__(name, "poison")
        self.name = name


class Holy(Spell):
    def __init__(self, name, cost):
        super().__init__(name, "holy")
        self.name = name
        self.cost = cost


class Heal(Holy):
    def __init__(self):
        super().__init__("Heal", 5)

    def cast(self, caster, target):
        import screen
        if caster.can_cast(self.cost) is True:
            target.heal(10)
            screen.update_chat("You cast heal. It heals you for 10.")


class Smite(Holy):
    def __init__(self):
        super().__init__("Smite", 5)

    def cast(self, caster):
        import screen
        if caster.can_cast(self.cost) is True:
            target = input_handler.targetting(caster)
            target.deal_damage(10)
            screen.update_chat("You cast smite. It deals 10 damage.")
        else:
            screen.update_chat("Not enough mana.")

class Battle(Spell):
    def __init__(self, name):
        super().__init__(name, "battle")
        self.name = name


class Nature(Spell):
    def __init__(self, name):
        super().__init__(name, "nature")
        self.name = name


class Fire(Spell):
    def __init__(self, name):
        super().__init__(name, "fire")
        self.name = name


class Death(Spell):
    def __init__(self, name):
        super().__init__(name, "death")
        self.name = name
