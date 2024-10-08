from util_funcs import greeting
from validation_funcs import validate_player_age, validate_player_race, validate_combat_class
from classes import Player, Ogre, Goblin, Spectre, BossMonster
import random


# Greet the player and give a brief description to game and game play
greeting()


# Collect user input for the name, age, fantasy race and class of their character
player_name = input('What is the name of your player?\n> ')

player_age = validate_player_age()

player_race = validate_player_race()

player_class = validate_combat_class()

# Instantiate the Player character
player_character = Player(player_name, player_age, player_race, player_class)


# Instantiate monster characters
# Append monster characters to list of monsters
ogre = Ogre()
goblin = Goblin()
spectre = Spectre()

monsters_list = []

monsters_list.append(ogre)
monsters_list.append(goblin)
monsters_list.append(spectre)


# Collect user input to determine if the user is ready to start fighting monsters
ready_to_fight = input('Are you ready to start fighting some monsters? Y/N\n> ')
ready_to_fight.lower()

if ready_to_fight != 'y':
    print('You won\'t save the Realm sitting in the tavern. Ready or not... you\'re fighting monsters!')
    ready_to_fight = 'y'


while player_character.health > 0 and ready_to_fight == 'y':
    # Set the player character health to their current health before they start fighting monsters
    health_before_fight = player_character.health

    # Determine which enemy the player will be fighting from the monsters_list
    random_index = random.randint(0, 2)
    monster = monsters_list[random_index]
    
    # While both the player and the monster they continue to exchange attacks until one dies
    # Attack pattern is randomly decided by a 50/50 chance
    while player_character.health > 0 and monster.health > 0:
        attack_pattern = random.randint(0, 1)

        if attack_pattern == 1:
            player_character.attack_monster(monster)
        else:
            monster.attack_player(player_character)

    # Determine whether the player or the monster survived the encounter, if they died break the loop
    # If the player survives, reset the player health to be equal to their health before the monster encounter
    # Increase the players health and relevant stat based on the type of monster fought
    if player_character.health <= 0:
        player_character.player_dies(monster)
        break
    else:
        monster.monster_dies()
        monster.raise_stats()
        print('\nCongratulations! You defeated the {monster}!'.format(monster=monster.name.title()))
        player_character.health = health_before_fight
        player_character.gain_health()
        player_character.boost_stats(monster)
        print('You\'re health and stats have increased! You now have {health} points of health. You\'re strength stat is {strength}, dexterity is {dexterity} and wisdom is {wisdom}.\n'.format(health=player_character.health, strength=player_character.strength, dexterity=player_character.dexterity, wisdom=player_character.wisdom))
    
    # Determine if the player wants to continue fighting monsters
    ready_to_fight = input('\nAre you ready to keep fighting some monsters? Or are you ready to face the boss? "Y" to keep fighting, "N" to face the boss.\n> ')
    ready_to_fight = ready_to_fight.lower()

    while ready_to_fight != 'y' and ready_to_fight != 'n':
        ready_to_fight = input('\nWe\'re sorry... but we need either "Y" for yes or "N" for no\n> ')
        ready_to_fight = ready_to_fight.lower()

    if ready_to_fight == 'n':
        break


# Ensure that the player is alive before starting the boss fight
if player_character.is_dead == False:
    # Instantiate the boss monster
    boss_monster = BossMonster()


    # Collect user input to start the boss fight
    fight_the_boss = input('\nNo turning back now. The lair of {monster} lays before you. All that\'s left is to defeat it. If you\'re ready lets hear a "Leroy Jenkins!"!\n> '.format(monster=boss_monster.name.title()))
    # If the user enters any other input switch automatically to the requirement to start the boss fight
    fight_the_boss = 'leroy jenkins!'


    # Start the boss fight
    # Boss fight will continue until either the boss monster of the player dies
    # If the player beats the boss the player wins!
    while player_character.health > 0 and fight_the_boss == 'leroy jenkins!':
        # While both the player and the boss continue to exchange attacks until one dies
        # Attack pattern is randomly decided by a 50/50 chance
        while player_character.health > 0 and boss_monster.health > 0:
            attack_pattern = random.randint(0, 1)

            if attack_pattern == 1:
                player_character.attack_monster(boss_monster)
            else:
                boss_monster.attack_player(player_character)

        # Determine whether the player or the monster survived the encounter, if they died break the loop
        # If the player survives, reset the player health to be equal to their health before the monster encounter
        # Increase the players health and relevant stat based on the type of monster fought
        if player_character.health <= 0:
            player_character.player_dies(boss_monster)
            break
        else:
            boss_monster.monster_dies()
            print('\nCongratulations! You defeated the {monster}! You have saved the Realm of Python!'.format(monster=boss_monster.name.title()))
            break