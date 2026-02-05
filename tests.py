from engine.entities import Tank, Monster
from engine.actions import MeleeAttack

import sys
sys.stdout.reconfigure(encoding='utf-8')


def test_combat():
    print("🧪 Running Test: Combat Logic...")

    hero = Tank("Test Knight", 100, 10, 0)
    enemy = Monster("Test Goblin", 30, 5, 0)
    attack = MeleeAttack()
    initial_hp = enemy.hp
    attack.execute(hero, enemy)
    if enemy.hp < initial_hp:
        print("✅ Success: Enemy HP decreased after attack.")
    else:
        print("❌ Failure: Enemy HP did not change.")


def test_level_up():
    print("\n🧪 Running Test: Level Up...")
    hero = Tank("Leveler", 100, 10, 0)
    hero.gain_experience(150)

    if hero.level == 2:
        print("✅ Success: Hero reached level 2.")
    else:
        print("❌ Failure: Level did not increase.")


if __name__ == "__main__":
    print("=== STARTING MANUAL TESTS ===\n")
    try:
        test_combat()
        test_level_up()
        print("\n=== ALL TESTS FINISHED ===")
    except Exception as e:
        print(f"\n⚠️ CRITICAL ERROR DURING TESTING: {e}")
