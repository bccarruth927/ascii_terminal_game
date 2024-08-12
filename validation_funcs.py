def validate_player_age():
    # Ensure that the user can only enter an age between 13 and 169
    player_age = input('\nHow old is your character?\n> ')
    player_age = int(player_age)

    while player_age < 13 or player_age > 169:
        player_age = input('\nWe\'re sorry... but that age is crazy! Please choose a number between 13 and 169.\n> ')
        player_age = int(player_age)

    return str(player_age)


def validate_player_race():
    # Ensure that the user can only enter a race defined in valid_races
    valid_races = ['human', 'elf', 'dwarf']
    
    player_race = input('\nWhich fantasy race do you want your character to be? Choose from "Human", "Elf" or "Dwarf".\n> ')
    player_race = player_race.lower()

    while player_race not in valid_races:
        player_race = input('\nWe\'re sorry... but the realm of Python doesn\'t know that race. Please choose either "Human", "Elf" or "Dwarf".\n> ')
        player_race = player_race.lower()

    return player_race


def validate_combat_class():
    # Ensure that the user can only enter a combat class defined in valid_combat_classes
    valid_combat_classes = ['warrior', 'archer', 'mage']

    player_class = input('\nWhich fantasy class fo you want your character to be? Choose from "Warrior", "Archer" or "Mage".\n> ')
    player_class = player_class.lower()

    while player_class not in valid_combat_classes:
        player_class = input('\nWe\'re sorry... but the realm of Python has never heard of that class. Please choose either "Warrior", "Archer", or "Mage".\n> ')
        player_class = player_class.lower()

    return player_class