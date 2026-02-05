from abc import ABC, abstractmethod

class Effect(ABC):
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def apply(self, target):
        pass

    def tick(self):
        self.duration -= 1

class PoisonEffect(Effect):
    def __init__(self, damage_per_turn=5, duration=3):
        super().__init__("Poison", duration)
        self.damage_per_turn = damage_per_turn

    def apply(self, target):
        target.hp -= self.damage_per_turn
        print(f"🤢 Poisoning {target.name} {self.damage_per_turn} damage! (Remaining moves: {self.duration})")

class ShieldEffect(Effect):
    def __init__(self, duration=2):
        super().__init__("Shield", duration)

    def apply(self, target):
        print(f"🛡️ Shield {target.name}! (Remaining moves: {self.duration})")
