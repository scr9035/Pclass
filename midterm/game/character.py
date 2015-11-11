from __future__ import print_function
import random

from combat import Combat

class Character(Combat):
	attack_limit = 1
	defense = 1
	xp = 0
	base_hp = 30


	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.char_class == 'coden00b':
			roll += 1
		elif self.char_class == '1337fizzbuzz':
			roll += 2
		return roll > 4


	def get_char_class(self):
		char_class_choice = raw_input("Character Class ([1]Coden00b, [2]1337Fizzbuzz): ").lower()

		if char_class_choice in '12':
			if char_class_choice == '1':
				self.attack_limit += 9
				self.defense  += 7
				return 'coden00b'

			elif char_class_choice == '2':
				self.attack_limit += 7
				self.defense  += 9
				return '1337fizzbuzz'

		else:
			return self.get_get_char_class()


	def __init__(self, **kwargs):
		self.name = raw_input("Name: ")
		self.char_class = self.get_char_class()
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