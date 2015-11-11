'''Scott Riggs scr9035. Program creates a RPG with multiple
   character class, monsters, potions, and other goodies.
   the RPG takes place on a 5 x 5 grid''' 

from __future__ import print_function
import SocketServer
import threading
import random
import sys
from character3 import Character
from monster3 import Evil_robot, Doc_student




CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        g = Game(self.request)



class Game():
    """handles game layout,movement and monster character interaction"""
    def setup(self):
        """Assign a tuple cell to player, monster, rat_trap, and backpack.
           creates an instance of 3 Evil_robots, 1 Doc_student and 1 Character"""
        self.player = Character(self.c)
        self.evil_robot1 = Evil_robot(self.c)
        self.evil_robot2 = Evil_robot(self.c)
        self.evil_robot3 = Evil_robot(self.c)
        self.doc_student1 = Doc_student(self.c)
        

        self.backpack = random.choice(CELLS)
        self.player.location = random.choice(CELLS)
        self.rat_trap = random.choice(CELLS)

        self.monsters = [
            self.evil_robot1,
            self.evil_robot2,
            self.evil_robot3,
            self.doc_student1
        ]

        for item in self.monsters:
            item.location = random.choice(CELLS)

    def show_help(self):
        """Prints commands available to the user."""
        self.c.send("\033[0;36m Your position on the map is denoted by an X.\n To move press N, S, E, W. \n Type [L]ife to see your hit points\033[0;m \n")
        

    def show_health(self,player):
        """Prints the players current HP"""
        self.c.send("\033[0;32mYou have {} HP\033[0;m \n".format(self.player.hit_points))


    def get_moves(self, player):
        """Checks to see if player is at the edge/corner of the grid. 
           If at edge of grid, removes the edge value as a movement option"""
        moves = ['N', 'S', 'E', 'W']

        if player[1] == 0:
            moves.remove('W')
        if player[1] == 4:
            moves.remove('E')
        if player[0] == 0:
            moves.remove('N')
        if player[0] == 4:
            moves.remove('S')

        return moves

    def move_player(self, player, move):
        """Moves player N,S,E,W on the grid"""
        x, y = player

        if move == 'W':
            y -= 1
        elif move == 'E':
            y += 1
        elif move == 'N':
            x -= 1
        elif move == 'S':
            x += 1
        return x, y

    def draw_map(self, player):
        """Makes a map of the cells, and gives the players location as an X"""
        self.c.send(' _ _ _ _ _')
        tile = '|{}'

        for idx, cell in enumerate(CELLS):
            if idx in [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23]:
                if cell == player:
                    self.c.send(tile.format("X"),) #end='')) 
                else:
                    self.c.send(tile.format("_"),) #end=''))
            else:
                if cell == player:
                    self.c.send(tile.format('X|'))
                else:
                    self.c.send(tile.format('_|'))

    def player_dies(self, monster):
        """When players HP >=0 exits the game."""
        #player = self.player
        #self.c.send(player)
        if self.player.hit_points <= 0:
            self.c.send("You have been killed by {} \n".format(monster))
            sys.exit()

    def monster_turn(self, monster):
            """ Start monsters turn. Player can choose dodge. 
            If player chooses not to dodge, block is an option
            If player successfully blocks or dodges, no damage.
            Otherwise player is hit for random.randint(1,6) + 
            self.monster.attack_strength - self.player.attack_defense damage.
            If self.monster.attack_strength < self.player.attack_defense hp lost is 1 
            rather than player gaining HP during a fight
            """
            if monster.attack():
                self.c.send('\033[1;31m{} attacks!\033[1;m \n'.format(monster))

                self.c.send('Block? (Y/N): ')
                does_player_block = self.c.recv(20)[0]
                does_player_block = does_player_block.lower()

                if does_player_block == 'y':
                    self.c.send("You attempted to block! \n")
                    if self.player.block():
                        self.c.send("You blocked {}'s attack! \n".format(monster))
                    else:
                        if self.monster.attack_strength > self.player.attack_defense:   
                            hp_lost = random.randint(1,6) + self.monster.attack_strength - self.player.attack_defense
                            self.player.hit_points -= hp_lost
                        else:
                            hp_lost = 1
                            self.player.hit_points -= hp_lost

                        self.c.send("\033[1;31mYou failed to block {}'s attack. Lost {} HP\033[1;m \n".format(monster, hp_lost))
                        self.player_dies(monster)
                        

                elif self.player.dodge():
                    self.c.send('You dodged the attack! \n')
                else:
                    if self.monster.attack_strength > self.player.attack_defense:   
                            hp_lost = random.randint(1,6) + self.monster.attack_strength - self.player.attack_defense
                            self.player.hit_points -= hp_lost
                    else:
                        hp_lost = 1
                        self.player.hit_points -= hp_lost
                    self.c.send('\033[1;31m{} hit you! Lost {} HP\033[1;m \n'.format(monster, hp_lost))
                    self.player_dies(monster)

            else:
                self.c.send('{} does not attack. \n'.format(monster))

    def player_turn(self, monster):
            """Players attack phase. Monster will try to dodge.
               If dodge successful no damage to monster. Otherwise
               monster takes damage = random.randint(1,6) + 
               self.player.attack_strength - self.monster.attack_defense.
               Unless of course self.player.attack_strength < self.monster.attack_defense
               the monster only takes 1 HP in damage"""
            if self.player.attack():
                if monster.dodge():
                    self.c.send('{} dodged your attack. \n'.format(monster))
                else:

                    if self.player.attack_strength > self.monster.attack_defense:   
                            hp_lost = random.randint(1,6) + self.player.attack_strength - self.monster.attack_defense
                            self.monster.hit_points -= hp_lost
                    else:
                        hp_lost = 1
                        self.monster.hit_points -= hp_lost

                    self.c.send('\033[1;34mYou hit {} for {} HP.\033[1;m \n'.format(
                        monster,
                        self.player.attack_strength
                    ))
            else:
                self.c.send('Your attack misses. \n')

    def cleanup(self):
        """Cleans up the battle. Player gains xp for killing monsters. Add xp here
           Sets the monster location to be off the grid (removes monster from game)"""
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            self.c.send('\033[1;34mYou killed {}!\033[1;m \n'.format(self.monster))
            self.c.send('{} \n'.format(self.player))
            

            
            self.monster.location = 0

    def __init__(self, c):
        """First runs character() class to have player build a character
           Runs setup to build the cells and populate them with character, monsters, backpack, and rat_trap.
           Loop has player move through grids and interact with instances in the cells.
        """
        self.c = c
        self.setup()

        self.c.send("  ")
        self.c.send("\n \033[1;31mWelcome to CS Hell.\033[1;m \n\n")
        self.c.send("You've lost your backpack somewhere in the 'Love'-ly building basement.\n")
        self.c.send("You must find it so you can submit your assignment.\n")
        self.c.send("Watch out though, rogue machined learned bots, bitter doctoral students,\n")
        self.c.send("and untenured prof's roam these halls!\n")

        self.c.send("Your stats: {}".format(self.player))
        
        player = self.player.location
        

        while True:

            moves = self.get_moves(player)

            #self.draw_map(player)
            self.c.send("\nYour current location is {} \n".format(player))
            #self.c.send("\n rat trap location is {} \n".format(self.rat_trap))

            for monster in self.monsters:
                self.monster = monster
                if player == self.monster.location:
                    self.c.send("\n\033[1;31mThere is a {}, HP: {}, XP: {}!\033[1;m \n".format(self.monster,
                                                                                      self.monster.hit_points,
                                                                                      self.monster.experience
                                                                                      ))
                    self.c.send("{} \n".format(monster.battlecry()))

                    
                    if player == self.backpack:
                        self.c.send("\033[1;33mThere's the backpack! It is guarded by a {}.\033[1;m \n".format(monster))

                    # Combat loop. Run monster and player turns until monster HP reaches 0
                    # or player successfully runs away.
                    if player == self.rat_trap:
                        self.c.send("You found the Untenured Prof (rat_trap)! You die \n")
                        sys.exit()

                    run = False

                    while self.monster.hit_points > 0:
                        if run is True:
                            self.c.send("RUN AWAY, RUN AWAY! \n")
                            player = self.move_player(player, random.choice(self.get_moves(player)))
                            moves = self.get_moves(player)
                            self.draw_map(player)
                            break

                        self.c.send("_" * 50 + "\n")
                        self.monster_turn(self.monster)
                        move = self.c.send("Watcha gonna do: [A]ttack, [D]rink, R[u]n away, or [Q]uit? ")
                        move = self.c.recv(20)[0]
                        move = move.lower()

                        if move == 'a':
                            self.c.send('You attack {}! \n'.format(monster))
                            self.player_turn(self.monster)
                        elif move == 'd':
                            self.player.rest()
                            self.c.send("You recover {} HP. \n{} \n".format(self.player.potion, self.player))
                        elif move == 'u':
                            if self.player.run():
                                run = True
                            else:
                                self.c.send("You could not run away. \n")

                        elif move == 'q':
                            self.c.send("You have given up on life. \n") 
                            self.c.send("You notice yourself turning into yet another doctoral student \n") 
                            self.c.send("destined to roam the halls in search fo free food ")
                            sys.exit()
                        else:
                            self.c.send("Invalid move. \n")
                            continue

                    # After combat run cleanup. Cleanup will run if monster has been killed.

                    self.cleanup()

            if player == self.backpack:
                self.c.send("\033[1;33mThere's the backpack!\033[1;m \n")
                if player not in self.monsters:
                    self.c.send("You have your laptop and submit your CS homework! \n")
                    sys.exit()

            if player == self.rat_trap:
                    self.c.send("You found the Untenured Prof (rat_trap)! You die \n")
                    sys.exit()

            self.c.send("You can move {} \n".format(moves))
            self.c.send("Enter [Q]uit to end game, [H]elp to get help, [L]ife for player hit points. \n")
            self.c.send("> ")
            move = self.c.recv(20)[0]
            move = move.upper()
            if move == 'H':
                self.show_help()
            if move == 'L':
                self.show_health(player)
            if move == 'Q':
                sys.exit()
            if move in moves:
                player = self.move_player(player, move)
            else:
                self.c.send("Move again.\n")
                continue

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = 'localhost', 9003
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

