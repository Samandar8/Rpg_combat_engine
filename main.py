from engine.entities import Tank, Archer, MonsterBoss
from engine.actions import MeleeAttack, PowerStrike, HealSpell
from engine.battle import BattleManager
from engine.utils import DataLoader

import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("--- ⚔️ Welcome to the Core Combat Engine ⚔️ ---")
    player = Tank(name="Arthur", hp=100, attack_power=15, mana=30)
    player.skills = [
        MeleeAttack(),
        PowerStrike(mana_cost=20)
    ]
    boss = MonsterBoss(name="Ragnaros", hp=50, attack_power=10, mana=50)
    battle = BattleManager(player, boss)

    try:
        winner = battle.start_fight()
        print(f"\n🏆 Winner: {winner.name}!")

        if winner == player:
            player.gain_experience(150)

    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
