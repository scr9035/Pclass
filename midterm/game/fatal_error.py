from __future__ import print_function
import random
import logging
import sys
from character import Character
from monster import Evil_robot, Doc_student

#what does
logging.basicConfig(filename='game.log', level=logging.DEBUG)


'''builds the 5x5 playing matrix'''
CELLS = [(0,0),(0,1),(0,2),(0,3),(0,4),
		 (1,0),(1,1),(1,2),(1,3),(1,4),
		 (2,0),(2,1),(2,2),(2,3),(2,4),
		 (3,0),(3,1),(3,2),(3,3),(3,4),
		 (4,0),(4,1),(4,2),(4,3),(4,4)]


class Game(object):

	def setup(self):

		self.player = Character()
		self.robot1 = Evil_robot()
		self.robot2 = Evil_robot()
		self.robot3 = Evil_robot()
		self.doc_student1 = Doc_student()

		self.monsters = [self.robot1,
						 self.robot2,
						 self.robot3,
						 self.doc_student1]


		self.player.location = random.choice(CELLS)
		self.door = random.choice(CELLS)


		for item in self.monsters:
			item.location = random.choice(CELLS)

		#if monster == door or monster == start or door == start:
		#return get_locations()


	def show_help(self):
		print("help instructions here")


	def move_player(self, player, move):
		x,y = player

		if move == 'LEFT':
			y -= 1
		elif move == 'RIGHT':
			y += 1
		elif move == 'UP':
			x -= 1
		elif move == 'DOWN':
			x += 1
	
		return x,y

	def get_moves(self, player):
		moves = ['LEFT','RIGHT','UP','DOWN']

		if player[1] == 0:
			moves.remove('LEFT')
		if player[1] == 4:
			moves.remove('RIGHT')
		if player[0] == 0:
			moves.remove('UP')
		if player[0] == 4:
			moves.remove('DOWN')

		return moves


	def draw_map(self, player):
		print('_ _ _ _ _')
		tile = '|{}'

		for idx, cell in enumerate(CELLS):
			if idx in [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23]:
				if cell == player:
					print(tile.format('X'), end='')
				else:
					print(tile.format('_'), end='')
			else:
				if cell == player:
					print(tile.format('X|'))
				else:
					print(tile.format('_|'))


	def player_dies(self,monster):
		print(self.player)
		if self.player.hp <= 0:
			print("{} has destroyed your will to live".format(monster))
			sys.exit()


	def monster_turn(self, monster):
		if monster.attack():
			print('{} attacks!'.format(monster))

			if raw_input('Do you try and dodge? (Y/N):').lower() == 'y':
				if self.player.dodge():
					print("You blocked the {}'s attack".format(monster))
				else:
					print("You failed to dodge and are hit!")
					self.player.hp -= round(self.monster.strength)
					self.player_dies(monster)
					logging.info(self.player)
			else:
				print("{} hit's you!".format(monster))
				self.player.hp -= round(self.monster.strength)
				self.player_dies(monster)
		else:
			print("{} stops to check you out".format(monster))


	def player_turn(self, monster):
		if self.player.attack():
			if monster.dodge():
				print('{} dodged your attack'.format(monster))
			else:
				monster.hp -= self.player.attack_limit
				print("You hit the {} for {} HP".format(monster, self.player.attack_limit))
		else:
			print('Your attack misses')


	def cleanup(self):
		if self.monster.hp <=0:
			logging.info('{}'.format(self.player))
			self.monster.location = 0

	def __init__(self):
		self.setup()

		print("Welcome to CS Hell")
		print('Your stats {} \n'.format(self.player))

		logging.info('robot1 {}, robot2 {}, robot3 {}, doc_student1 {}'.
		format(self.robot1.location, self.robot2.location, self.robot3.location,
			   self.doc_student1.location, self.door))

		player = self.player.location
		logging.info('Player location {}'.format(player))

		while True:

			moves = self.get_moves(player)

			self.draw_map(player)
			print('\n You are in room {}'.format(player))

			for monster in self.monsters:
				self.monster = monster
				if player == self.monster.location:
					print('In this room there is a {}!'.format(self.monster))
					logging.info("Monster: {}".format(self.monster))

				if player == self.door:
					print('You have found your backpack!')
					sys.exit()


				while self.monster.hp > 0:

					print('_'*50 + '\n')
					self.monster_turn(self.monster)
					move = raw_input('Do you [A]ttack, [R]est, or [Q]uit? ').lower()

					if move == 'a':
						print('You attack the {}! '.format(monster))
						self.player_turn(self.monster)
					elif move == 'r':
						self.player.hp += 1
						print('You rest and gain back 1 HP')
					elif move == 'q':
						sys.exit()
					else:
						print('Invalid choice')
						continue

			if player == self.door:
					print('You have found your backpack!')
					sys.exit()


			print('You can move {}'.format(moves))
			print('Enter [Q]uit exit the game')
			move = raw_input('> ')
			move = move.upper()
			if move == 'Q':
				sys.exit()
			if move in moves:
				player = self.move_player(player, move)
			else:
				print('Not a valid move. \n')
				continue

Game()




				


