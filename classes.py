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
    
    def attack_monster(self, monster):
        # Attack patterns are randomly generated
        # Depending on the randomly generated attack, attack strength depends on relevant stat compared to monster's
        # Generate random attack pattern
        random_attack = random.randint(1,3)

        if random_attack == 1:
            if self.strength > monster.strength:
                monster.health -= self.strength / 1.5
                print('Your strength is superior to that of the {monster}. Your attack does full strength damage.'.format(monster=monster.name.title()))
            else:
                monster.health -= self.strength / 2
                print('The {monster}\'s strength is greater than yours. Your attack has reduced strength damage.'.format(monster=monster.name.title()))
        elif random_attack == 2:
            if self.dexterity > monster.dexterity:
                monster.health -= self.dexterity / 1.5
                print('You prove to be more nimble than the {monster}. You land an attack for full dexterity damage.'.format(monster=monster.name.title()))
            else:
                monster.health -= self.dexterity / 2
                print('The {monster}\'s proves to be more dexterous than you. Your attack has reduced dexterity damage.'.format(monster=monster.name.title()))
        else:
            if self.wisdom > monster.wisdom:
                monster.health -= self.wisdom / 1.5
                print('You are much wiser than your foe, the {monster}. Your attack does full wisdom damage.'.format(monster=monster.name.title()))
            else:
                monster.health -= self.wisdom / 2
                print('Your mental fortitude is outmatched by the {monster}. Your attack has reduced wisdom damage.'.format(monster=monster.name.title()))
        

    def boost_stats(self, monster):
        # Boosted stat depends on the monster fought
        if monster.name == 'ogre':
            self.strength += 3
        elif monster.name == 'goblin':
            self.dexterity += 3
        else:
            self.wisdom += 3


class Ogre:
    # The Ogre is the strongest of the common monsters with the highest strength and health stats
    # Attributes of the Ogre class
    def __init__(self):
        self.name = 'ogre'
        self.health = 35
        self.strength = 15
        self.dexterity = 10
        self.wisdom = 7
        self.is_dead = False


    def monster_dies(self):
        # If the Ogre loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0


    def attack_player(self, player):
        # Attack patterns are randomly generated
        # Depending on the randomly generated attack, attack strength depends on relevant stat compared to monster's
        # Generate random attack pattern
        random_attack = random.randint(1,3)

        if random_attack == 1:
            if self.strength > player.strength:
                player.health -= self.strength / 1.25
                print('The {monster}\'s strength is greater than {player}. The attack does full strength damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.strength / 2
                print('{player}\'s strength is greater than {monster}\'s. The attack has reduced strength damage.'.format(monster=self.name.title(), player=player.name))
        elif random_attack == 2:
            if self.dexterity > player.dexterity:
                player.health -= self.dexterity / 1.25
                print('The {monster} appears to be more nimble than the {player}. The attack lands for full dexterity damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.dexterity / 2
                print('{player} proves to be more dexterous than the {monster}. The attack has reduced dexterity damage.'.format(monster=self.name.title(), player=player.name))
        else:
            if self.wisdom > player.wisdom:
                player.health -= self.wisdom / 1.25
                print('Despite being a {monster}, it\'s wisdom is higher than {player}. The attack does full wisdom damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.wisdom / 2
                print('The mental fortitude of the {monster} is weaker than {player}. Your attack has reduced wisdom damage.'.format(monster=self.name.title(), player=player.name))

    
    def raise_stats(self):
        # To make the monsters competitive, raise stats after each defeat
        self.strength += 2
        self.dexterity += 2
        self.wisdom += 2

class Goblin:
    # The Goblin is the most nimble of the common monsters with the highest dexterity stat but lowest health
    # Attributes of the Goblin class
    def __init__(self):
        self.name = 'goblin'
        self.health = 20
        self.strength = 7
        self.dexterity = 15
        self.wisdom = 10
        self.is_dead = False
    

    def monster_dies(self):
        # If the Goblin loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0


    def attack_player(self, player):
        # Attack patterns are randomly generated
        # Depending on the randomly generated attack, attack strength depends on relevant stat compared to monster's
        # Generate random attack pattern
        random_attack = random.randint(1,3)

        if random_attack == 1:
            if self.strength > player.strength:
                player.health -= self.strength / 1.25
                print('The {monster}\'s strength is greater than {player}. The attack does full strength damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.strength / 2
                print('{player}\'s strength is greater than {monster}\'s. The attack has reduced strength damage.'.format(monster=self.name.title(), player=player.name))
        elif random_attack == 2:
            if self.dexterity > player.dexterity:
                player.health -= self.dexterity / 1.25
                print('The {monster} appears to be more nimble than the {player}. The attack lands for full dexterity damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.dexterity / 2
                print('{player} proves to be more dexterous than the {monster}. The attack has reduced dexterity damage.'.format(monster=self.name.title(), player=player.name))
        else:
            if self.wisdom > player.wisdom:
                player.health -= self.wisdom / 1.25
                print('Despite being a {monster}, it\'s wisdom is higher than {player}. The attack does full wisdom damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.wisdom / 2
                print('The mental fortitude of the {monster} is weaker than {player}. Your attack has reduced wisdom damage.'.format(monster=self.name.title(), player=player.name))

    
    def raise_stats(self):
        # To make the monsters competitive, raise stats after each defeat
        self.strength += 2
        self.dexterity += 2
        self.wisdom += 2


class Spectre:
    # The Spectre is an ethereal monster with the highest wisdom stat but the lowest strength stat
    # Attributes of the Spectre classS
    def __init__(self):
        self.name = 'spectre'
        self.health = 25
        self.strength = 7
        self.dexterity = 10
        self.wisdom = 15
        self.is_dead = False


    def monster_dies(self):
        # If the Spectre loses all its health then the is_dead attribute is switched to true
        self.is_dead = True

        # A negative value could potentially result in a bug where the monster continues to live despite having 0 health
        # Set health to 0 to prevent a bug possibility
        if self.health != 0:
            self.health = 0


    def attack_player(self, player):
        # Attack patterns are randomly generated
        # Depending on the randomly generated attack, attack strength depends on relevant stat compared to monster's
        # Generate random attack pattern
        random_attack = random.randint(1,3)

        if random_attack == 1:
            if self.strength > player.strength:
                player.health -= self.strength / 1.25
                print('The {monster}\'s strength is greater than {player}. The attack does full strength damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.strength / 2
                print('{player}\'s strength is greater than {monster}\'s. The attack has reduced strength damage.'.format(monster=self.name.title(), player=player.name))
        elif random_attack == 2:
            if self.dexterity > player.dexterity:
                player.health -= self.dexterity / 1.25
                print('The {monster} appears to be more nimble than the {player}. The attack lands for full dexterity damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.dexterity / 2
                print('{player} proves to be more dexterous than the {monster}. The attack has reduced dexterity damage.'.format(monster=self.name.title(), player=player.name))
        else:
            if self.wisdom > player.wisdom:
                player.health -= self.wisdom / 1.25
                print('Despite being a {monster}, it\'s wisdom is higher than {player}. The attack does full wisdom damage.'.format(monster=self.name.title(), player=player.name))
            else:
                player.health -= self.wisdom / 2
                print('The mental fortitude of the {monster} is weaker than {player}. Your attack has reduced wisdom damage.'.format(monster=self.name.title(), player=player.name))


    def raise_stats(self):
        # To make the monsters competitive, raise stats after each defeat
        self.strength += 2
        self.dexterity += 2
        self.wisdom += 2