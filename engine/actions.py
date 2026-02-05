from abc import ABC, abstractmethod
import random


class Action(ABC):
    @abstractmethod
    def execute(self, source, target):
        """
        source: who performs action (Entity)
        target: target to receive action (Entity)
        """
        pass


class MeleeAttack(Action):
    def execute(self, source, target):
        damage = source.attack_power * (1 + (source.level - 1) * 0.1)

        damage = int(damage * random.uniform(0.85, 1.15))

        print(f"⚔️ {source.name} attacks {target.name}!")
        target.take_damage(damage)


class PowerStrike(Action):
    def __init__(self, mana_cost=20):
        self.mana_cost = mana_cost

    def execute(self, source, target):
        if source.mana >= self.mana_cost:
            source.mana -= self.mana_cost
            damage = int(source.attack_power * 2.5)
            print(f"💥 {source.name} uses POWER STRIKE!")
            target.take_damage(damage)
        else:
            print(f"❌ {source.name} not enough mana!")


class HealSpell(Action):
    def __init__(self, mana_cost=15):
        self.mana_cost = mana_cost

    def execute(self, source, target):
        if source.mana >= self.mana_cost:
            source.mana -= self.mana_cost
            heal_amount = 20 * source.level
            target.hp += heal_amount
            print(f"✨ {source.name} heals {target.name} for {heal_amount} HP!")
        else:
            print(f"❌ {source.name} cannot cast spell!")
