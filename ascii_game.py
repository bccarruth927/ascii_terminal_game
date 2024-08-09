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
        self.health = 20
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
        description = 'Greetings {name}! You are a {race} from the Realm of Python! You are a {combat_class} class and your current health is at {health}. Your strength is {strength}, your dexterity is {dexterity} and your wisdom is {wisdom}.'.format(name=self.name, race=self.race, combat_class=self.combat_class, health=self.health, strength=self.strength, dexterity=self.dexterity, wisdom=self.wisdom)

        # Control flow to adjust description based on whether the Player character is dead or not
        if self.is_dead:
            description += ' Sadly you are dead. You lived to about {age} years of age.'.format(age=self.age)
        else:
            description += ' Fortunately you have not yet died! You are {age} years of age.'.format(age=self.age)
        
        return description

# Test whether Player class initializes correctly
player_character = Player('The Mighty Brenden', 26, 'human', 'warrior')
print(player_character)
