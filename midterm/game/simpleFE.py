from __future__ import print_function
import random
import sys
from character import Character
from monster import Evil_robot, Doc_student
from game2 import Game


CELLS = [(0,0),(0,1),(0,2),(0,3),(0,4),
		 (1,0),(1,1),(1,2),(1,3),(1,4),
		 (2,0),(2,1),(2,2),(2,3),(2,4),
		 (3,0),(3,1),(3,2),(3,3),(3,4),
		 (4,0),(4,1),(4,2),(4,3),(4,4)]


def get_locations():
	monster = random.choice(CELLS)
	backpack = random.choice(CELLS)
	start = random.choice(CELLS)

	if monster == backpack or monster == start or backpack == start:
		return get_locations()

	return monster, backpack, start

	#make a list of cells, then look for duplicates. If so return get_locations
	

def move_player(player,move):
	x,y = player

	if move == 'W':
		y -= 1
	elif move == 'E':
		y += 1
	elif move == 'N':
		x -= 1
	elif move == 'S':
		x += 1
	
	return x,y

def get_moves(player):
	moves = ['W','E','N','S']

	if player[1] == 0:
		moves.remove('W')
	if player[1] == 4:
		moves.remove('E')
	if player[0] == 0:
		moves.remove('N')
	if player[0] == 4:
		moves.remove('S')

	return moves

def draw_map(player):
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


def battle(some_character):
	print('Oh NO! You are not alone')
	Game(player1)
	return some_character


player1 = Character()
monster, backpack, player = get_locations()
print("Welcome to Computer Science Hell")

while True:
	moves = get_moves(player)
	
	print("You're currently in room {}".format(player)) 

	draw_map(player)

	print("You can move {}".format(moves)) 
	print("Enter [Q] to quit and [H] for help")

	move = raw_input("> ")
	move = move.upper()

	if move == 'Q':
		break

	if move == 'H':
		print("help stuff")
		continue

	if move in moves:
		player = move_player(player,move)
	else:
		print("Dude, you're literally up against a brick wall")
		continue

	if player == backpack:
		print("You found your backpack. You're a winner")
		break
	elif player == monster:
		battle(player1)
		#print("You were eaten by the evil robot")
		break