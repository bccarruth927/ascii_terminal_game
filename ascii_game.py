from util_funcs import greeting
from validation_funcs import validate_player_age, validate_player_race, validate_combat_class
import random

class Player:
    # To create the Player character user input is collected to generate a name, age and desired fantasy class,
    # Class and fantasy race determines the characters primary stats upon initialization,
    # Stats are categorized as strength, dexterity and wisdom. Defeating monsters raises stats,
    # The Player character is not dead upon initialization
    # The Player health is initially set to 20, raised by 5 with each successful vanquished monster encounter
    def __init__(self, name, age, race, combat_class):
        self.name = name
        self.age = age
        self.race = race
        self.combat_class = combat_class
        self.health = 30
        self.strength = 0
        self.dexterity = 0
        self.wisdom = 0
        self.is_dead = False

        # Control flow statement to raise Player stats based on fantasy race selection
        if self.race == 'human':
            self.strength += 10
            self.dexterity += 5
            self.wisdom += 3
        elif self.race == 'elf':
            self.strength += 3
            self.dexterity += 10
            self.wisdom += 5
        else:
            self.strength += 7
            self.dexterity += 3
            self.wisdom += 5
        
        # Control flow statement to raise Player stats based on fantasy class selection
        if self.combat_class == 'warrior':
            self.strength += 10
            self.dexterity += 5
            self.wisdom += 3
        elif self.combat_class == 'archer':
            self.strength += 3
            self.dexterity += 10
            self.wisdom += 5
        else:
            self.strength += 3
            self.dexterity += 5
            self.wisdom += 10
    
    def __repr__(self):
        # Printing the Player character will provide a description including their name and stats
        # Modify combat_class string from lower() to title() for the description
        self.combat_class = self.combat_class.title()
        description = 'Greetings {name}! You are a {race} from the Realm of Python! You are a {combat_class} class and your current health is at {health}. Your strength is {strength}, your dexterity is {dexterity} and your wisdom is {wisdom}.'.format(name=self.name, race=self.race.title(), combat_class=self.combat_class.title(), health=self.health, strength=self.strength, dexterity=self.dexterity, wisdom=self.wisdom)

        # Control flow to adjust description based on whether the Player character is dead or not
        if self.is_dead:
            description += ' Sadly you are dead. You lived to about {age} years of age.'.format(age=self.age)
        else:
            description += ' Fortunately you have not yet died! You are {age} years of age.'.format(age=self.age)
        
        return description
    
    def player_dies(self, monster):
        # If the player loses all of their health then the is_dead attribute is switched to false
        self.is_dead = True

        # A negative value could potentially result in a bug where the player continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0
        
        print('Oh no! {name} died fighting {monster}!'.format(name=self.name, monster=monster.name))

    def gain_health(self):
        # If the player successfully defeats a monster, increase their health by 2
        self.health += 2

    def lose_health(self, monster):
        # Health lost depends on the combat class of the Player and the type of monster being fought
        if self.combat_class == 'warrior' and monster.name == 'ogre':
            self.health -= monster.strength / 5
            print('Your training as a {combat_class} pays off! The {monster}\'s attack is reduced significantly'.format(combat_class=self.combat_class.title(), monster=monster.name.title()))
        elif self.combat_class == 'warrior' and monster.name == 'goblin':
            self.health -= monster.strength
            print('The {monster} proves to be more nimble than you. You take full damage.'.format(monster=monster.name.title()))
        elif self.combat_class == 'warrior' and monster.name == 'spectre':
            self.health -= monster.strength / 2
            print('Your training as a {combat_class} has provided you with mental fortitude. The {monster}\'s attack is reduced by half'.format(combat_class=self.combat_class.title(), monster=monster.name.title()))
        elif self.combat_class == 'archer' and monster.name == 'ogre':
            self.health -= monster.strength / 2
            print('You\'re long range attack style proves troublesome for the {monster}. {monster}\'s attack is reduced by half'.format(monster=monster.name.title()))
        elif self.combat_class == 'archer' and monster.name == 'goblin':
            self.health -= monster.strength / 5
            print('You\'re naturally dexterous making it easy to dodge the {monster}\'s attacks. {monster}\'s attack is significantly reduced'.format(monster=monster.name.title()))
        elif self.combat_class == 'archer' and monster.name == 'spectre':
            self.health -= monster.strength
            print('You have little to no defense against the {monster}. You take full damage.'.format(monster=monster.name.title()))
        elif self.combat_class == 'mage' and monster.name == 'ogre':
            self.health -= monster.strength
            print('You\'re magical training has left you ill prepared for the brute force of the {monster}. You take full damage.'.format(monster=monster.name.title()))
        elif self.combat_class == 'mage' and monster.name == 'goblin':
            self.health -= monster.strength / 2
            print('You\'re lack of physical armor leaves you light on your feet. {monster}\'s attack is reduced by half.'.format(monster=monster.name.title()))
        elif self.combat_class == 'mage' and monster.name == 'spectre':
            self.health -= monster.strength / 5
            print('Years of magical training as {combat_class} prepares you for otherwordly attacks! {monster}\'s attack is significantly reduced.'.format(combat_class=self.combat_class.title(), monster=monster.name.title()))
        else:
            # If on the chance of a bug and neither of the above condition are met. Bless the Player by divine intervention
            print('By a divine miracle no damage befalls {name}.'.format(self.name))
    
    def attack_monster(self, monster):
        # Attack strength depends on the combat class of the Player and the monster type
        if self.combat_class == 'warrior' and monster.name == 'ogre':
            monster.health -= self.strength
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.strength))
        elif self.combat_class == 'warrior' and monster.name == 'goblin':
            monster.health -= self.dexterity
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.dexterity))
        elif self.combat_class == 'warrior' and monster.name == 'spectre':
            monster.health -= self.wisdom
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.wisdom))
        elif self.combat_class == 'archer' and monster.name == 'ogre':
            monster.health -= self.dexterity
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.dexterity))
        elif self.combat_class == 'archer' and monster.name == 'goblin':
            monster.health -= self.strength
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.strength))
        elif self.combat_class == 'archer' and monster.name == 'spectre':
            monster.health -= self.wisdom
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.wisdom))
        elif self.combat_class == 'mage' and monster.name == 'ogre':
            monster.health -= self.strength
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.strength))
        elif self.combat_class == 'mage' and monster.name == 'goblin':
            monster.health -= self.dexterity
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.dexterity))
        elif self.combat_class == 'mage' and monster.name == 'spectre':
            monster.health -= self.wisdom
            print('You attack the {monster} for {damage} points of damage.'.format(monster=monster.name.title(), damage=self.wisdom))
        else:
            # If on the chance of a bug and neither of the conditions above are met. Blame divine punishment
            print('Is is divine punishment? No damage befalls the {monster}'.format(monster=monster.name))

    def boost_stats(self, monster):
        # Boosted stat depends on the monster fought
        if monster.name == 'ogre':
            self.strength += 2
        elif monster.name == 'goblin':
            self.dexterity += 2
        else:
            self.wisdom += 2

