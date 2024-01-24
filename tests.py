import unittest
import actors
import item
import terrain


class TestCombat(unittest.TestCase):
    # def test_many_fights(self):
    #     players = [actors.HumanWithLeatherArmorAndLongsword(-1, -1), actors.HumanWithPlateArmorAndWarhammer(-1, -1),
    #                actors.TowerMaster(-1, -1)]
    #     enemies = [actors.Dog(-1, -1), actors.HumanWithLeatherArmorAndLongsword(-1, -1),
    #                actors.HumanWithPlateArmorAndWarhammer(-1, -1), actors.GreenJelly(-1, -1), actors.BlueJelly(-1, -1),
    #                actors.Oni(-1, -1), actors.TowerMaster(-1, -1)]
    #     for first in players:
    #         for second in enemies:
    #             first_wins = 0
    #             second_wins = 0
    #             for round in range(0, 10000):
    #                 first.current_hp = first.max_hp
    #                 second.current_hp = second.max_hp
    #                 while first.is_alive() and second.is_alive():
    #                     actors.melee_attack(first, second)
    #                     if second.is_alive():
    #                         actors.melee_attack(second, first)
    #                         if first.is_alive() is False:
    #                             second_wins += 1
    #                     else:
    #                         first_wins += 1
    #             print(f"{first.name} wins: {first_wins}, {second.name} wins: {second_wins}")
    #
    def test_terrain_gen(self):
        map1 = terrain.generate_terrain(50, 50, "1")
        for i in range(0, 49):
            for j in range(0, 49):
                print(map1[i][j].char, end=" ")
            print()
    #
    # def test_continuous_fight(self):
    #     first = actors.HumanWithPlateArmorAndWarhammer(-1, -1)
    #     second = actors.Dog(-1, -2)
    #     first_wins = 0
    #     while first.is_alive():
    #         actors.melee_attack(first, second, 1)
    #         if second.is_alive():
    #             actors.melee_attack(second, first, 1)
    #         else:
    #             first_wins += 1
    #             second.heal(9999)
    #     print(f"plate armor warhammer human dies from dog after {first_wins} won fights")
    #
    # def test_is_dead(self):
    #     human = actors.Human(-1, -1)
    #     human.deal_damage(9999)
    #     self.assertFalse(human.is_alive())
    #
    # def test_is_healed_to_full_hp(self):
    #     human = actors.Human(-1, -1)
    #     human.current_hp = 1
    #     human.heal(9999)
    #     self.assertEqual(human.current_hp, human.max_hp)


if __name__ == '__main__':
    unittest.main()
