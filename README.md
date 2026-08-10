# Python RPG Combat Engine

A small turn-based combat engine built to practise modular Python and object-oriented design.

## What it demonstrates

- Abstract base classes for entities, actions, and effects
- Inheritance and composition for heroes, monsters, skills, and inventory
- Encapsulated HP state with safe value bounds
- Strategy-like action objects for melee attacks, power strikes, and healing
- Character progression and a boss enrage mechanic
- Automated tests for combat rules and entity state

## Project structure

```text
engine/
  actions.py    # Combat actions
  base.py       # Core abstractions and inventory
  battle.py     # Turn orchestration
  effects.py    # Timed combat effects
  entities.py   # Heroes, monsters, and progression
  utils.py      # Battle logging
main.py         # Example game entry point
test_engine.py  # Unit tests for core rules
tests_battle.py # Battle-flow test
```

## Run locally

Python 3.10 or newer is recommended. The project uses only the Python standard library.

```bash
git clone https://github.com/Samandar8/Rpg_combat_engine.git
cd Rpg_combat_engine
python main.py
```

## Run tests

```bash
python -m unittest discover -v
```

The test suite checks HP bounds, inventory behaviour, mana use, healing, level progression, boss enrage, and the battle turn flow.

## Status

This is a portfolio and learning project. Planned improvements include non-interactive battle policies, richer effects, and stronger separation between game logic and console output.
