from __future__ import print_function
from combat import Combat
import random




class Monster(Combat):
	min_hp = 1
	max_hp = 1
	min_xp = 1
	max_xp = 1
	strength = 1
	defense = 1
	weapon = "CS homework"

	def __init__(self, **kwargs):
		self.hp = random.randint(self.min_hp, self.max_hp)
		self.xp = random.randint(self.max_xp, self.max_xp)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.__class__.__name__, self.hp, self.xp)



class Evil_robot(Monster):
	max_hp = 1
	min_hp = 1
	max_xp = 3
	strength = 9
	defense = 7
	weapon = "keyboard"


class Doc_student(Monster):
	min_hp = 40
	max_hp = 50
	min_xp = 4
	max_xp = 5
	strength = 1
	defense = 1
	weapon = "distain and bitterness"
