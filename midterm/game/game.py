from __future__ import print_function
import sys
from character import Character
from monster import Evil_robot
from monster import Doc_student


class Game:
	
	def setup(self):
		self.player = Character()
		self.monsters = [Evil_robot()]

		self.monster = self.get_next_monster()

	def get_next_monster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None


	def monster_turn(self):
		if self.monster.attack():
			print('{} is attacking'.format(self.monster))

			if raw_input("Do you want to dodge? Y/N ").lower() == 'y':
				if self.player.dodge():
					print('you dodged the attack')
				else:
					print("you got hit")
					self.player.hp -= 1
			else:
				print("You got punched by a monster")
				self.player.hp -= 1
		else:
			print("{} is stopping to check you out".format(self.monster))



	def player_turn(self):
		player_choice = raw_input('[A]ttack, [R]est, [Q]uit? ').lower()
		if player_choice == 'a':
			print('You are attacking {}'.format(self.monster))

			if self.player.attack():
				if self.monster.dodge():
					print('{} dodged your attack!'.format(self.monster))
				else:
					if self.player.level_up():
						self.monster.hp -= 2
					else:
						self.monster.hp -= 1

					print('You hit the {}!'.format(self.monster))
			else:
				print("You missed")
		elif player_choice == 'r':
			self.player.rest()
		elif player_choice == 'q':
			sys.exit()
		else:
			self.player_turn()


	def cleanup(self):
		if self.monster.hp <= 0:
			self.player.xp += self.monster.xp
			print("You killed a {}".format(self.monster))
			self.monster = self.get_next_monster()


	def __init__(self):
		self.setup()

		while self.player.hp and (self.monster or self.monsters):
			print('\n'+'='*20)
			print (self.player)
			self.monster_turn()
			print('-'*20)
			self.player_turn()
			self.cleanup()
			print('\n'+'='*20)

		if self.player.hp:
			print('You win!')
		elif self.monsters or self.monster:
			('You lose!')
		sys.exit()

Game()