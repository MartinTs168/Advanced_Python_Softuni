import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Shadow", 20, 1000, 100)
        self.enemy = Hero("Bad", 10, 500, 20)

    def test_correct_init(self):
        self.assertEqual("Shadow", self.hero.username)
        self.assertEqual(20, self.hero.level)
        self.assertEqual(1000, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_usernames_are_the_same_raises_exception(self):
        self.enemy.username = "Shadow"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health_raises_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_zero_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Bad. He needs to rest", str(ve.exception))

    def test_battle_with_both_players_down_returns_draw(self):
        self.enemy.health, self.hero.health = 1, 1

        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_with_enemy_dies_returns_hero_win(self):
        self.enemy.health = 1

        self.assertEqual("You win", self.hero.battle(self.enemy))
        self.assertEqual(21, self.hero.level)
        self.assertEqual(805, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_with_enemy_wins_returns_hero_loses(self):
        self.hero.health, self.hero.damage = 1, 1
        self.assertEqual("You lose", self.hero.battle(self.enemy))

        self.assertEqual(11, self.enemy.level)
        self.assertEqual(485, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)

    def test_str_should_return_correct_format(self):
        expected = f"Hero Shadow: 20 lvl\n" \
               f"Health: 1000\n" \
               f"Damage: 100\n"

        self.assertEqual(expected, self.hero.__str__())


if __name__ == '__main__':
    unittest.main()
