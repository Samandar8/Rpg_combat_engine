# Core Combat Engine (Python OOP)

A robust and extensible turn-based combat engine built with Python, focusing on Clean Architecture and core Object-Oriented Programming principles.

## 🚀 Key Features
* **Interface-Based Architecture**: Utilizes Abstract Base Classes (`abc.ABC`) to define strict contracts for entities and combat actions.
* **Strategy Design Pattern**: Combat skills are encapsulated into independent classes, allowing dynamic skill assignment to any character.
* **Progression System**: A centralized Level/EXP mechanic inherited by both Heroes and Monsters.
* **Composition & Encapsulation**: Uses properties for safe data access (e.g., HP clamping) and manages inventories/skills as composite objects.
* **State Management**: Features a Boss "Enrage" mechanic and a system for handling turn-based combat states.

## 🏗 Project Structure
* `engine/base.py` – Core abstractions, entity interfaces, and base Level/HP logic.
* `engine/entities.py` – Character hierarchy including Heroes (Tanks, Archers) and Monsters (Bosses).
* `engine/actions.py` – Implementation of combat mechanics (Melee, Magic, Healing).
* `engine/battle.py` – The game loop orchestrator managing turn order and player input.
* `engine/utils.py` – Utility classes for battle logging and data handling.

## 🛠 Technologies
- **Python 3.10+**
- **OOP Principles** (Inheritance, Encapsulation, Polymorphism)
- **ABC Module** (Abstract Base Classes)

## 🎯 Getting Started

### Prerequisites
- Python 3 installed.

### Running the Game
To run the combat simulation:
```bash
python main.py
```

### Running Tests
To verify the engine mechanics and battle logic:
```bash
python tests.py
python tests_battle.py
```

## 🎮 How to Play
1. Launch the game with `python main.py`.
2. You control a **Hero (Tank)**.
3. Choose your action each turn (e.g., Melee Attack or Power Strike).
4. Defeat the **Boss** to win!