import json
import os

class BattleLogger:
    """Static class for pretty console output"""
    @staticmethod
    def log(message):
        print(f"[LOG]: {message}")

    @staticmethod
    def log_battle_status(p1, p2):
        print("-" * 30)
        print(f"{p1.name}: {p1.hp}/{p1.max_hp} HP")
        print(f"{p2.name}: {p2.hp}/{p2.max_hp} HP")
        print("-" * 30)

class DataLoader:
    """Class for working with external files"""
    @staticmethod
    def load_units(file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_game_result(winner_name, rounds):
        with open("battle_history.txt", "a", encoding='utf-8') as f:
            f.write(f"Winner: {winner_name}, Rounds: {rounds}\n")
