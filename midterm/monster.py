
from __future__ import print_function
from combat import Combat
import random

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
	min_hp = 1
	max_hp = 1
	min_xp = 1
	max_xp = 1
	weapon = "sword"
	sound = 'roar'

	def __init__(self, **kwargs):
		self.hp = random.randint(self.min_hp, self.max_hp)
		self.xp = random.randint(self.max_xp, self.max_xp)
		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
											  self.__class__.__name__,
											  self.hp,
											  self.xp)

	def battlecry(self):
		return self.sound.upper()


class Goblin(Monster):
	max_hp = 3
	max_xp = 2
	sound = 'bawahaa'


class Troll(Monster):
	min_hp = 3
	max_hp = 5
	min_xp = 2
	max_xp = 6
	sound = 'growl'

class Dragon(Monster):
	min_hp = 5
	max_hp = 10
	min_xp = 6
	max_xp = 10
	sound = 'Hello weakling'
