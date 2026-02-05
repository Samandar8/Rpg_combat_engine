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
- **Type Hinting** (For clean and maintainable code)

## 🎯 Getting Started
To run the combat simulation:
```bash
python main.py