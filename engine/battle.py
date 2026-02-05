import os
from engine.utils import BattleLogger


class BattleManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.round = 1

    def start_fight(self):
        BattleLogger.log(f"The battle between {self.player.name} and {self.enemy.name}!")

        while self.player.is_alive and self.enemy.is_alive:
            print(f"\n--- Round {self.round} ---")
            BattleLogger.log_battle_status(self.player, self.enemy)

            self.player_turn()
            if not self.enemy.is_alive:
                print(f"\n💀 {self.enemy.name} defeated!")
                return self.player

            self.enemy_turn()
            if not self.player.is_alive:
                print(f"\n💀 {self.player.name} died in battle...")
                return self.enemy

            self.round += 1

    def player_turn(self):
        print(f"\nPlayer's move {self.player.name}:")
        for i, skill in enumerate(self.player.skills):
            print(f"{i + 1}. {skill.__class__.__name__}")

        while True:
            choice = input("Select an action: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.player.skills):
                selected_skill = self.player.skills[int(choice) - 1]
                selected_skill.execute(self.player, self.enemy)
                break
            else:
                print("Incorrect choice. Try again.")

    def enemy_turn(self):
        print(f"\nEnemy's move {self.enemy.name}:")
        self.enemy.make_turn(self.player)