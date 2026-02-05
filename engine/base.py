from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, hp: int, attack_power: int, mana: int, level: int = 1):
        self.name = name
        self.max_hp = hp
        self._hp = hp
        self.attack_power = attack_power
        self.mana = mana
        self.level = level

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))

    @property
    def is_alive(self) -> bool:
        return self._hp > 0

    @abstractmethod
    def make_turn(self, target):
        pass

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"🩸 {self.name} takes {amount} damage. HP: {self.hp}/{self.max_hp}")

    def level_up_base(self, hp_gain, attack_gain):
        self.level += 1
        self.max_hp += hp_gain
        self.hp = self.max_hp
        self.attack_power += attack_gain
        print(f"⬆️ {self.name} reached {self.level} level!")


class Action(ABC):
    @abstractmethod
    def execute(self, source, target):
        pass

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        print(f"[Inventory] Item '{item.name}' added.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print(f"[Inventory] Item '{item.name}' removed.")
        else:
            print(f"[Inventory] Error: Item '{item.name}' not in inventory.")

    def __len__(self):
        return len(self._items)

    def __str__(self):
        if not self._items:
            return "Empty Inventory."
        names = [item.name for item in self._items]
        return "Inventory: " + ", ".join(names)

    @property
    def items(self):
        return self._items[:]