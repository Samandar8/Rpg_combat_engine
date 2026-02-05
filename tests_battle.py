
import sys
import unittest
from unittest import mock
from io import StringIO
from engine.entities import Tank, MonsterBoss
from engine.battle import BattleManager
from engine.actions import MeleeAttack


sys.stdout.reconfigure(encoding='utf-8')

class TestBattle(unittest.TestCase):
    def test_battle_flow(self):
        player = Tank("Hero", 200, 20, 10)
        player.skills = [MeleeAttack()] 
        boss = MonsterBoss("Boss", 50, 5, 0)
        
        with unittest.mock.patch('builtins.input', return_value='1'):
            battle = BattleManager(player, boss)
            
            print("\n--- Testing Player Turn ---")
            battle.player_turn()
            self.assertLess(boss.hp, 250, "Boss should take damage from player")
            
            print("\n--- Testing Enemy Turn ---")
            initial_player_hp = player.hp
            battle.enemy_turn()
            self.assertLess(player.hp, initial_player_hp, "Player should take damage from boss")
            
            
            damage_taken = initial_player_hp - player.hp
            print(f"Debug: Player took {damage_taken} damage")
            
            self.assertLess(damage_taken, 10, "Boss should only attack once per turn!")

if __name__ == '__main__':
    unittest.main()