class Ogre:
    # Attributes for the Ogre Class
    def __init__(self):
        self.name = 'ogre'
        self.health = 35
        self.strength = 15
        self.is_dead = False

    def monster_dies(self):
        # If the Ogre loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0

class Goblin:
    # Attributes for the Goblin Class
    def __init__(self):
        self.name = 'goblin'
        self.health = 20
        self.strength = 7
    
    def monster_dies(self):
        # If the Goblin loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0

class Spectre:
    # Attributes for the Spectre Class
    def __init__(self):
        self.name = 'spectre'
        self.health = 25
        self.strength = 10

    def monster_dies(self):
        # If the Spectre loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0


# Greet the player and give a brief description to game and game play
# greeting()


# Collect user input for the name, age, fantasy race and class of their character
# player_name = input('What is the name of your player?\n> ')

# player_age = validate_player_age()

# player_race = validate_player_race()

# player_class = validate_combat_class()

# Instantiate the Player character
# player_character = Player(player_name, player_age, player_race, player_class)

player_character = Player('Brenden the Almighty', 26, 'human', 'warrior')

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
            player_character.lose_health(monster)

    # Determine whether the player or the monster survived the encounter, if they died break the loop
    # If the player survives, reset the player health to be equal to their health before the monster encounter
    # Increase the players health and relevant stat based on the type of monster fought
    if player_character.health <= 0:
        player_character.player_dies(monster)
        break
    else:
        monster.monster_dies()
        print('\nCongratulations! You defeated the {monster}!'.format(monster=monster.name.title()))
        player_character.health = health_before_fight
        player_character.gain_health()
        player_character.boost_stats(monster)
        print('You\'re health and stats have increased! You now have {health} points of health. You\'re strength stat is {strength}, dexterity is {dexterity} and wisdom is {wisdom}.\n'.format(health=player_character.health, strength=player_character.strength, dexterity=player_character.dexterity, wisdom=player_character.wisdom))
    
    # Determine if the player wants to continue fighting monsters
    ready_to_fight = input('\nAre you ready to keep fighting some monsters? Y/N\n> ')
    ready_to_fight = ready_to_fight.lower()

    while ready_to_fight != 'y' and ready_to_fight != 'n':
        ready_to_fight = input('\nWe\'re sorry... but we need either "Y" for yes or "N" for no\n> ')
        ready_to_fight = ready_to_fight.lower()

    if ready_to_fight == 'n':
        break
