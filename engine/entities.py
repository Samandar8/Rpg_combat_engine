from engine.base import Entity, Inventory

class Hero(Entity):
    def __init__(self, name, hp, attack_power, mana, role_name):
        super().__init__(name, hp, attack_power, mana)
        self.role_name = role_name
        self.inventory = Inventory()
        self.exp = 0

    def gain_experience(self, amount):
        self.exp += amount
        print(f"✨ {self.name} gained {amount} exp.")
        if self.exp >= 100:
            self.exp -= 100
            self.level_up_base(hp_gain=20, attack_gain=5)

    def make_turn(self, target):
        print(f"⚔️ {self.name} ({self.role_name}) plans an attack.")


class Monster(Entity):
    def make_turn(self, target):
        print(f"👹 {self.name} {self.level} level attacks!")
        from engine.actions import MeleeAttack
        MeleeAttack().execute(self, target)

    def evolve(self):
        self.level_up_base(hp_gain=50, attack_gain=10)
        print(f"🧬 {self.name} evolved!")

    def __str__(self):
        return f"👹 {self.name} (HP: {self.hp}/{self.max_hp})"


class Tank(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp * 2, attack_power * 0.7, mana, "Tank")


class Archer(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp * 0.8, attack_power * 1.5, mana, "Archer")


class MonsterBoss(Monster):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp * 5, attack_power * 1.2, mana)
        self.is_enraged = False

    def take_damage(self, amount):
        super().take_damage(amount)

        if self.hp > 0 and self.hp <= (self.max_hp * 0.3) and not self.is_enraged:
            self.enter_enrage_mode()

    def enter_enrage_mode(self):
        self.is_enraged = True
        self.attack_power *= 1.5
        print(f"🔥 ATTENTION: {self.name} Enraged! Damage increased!")

    def make_turn(self, target):
        if self.is_enraged:
            print(f"💥 {self.name} deals a crushing blow to {target.name}!")
            from engine.actions import MeleeAttack
            MeleeAttack().execute(self, target)
        else:
            super().make_turn(target)


