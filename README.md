# QuestForge — Architecture Overview


## System Summary
QuestForge is a modular, extensible, turn-based RPG battle engine. It supports pluggable character classes, dynamic inventory systems, customizable AI strategies, and save/load persistence. The architecture heavily utilizes GoF design patterns to ensure the domain logic remains decoupled from the CLI and storage layers.


## Component Diagram 


    ┌─────────────────────┐
    │      play.py (CLI)  │
    └──────────┬───────────┘
               │ uses
    ┌──────────▼───────────┐
    │   QuestForgeAPI      │  (Facade)
    └──────────┬───────────┘
       ┌────────┼─────────────┬───────────────┐
       ▼        ▼             ▼               ▼
 GameManager CharacterFactory SaveAdapter    EventBus
 (Singleton) / EnemyBuilder   (Adapter)      (Observer)
       │                                      │
       ▼                                      ▼
  Character (ABC)                       CombatLogger /
   ├─ Warrior                           AchievementTracker
   ├─ Mage
   ├─ Rogue
   ├─ Cleric
   └─ Enemy
       │  has-a
       ▼
   Inventory ── contains ──> Item (ABC)
                               ├─ Potion (Usable)
                               └─ Weapon (Equippable)


   Buffs: RageBuff / PoisonDebuff  --(Decorator wraps)--> Character
   Actions: AttackCommand / UseItemCommand --(Command)--> executed via CommandHistory
   Battle flow: BattleStateMachine (State) drives AggressiveAI/DefensiveAI (Strategy)


## Design Pattern Index
| Pattern | Where Used | Problem Solved |
|---|---|---|
| Factory Method | CharacterFactory | Decouple character creation from concrete classes |
| Builder | EnemyBuilder | Configure enemies with many optional stats/loot |
| Singleton | GameManager | Single source of truth for session state |
| Decorator | RageBuff, PoisonDebuff | Add temporary effects without modifying Character |
| Adapter | JsonFileAdapter, InMemoryAdapter | Swap storage backend without touching game logic |
| Facade | QuestForgeAPI | One simple entry point over many subsystems |
| Strategy | AggressiveAI, DefensiveAI | Swappable enemy decision-making |
| State | BattleStateMachine | Explicit, illegal-transition-proof battle flow |
| Observer | EventBus, CombatLogger, AchievementTracker | Decouple game events from reactions to them |
| Command | AttackCommand, CommandHistory | Undoable, loggable player/enemy actions |


## SOLID Compliance Notes
- **SRP**: `Character` manages stats, while `CombatLogger` manages printing output.
- **OCP**: We added `Cleric` and `DefensiveAI` without altering any existing code.
- **LSP**: All character subclasses reliably implement `take_damage` and `heal`.
- **ISP**: `Item` was split into `Usable` and `Equippable` interfaces.
- **DIP**: `QuestForgeAPI` depends on the `SaveAdapter` abstraction, not `JsonFileAdapter`.


## Key Trade-offs & Alternatives Considered
- **Singleton Choice:** We chose one Singleton (`GameManager`) to track global session state, avoiding passing a session object through every function, but deliberately avoided making `Character` or `Item` singletons to maintain testability.
- **Composition vs Inheritance:** We used Composition for inventories and equipment to prevent class explosion (e.g., avoiding `WarriorWithFireSword`).
- **Separation of UI:** The CLI is deliberately kept completely separate from the `domain/` logic. This architecture allows swapping the CLI for a graphical UI (Pygame or web) with zero changes to the underlying rules.


## How to Extend
- **Add a new character class:** Implement `Character`, register in `CharacterFactory`. No other file changes needed.
- **Add a new buff:** Subclass `CharacterBuff`. No changes to `Character`.
- **Add a new save backend:** Implement `SaveAdapter`. No changes to `QuestForgeAPI` callers.