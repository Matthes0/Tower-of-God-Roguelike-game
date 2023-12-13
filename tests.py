import unittest
import actors
import item


class TestCombat(unittest.TestCase):
    def test_many_fights(self):
        players = [actors.Human_with_leather_armor_and_longsword(-1, -1), actors.Human_with_plate_armor_and_warhammer(-1, -1), actors.Tower_Master(-1, -1)]
        enemies = [actors.Dog(-1,-1), actors.Human_with_leather_armor_and_longsword(-1, -1), actors.Human_with_plate_armor_and_warhammer(-1, -1), actors.Green_Jelly(-1, -1), actors.Blue_Jelly(-1, -1), actors.Oni(-1, -1), actors.Tower_Master(-1, -1)]
        for first in players:
            for second in enemies:
                first_wins = 0
                second_wins = 0
                for round in range(0, 10000):
                    first.current_hp = first.max_hp
                    second.current_hp = second.max_hp
                    while first.is_alive() and second.is_alive():
                        actors.melee_attack(first, second)
                        if second.is_alive():
                            actors.melee_attack(second, first)
                            if first.is_alive() is False:
                                second_wins += 1
                        else:
                            first_wins += 1
                print(f"{first.name} wins: {first_wins}, {second.name} wins: {second_wins}")
    # def test_many_fights(self):
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.PlateArmor())
    #     first.equip_weapon(item.Warhammer())
    #     second = actors.Dog(-1, -2)
    #     second.equip_armor(item.Hide())
    #     second.equip_weapon(item.Claws())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"plate armor warhammer human wins: {first_wins}, dog wins: {second_wins}")
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.PlateArmor())
    #     first.equip_weapon(item.Warhammer())
    #     second = actors.Human(-1, -2)
    #     second.equip_armor(item.LeatherArmor())
    #     second.equip_weapon(item.LongSword())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"plate armor warhammer human wins: {first_wins}, leather armor long sword human wins: {second_wins}")
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.LeatherArmor())
    #     first.equip_weapon(item.LongSword())
    #     second = actors.Dog(-1, -2)
    #     second.equip_armor(item.Hide())
    #     second.equip_weapon(item.Claws())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"leather armor long sword human wins: {first_wins}, dog wins: {second_wins}")
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.LeatherArmor())
    #     first.equip_weapon(item.LongSword())
    #     second = actors.Oni(-1, -2)
    #     second.equip_armor(item.Hide())
    #     second.equip_weapon(item.Warhammer())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"leather armor long sword human wins: {first_wins}, oni wins: {second_wins}")
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.PlateArmor())
    #     first.equip_weapon(item.Warhammer())
    #     second = actors.Oni(-1, -2)
    #     second.equip_armor(item.Hide())
    #     second.equip_weapon(item.Warhammer())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"plate armor warhammer human wins: {first_wins}, oni wins: {second_wins}")
    #     first = actors.Human(-1, -1)
    #     first.equip_armor(item.LeatherArmor())
    #     first.equip_weapon(item.LongSword())
    #     second = actors.Human(-1, -2)
    #     second.equip_armor(item.LeatherArmor())
    #     second.equip_weapon(item.LongSword())
    #     first_wins = 0
    #     second_wins = 0
    #     for round in range(0, 10000):
    #         first.current_hp = first.max_hp
    #         second.current_hp = second.max_hp
    #         while first.is_alive() and second.is_alive():
    #             actors.melee_attack(first, second)
    #             if second.is_alive():
    #                 actors.melee_attack(second, first)
    #                 if first.is_alive() is False:
    #                     second_wins += 1
    #             else:
    #                 first_wins += 1
    #     print(f"leather armor long sword human wins: {first_wins}, leather armor long sword human wins: {second_wins}")

    def test_continuous_fight(self):
        first = actors.Human(-1, -1)
        first.equip_armor(item.PlateArmor())
        first.equip_weapon(item.Warhammer())
        second = actors.Dog(-1, -2)
        second.equip_armor(item.Hide())
        second.equip_weapon(item.Claws())
        first_wins = 0
        while first.is_alive():
            actors.melee_attack(first, second, 1)
            if second.is_alive():
                actors.melee_attack(second, first, 1)
            else:
                first_wins += 1
                second.heal(9999)
        print(f"plate armor warhammer human dies from dog after {first_wins} won fights")

    def test_is_dead(self):
        human = actors.Human(-1, -1)
        human.deal_damage(9999)
        self.assertFalse(human.is_alive())

    def test_is_healed_to_full_hp(self):
        human = actors.Human(-1, -1)
        human.current_hp = 1
        human.heal(9999)
        self.assertEqual(human.current_hp, human.max_hp)


if __name__ == '__main__':
    unittest.main()
