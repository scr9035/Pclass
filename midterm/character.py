
from __future__ import print_function
import random

from combat import Combat

class Character(Combat):
	attack_limit = 10
	xp = 0
	base_hp = 10


	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'sword':
			rol1 += 1
		elif self.weapon == 'axe':
			roll += 2
		return roll > 4


	def get_weapon(self):
		weapon_choice = raw_input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return 'sword'
			elif weapon_choice == 'a':
				return 'axe'
			elif weapon_choice == 'b':
				return 'bow'
		else:
			return self.get_weapon()


	def __init__(self, **kwargs):
		self.name = raw_input("Name: ")
		self.weapon = self.get_weapon()
		self.hp = self.base_hp

		for key, value in kwargs.items():
			setattr(self,key,value)

	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.xp)

	def rest(self):
		if self.hp < self.base_hp:
			self.hp += 1

	def level_up(self):
		return self.xp >= 5
		