from __future__ import print_function
import random

CELLS = [(0,0),(0,1),(0,2),(0,3),(0,4),
		 (1,0),(1,1),(1,2),(1,3),(1,4),
		 (2,0),(2,1),(2,2),(2,3),(2,4),
		 (3,0),(3,1),(3,2),(3,3),(3,4),
		 (4,0),(4,1),(4,2),(4,3),(4,4)]


def get_locations():
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	if monster == door or monster == start or door == start:
		return get_locations()

	return monster, door, start
	

def move_player(player,move):
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

def get_moves(player):
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

monster, door, player = get_locations()
print("Welcome to Computer Science Hell")

while True:
	moves = get_moves(player)
	
	print("You're currently in room {}".format(player)) 

	draw_map(player)

	print("You can move {}".format(moves)) 
	print("Enter QUIT to show the world you're a loser")

	move = raw_input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	if move in moves:
		player = move_player(player,move)
	else:
		print("Dude, that's like a wall and shit")
		continue

	if player == door:
		print("You escaped")
		break
	elif player == monster:
		print("You were eaten by the evil robot")
		break

	#if good move, change player position
	#if its a bad move, don't change anything
	#if the new player position is the door, they win
	#if the new player poistion is a monster, they lose