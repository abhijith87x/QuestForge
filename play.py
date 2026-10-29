from patterns.facade import QuestForgeAPI
from infra.save_adapter import JsonFileAdapter
from patterns.state import BattleStateMachine, BattleState
from patterns.strategy import AggressiveAI
from patterns.command import AttackCommand, CommandHistory
from patterns.observer import EventBus, CombatLogger, AchievementTracker, GameEvent
from patterns.creational import EnemyBuilder
from domain.exceptions import QuestForgeError

def main():
    api  =  QuestForgeAPI(JsonFileAdapter())
    api.new_game([("warrior", 'Bram'),("mage", 'Sylla')])
    
    enemy = (EnemyBuilder("Orc Chief").with_health(30).with_attack(20).with_loot(["GreatAxe"]).build())
    enemy2 =(EnemyBuilder("Jithu").with_health(30).with_attack(20).with_loot(["GreatAxe"]).build())
    
    enemy.ai_strategy = AggressiveAI()
    enemy2.ai_strategy = AggressiveAI()
    
    
    bus = EventBus()
    bus.subscribe(CombatLogger())
    tracker = AchievementTracker()
    bus.subscribe(tracker)
    
    enemy.event_bus = bus
    enemy2.event_bus = bus
    
    history = CommandHistory()
    battle = BattleStateMachine()
    battle.transition(BattleState.PLAYER_TURN)
    
    party  = api.manager.party
    round_num = 0
    
    while battle.state not in (BattleState.VICTORY, BattleState.DEFEAT):
        
        
       
        
        if battle.state == BattleState.PLAYER_TURN:
            round_num += 1
            print(f"\n--Round {round_num} ---")
            
            print("player turn")
            
            enemies = [enemy, enemy2]

            for member in party:
                if not member.is_alive:
                    print("name for dead member",member.name)
                    continue

                for target in enemies:
                    if not target.is_alive:
                        continue

                    try:
                        print(f"health of the target{target.name} is {target.health}")
                        history.run(AttackCommand(member, target))
                        print("a")
                    except QuestForgeError as e:
                        print(f"Action failed: {e}")
                        break

                    # if not target.is_alive:
                    #     bus.publish(
                    #         GameEvent("ENEMY_DEFEATED", {"name": target.name})
                    #     )

                    # break

            battle.transition(BattleState.ENEMY_TURN)
            
        elif battle.state == BattleState.ENEMY_TURN:
            print("enemy turn")
            for current_enemy in [enemy, enemy2]:
                if current_enemy.is_alive:
                    living_party = [p for p in party if p.is_alive]
                    if not living_party:
                        break   
                    target = current_enemy.ai_strategy.choose_target(living_party) 
                    print(f"health of the player{target.name} is {target.health}") 
                    history.run(AttackCommand(current_enemy, target))
                    print(f"health of the player{target.name} is {target.health}") 
            battle.transition(BattleState.RESOLUTION)
            
        elif battle.state == BattleState.RESOLUTION:
            print("resolution")
            if all(not p.is_alive for p in party):
                battle.transition(BattleState.DEFEAT)
            elif not enemy.is_alive and not enemy2.is_alive:
                battle.transition(BattleState.VICTORY)
            else:
                battle.transition(BattleState.PLAYER_TURN)
    print("\nVICTORY!" if battle.state == BattleState.VICTORY else "\nDEFEAT")
    api.save()
    print(f"Game saved. Achievements:{tracker.unlocked}")
      
main()
