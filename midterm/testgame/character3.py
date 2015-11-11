from __future__ import print_function
import random
from combat import Combat




class Character(Combat):
    """Sets basic Character class attributes. Also determines character class and gives
       bonus/penalties based on class."""
    attack_strength = 8
    attack_defense = 7
    attack_limit = 16
    experience = 0
    base_hit_points = 30
    potion = 1
    location = (0, 0)
    block_limit = 10

    def attack(self):
        """Pic a random number between 1 and characters attack_limit. If roll is
           greater than 3 the attack is successful. Character class can increase
           the probability for a successful attack."""
        roll = random.randint(2, self.attack_limit)
        if self.char_class == 'coden00b':
            roll += 1
        elif self.char_class == '1337lulz':
            roll += 2
        return roll > 4

    def get_char_class(self):
        """Prompt user to choose a character class and sets that 
           character classes attributes"""
        self.c.send('Choose your Character type:\n[1] coden00b \n'
                          '[2] 1337lulz \n'
                          '[3] WeRBoozonymous\n>')
        char_class_choice = self.c.recv(10)[0]
        #print("choice: ", char_class_choice)

        if char_class_choice in '123':
            if char_class_choice == '1':
                self.attack_strength += 2
                #self.dodge_limit -= 1
                self.attack_defense += 1
                return 'coden00b'
            elif char_class_choice == '2':
                self.attack_strength += 1
                #self.dodge_limit += 3
                self.attack_defense += 3
                return '1337lulz'
            elif char_class_choice == '3':
                #self.dodge_limit += 6
                self.attack_limit -= 1
                self.potion += 6
                return 'werboozonymous'
        else:
            return self.get_char_class()

    def __init__(self, c, *args, **kwargs):
        """Init when character class is called. Asks user to input name and what
           type of character class they want to play"""
        self.c = c
        self.c.send('Name: ')
        self.name = self.c.recv(30)
        self.char_class = self.get_char_class()
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        
        return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

    def rest(self):
        """Sets number of hitpoints recovered after drinking the booze."""
        if self.hit_points < self.base_hit_points:
            self.hit_points += self.potion + 5
            if self.hit_points > self.base_hit_points:
                self.hit_points -= (self.hit_points - self.base_hit_points)

    