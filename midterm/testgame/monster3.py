from __future__ import print_function
import random
from combat import Combat


COLORS = ['rusted', 'copper', 'silver', 'iridium']


class Monster(Combat):
    """Basic monster class attributes"""
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    attack_strength = 1
    attack_defense = 1
    weapon = 'sword'
    sound = 'roar!'
    location = (0, 0)

    def __init__(self, c, **kwargs):
        """Sets the monsters hp and xp from min/max values
            if other attributes set, will add them into dictionary in the for loop"""
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        "Returns  the monsters name with the first letter capitalized"
        return '{} {}'.format(self.color.title(),
                              self.__class__.__name__, 
                              )

    def battlecry(self):
        """Return the battlecry of the enemy."""
        return self.sound


class Evil_robot(Monster):  
    """Subclass of monster, Evil robot created by the bitter doctoral student."""
    max_hit_points = 15
    max_experience = 6
    attack_limit = 7
    attack_strength = 9
    attack_defense = 7
    color = random.choice(COLORS)
    sound = "\033[1;31mAttack and Destroy!\033[1;m"


class Doc_student(Monster):
    """Sub class of Monster, Doctoral student; weak, but will not die due to pure will to finish dissertation"""
    min_hit_points = 30
    max_hit_points = 40
    min_experience = 2
    max_experience = 5
    attack_limit = 5
    attack_strength = 4
    attack_defense = 0
    color = "pale"
    sound = 'Fooooood'


