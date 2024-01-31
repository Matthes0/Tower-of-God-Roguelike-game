import unittest

import terrain


class TestCombat(unittest.TestCase):
    def test_terrain_gen(self):
        map1 = terrain.generate_terrain(50, 50, "1")
        for i in range(0, 49):
            for j in range(0, 49):
                print(map1[i][j].char, end=" ")
            print()


if __name__ == '__main__':
    unittest.main()
