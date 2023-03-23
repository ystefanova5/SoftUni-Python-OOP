from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def test_01_class_initializes_with_valid_data(self):
        hero = Hero("Player1", 10, 100, 20)

        self.assertEqual("Player1", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(20, hero.damage)

    def test_02_battle_enemy_with_same_username_raises(self):
        hero = Hero("Player1", 10, 100, 20)
        enemy_hero = Hero("Player1", 15, 150, 30)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        expected_message = "You cannot fight yourself"
        self.assertEqual(expected_message, str(ex.exception))

    def test_03_battle_hero_with_zero_or_negative_health_raises(self):
        hero = Hero("Player1", 10, 100, 20)
        enemy_hero = Hero("Player2", 15, 150, 30)
        hero.health = 0
        self.assertEqual(0, hero.health)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        expected_message = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected_message, str(ex.exception))

        hero.health = -5
        self.assertEqual(-5, hero.health)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        self.assertEqual(expected_message, str(ex.exception))

    def test_04_battle_enemy_with_zero_or_negative_health_raises(self):
        hero = Hero("Player1", 10, 100, 20)
        enemy_hero = Hero("Player2", 15, 150, 30)
        enemy_hero.health = 0
        self.assertEqual(0, enemy_hero.health)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        expected_message = "You cannot fight Player2. He needs to rest"
        self.assertEqual(expected_message, str(ex.exception))

        enemy_hero.health = -5
        self.assertEqual(-5, enemy_hero.health)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)

        self.assertEqual(expected_message, str(ex.exception))

    def test_05_battle_draw_reduces_health_correctly(self):
        hero = Hero("Player1", 5, 100, 20)
        enemy_hero = Hero("Player2", 5, 100, 20)
        hero.battle(enemy_hero)

        self.assertEqual(0, hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_06_draw_returns_correct_message(self):
        hero = Hero("Player1", 6, 100, 30)
        enemy_hero = Hero("Player2", 5, 100, 30)

        result = hero.battle(enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, hero.health)
        self.assertEqual(-80, enemy_hero.health)

    def test_07_after_battle_hero_and_enemy_attributes_when_enemy_health_zero_or_negative(self):
        hero = Hero("Player1", 6, 180, 30)
        enemy_hero = Hero("Player2", 5, 100, 20)

        hero.battle(enemy_hero)

        # test hero attributes:
        self.assertEqual(7, hero.level)
        self.assertEqual(85, hero.health)
        self.assertEqual(35, hero.damage)

        # test enemy_hero attributes:
        self.assertEqual(5, enemy_hero.level)
        self.assertEqual(-80, enemy_hero.health)
        self.assertEqual(20, enemy_hero.damage)

    def test_08_after_battle_message_when_enemy_health_zero_or_negative(self):
        hero = Hero("Player1", 6, 180, 30)
        enemy_hero = Hero("Player2", 5, 100, 20)

        result = hero.battle(enemy_hero)

        self.assertEqual("You win", result)

    def test_09_after_battle_hero_and_enemy_attributes_when_enemy_health_not_zero_or_negative(self):
        hero = Hero("Player1", 3, 90, 10)
        enemy_hero = Hero("Player2", 5, 100, 10)

        hero.battle(enemy_hero)

        # test hero attributes:
        self.assertEqual(3, hero.level)
        self.assertEqual(40, hero.health)
        self.assertEqual(10, hero.damage)

        # test enemy_hero attributes:
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(75, enemy_hero.health)
        self.assertEqual(15, enemy_hero.damage)

    def test_10_after_battle_message_when_hero_health_zero_or_negative(self):
        hero = Hero("Player1", 3, 90, 10)
        enemy_hero = Hero("Player2", 5, 100, 10)

        result = hero.battle(enemy_hero)

        self.assertEqual("You lose", result)

    def test_11_str_method_returns_correct_message(self):
        hero = Hero("Player1", 3, 90, 10)

        expected_message = "Hero Player1: 3 lvl\n" \
                           f"Health: 90\n" \
                           f"Damage: 10\n"
        actual_message = str(hero)
        self.assertEqual(expected_message, actual_message)


if __name__ == "__main__":
    main()
