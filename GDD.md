# DUNGEON ZERO
## Game Design Document (GDD)
**Version:** 1.0  
**Status:** Pre-Production  
**Genre:** 2D Action RPG / Dungeon Crawler  
**Platform:** Windows PC  
**Language:** Python  
**Framework:** Pygame  
**Perspective:** Top-down with a slight angled view  
**Players:** Single-player

---

# 1. Game Overview

Dungeon Zero is a 2D dark fantasy action RPG where players explore procedurally generated dungeons, fight dangerous creatures, collect equipment, uncover secrets, and descend deeper into a cursed kingdom.

The game focuses on real-time combat, exploration, progression, and replayability.

# 2. Story & Setting

An ancient curse has swallowed an entire kingdom in darkness.

Its cities have fallen silent, its inhabitants have transformed into hostile creatures, and its underground dungeons have become increasingly dangerous.

The player takes control of a customizable hero who ventures into these forgotten places to uncover the source of the curse.

Every dungeon holds new threats, treasures, and secrets.

# 3. Core Gameplay Loop

1. Enter a dungeon.
2. Explore procedurally generated rooms.
3. Fight enemies and avoid traps.
4. Collect weapons, equipment, gold, and resources.
5. Discover checkpoints and special rooms.
6. Defeat the floor boss.
7. Descend deeper into the kingdom.
8. Become stronger and uncover the truth.

# 4. Camera & Visual Direction

- 2D top-down perspective with a slight angled view.
- Dark fantasy pixel-art aesthetic.
- Atmospheric environments with detailed dungeon tiles.
- Smooth character movement and combat animations.
- Visual distinction between dungeon floors and enemy types.

# 5. Player Character

The player controls one customizable hero.

### Initial Attributes
- Health (HP)
- Stamina
- Attack
- Defence
- Movement Speed
- Experience (XP)
- Level

Character customization and equipment should influence the player's appearance and capabilities.

# 6. Controls

| Input | Action |
|---|---|
| WASD | Movement |
| Mouse | Aim |
| Left Click | Basic Attack |
| Space | Dodge / Roll |
| E | Interact |
| Q | Special Ability |
| I | Inventory |
| ESC | Pause Menu |

# 7. Combat System

Combat will happen in real time.

### Combat Features
- Melee and ranged attacks.
- Enemy attack patterns.
- Dodge and stamina mechanics.
- Weapon-specific attack behaviour.
- Special abilities.
- Boss fights with multiple phases.

Combat should reward positioning, timing, and strategy.

# 8. Dungeon Generation

Every dungeon should be procedurally generated.

### Room Types
- Normal Room
- Combat Room
- Treasure Room
- Trap Room
- Shop Room
- Rest Room
- Boss Room

### Generation Requirements
- Randomized room placement.
- Connected corridors.
- Reachable paths between rooms.
- Guaranteed route to the floor exit.
- Seed-based generation for reproducibility.

# 9. Enemies

Initial enemy roster:

| Enemy | Behaviour |
|---|---|
| Slime | Basic melee attacker |
| Skeleton | Standard dungeon enemy |
| Goblin | Fast and aggressive |
| Bat | Flying enemy |
| Dark Mage | Ranged magic attacker |
| Guardian | Heavy and powerful enemy |

Additional enemy types may be introduced as development progresses.

# 10. Weapons & Equipment

### Weapon Categories
- Swords
- Daggers
- Axes
- Bows
- Staffs
- Shields

### Equipment
- Helmets
- Armour
- Boots
- Accessories

### Rarity System
- Common
- Uncommon
- Rare
- Epic
- Legendary

Equipment should have different stats and gameplay effects.

# 11. Progression System

Players gain experience by defeating enemies and completing dungeon challenges.

Progression features:
- XP and leveling.
- Stat improvements.
- Weapon upgrades.
- Equipment collection.
- Unlockable abilities.
- Gold and loot.

# 12. Difficulty & Death System

**Difficulty:** Casual.

The game should be challenging without being excessively punishing.

When the player dies:
- Return to the last checkpoint.
- Retain collected inventory.
- Preserve established progression.
- Allow the player to continue without restarting the entire game.

# 13. Saving System

- Checkpoint-based progression.
- JSON-based save files.
- Save player statistics and inventory.
- Save relevant progression and unlocks.
- Support loading previous progress.

# 14. Audio

The game should eventually include:
- Background dungeon music.
- Combat music.
- Enemy sounds.
- Weapon attack effects.
- Movement sounds.
- Environmental ambience.
- Boss fight audio.

# 15. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Game Framework | Pygame |
| Data Storage | JSON |
| Version Control | Git |
| Repository | GitHub |
| Development Environment | VS Code |

No commercial game engine will be used.

# 16. Asset Requirements

Required assets include:
- Hero sprites and animations.
- Enemy sprites.
- Dungeon tilesets.
- Weapons and equipment.
- UI elements.
- Backgrounds.
- Sound effects and music.

Potential asset sources:
- Kenney
- OpenGameArt
- itch.io
- GitHub asset repositories

All third-party assets must have their licenses checked before inclusion.

# 17. Development Roadmap

### Phase 1 — Foundation
- Set up the Pygame project.
- Create the game window and main loop.
- Implement player movement.
- Add player sprites.
- Implement camera movement.

### Phase 2 — Dungeon System
- Implement dungeon tiles.
- Create room generation.
- Connect rooms using corridors.
- Validate dungeon connectivity.

### Phase 3 — Combat
- Implement player attacks.
- Add enemy AI.
- Implement collisions.
- Add health and damage systems.

### Phase 4 — RPG Systems
- Inventory.
- Weapons and armour.
- Loot drops.
- XP and leveling.

### Phase 5 — World Expansion
- Multiple dungeon floors.
- Special rooms.
- Shops and checkpoints.
- Floor bosses.

### Phase 6 — Polish
- Main menu and pause menu.
- Animations and effects.
- Audio.
- Save/load system.
- Testing and optimization.

# 18. First Playable Milestone

The first playable version must contain:

- One controllable hero.
- One generated dungeon floor.
- Multiple connected rooms and corridors.
- At least one enemy.
- Real-time combat.
- Health and damage systems.
- A dungeon exit or progression point.

**GDD Version 1.0 — Initial design baseline.**

Future features and changes will be documented in subsequent versions.