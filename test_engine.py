import unittest
from unittest.mock import patch

from engine.actions import HealSpell, MeleeAttack, PowerStrike
from engine.base import Inventory
from engine.entities import Hero, Monster, MonsterBoss, Tank


class Item:
    def __init__(self, name):
        self.name = name


class TestEntityState(unittest.TestCase):
    def test_hp_is_clamped_to_valid_range(self):
        hero = Tank("Guardian", 100, 10, 20)

        hero.hp = hero.max_hp + 50
        self.assertEqual(hero.hp, hero.max_hp)

        hero.hp = -1
        self.assertEqual(hero.hp, 0)
        self.assertFalse(hero.is_alive)

    def test_experience_levels_up_hero(self):
        hero = Hero("Ranger", 100, 10, 20, "Archer")

        with patch("builtins.print"):
            hero.gain_experience(100)

        self.assertEqual(hero.level, 2)
        self.assertEqual(hero.exp, 0)
        self.assertEqual(hero.max_hp, 120)
        self.assertEqual(hero.attack_power, 15)

    def test_boss_enrages_once_below_threshold(self):
        boss = MonsterBoss("Boss", 100, 10, 0)
        original_attack = boss.attack_power

        with patch("builtins.print"):
            boss.take_damage(360)
            enraged_attack = boss.attack_power
            boss.take_damage(10)

        self.assertTrue(boss.is_enraged)
        self.assertEqual(enraged_attack, original_attack * 1.5)
        self.assertEqual(boss.attack_power, enraged_attack)


class TestActions(unittest.TestCase):
    def test_melee_attack_uses_patched_damage_roll(self):
        attacker = Monster("Goblin", 50, 10, 0)
        target = Monster("Target", 50, 5, 0)

        with patch("engine.actions.random.uniform", return_value=1.0), patch("builtins.print"):
            MeleeAttack().execute(attacker, target)

        self.assertEqual(target.hp, 40)

    def test_power_strike_spends_mana_and_deals_damage(self):
        attacker = Hero("Knight", 100, 20, 30, "Fighter")
        target = Monster("Ogre", 100, 5, 0)

        with patch("builtins.print"):
            PowerStrike(mana_cost=20).execute(attacker, target)

        self.assertEqual(attacker.mana, 10)
        self.assertEqual(target.hp, 50)

    def test_heal_respects_max_hp(self):
        caster = Hero("Cleric", 100, 10, 30, "Support")
        caster.hp = 95

        with patch("builtins.print"):
            HealSpell(mana_cost=15).execute(caster, caster)

        self.assertEqual(caster.hp, caster.max_hp)
        self.assertEqual(caster.mana, 15)


class TestInventory(unittest.TestCase):
    def test_items_are_added_removed_and_copied_safely(self):
        inventory = Inventory()
        potion = Item("Potion")

        with patch("builtins.print"):
            inventory.add_item(potion)

        snapshot = inventory.items
        snapshot.clear()
        self.assertEqual(len(inventory), 1)

        with patch("builtins.print"):
            inventory.remove_item(potion)

        self.assertEqual(len(inventory), 0)


if __name__ == "__main__":
    unittest.main()
