from __future__ import print_function
import random
import sys
from character import Character
from monster import Evil_robot, Doc_student




CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


class Game:
    """handles game layout,movement and monster character interaction"""
    def setup(self):
        """Assign a tuple cell to player, monster, rat_trap, and backpack.
           creates an instance of 3 Evil_robots, 1 Doc_student and 1 Character"""
        self.player = Character()
        self.evil_robot1 = Evil_robot()
        self.evil_robot2 = Evil_robot()
        self.evil_robot3 = Evil_robot()
        self.doc_student1 = Doc_student()
        

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
        print("Your position on the map is denoted by an X.\n To move press N, S, E, W. \n Type [L]ife to see players hit points")

    def show_health(self,player):
        """Prints the players current HP"""
        print("You have {} HP".format(self.player.hit_points))


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
        print(' _ _ _ _ _')
        tile = '|{}'

        for idx, cell in enumerate(CELLS):
            if idx in [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23]:
                if cell == player:
                    print(tile.format("X"), end='')
                else:
                    print(tile.format("_"), end='')
            else:
                if cell == player:
                    print(tile.format('X|'))
                else:
                    print(tile.format('_|'))

    def player_dies(self, monster):
        """When players HP >=0 exits the game."""
        print(self.player)
        if self.player.hit_points <= 0:
            print("You have been killed by {}".format(monster))
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
                print('\033[1;31m{} attacks!\033[1;m \n'.format(monster))

                if raw_input('Block? (Y/N): \n').lower() == 'y':
                    print("You attempted to block!")
                    if self.player.block():
                        print("You blocked {}'s attack! \n".format(monster))
                    else:
                        if self.monster.attack_strength > self.player.attack_defense:   
                            hp_lost = random.randint(1,6) + self.monster.attack_strength - self.player.attack_defense
                            self.player.hit_points -= hp_lost
                        else:
                            hp_lost = 1
                            self.player.hit_points -= hp_lost

                        print("\033[1;31mYou failed to block {}'s attack. Lost {} HP\033[1;m".format(monster, hp_lost))
                        self.player_dies(monster)
                        

                elif self.player.dodge():
                    print('You dodged the attack! \n')
                else:
                    if self.monster.attack_strength > self.player.attack_defense:   
                            hp_lost = random.randint(1,6) + self.monster.attack_strength - self.player.attack_defense
                            self.player.hit_points -= hp_lost
                    else:
                        hp_lost = 1
                        self.player.hit_points -= hp_lost
                    print('\033[1;31m{} hit you! Lost {} HP\033[1;m \n'.format(monster, hp_lost))
                    self.player_dies(monster)

            else:
                print('{} does not attack. \n'.format(monster))

    def player_turn(self, monster):
            """Players attack phase. Monster will try to dodge.
               If dodge successful no damage to monster. Otherwise
               monster takes damage = random.randint(1,6) + 
               self.player.attack_strength - self.monster.attack_defense.
               Unless of course self.player.attack_strength < self.monster.attack_defense
               the monster only takes 1 HP in damage"""
            if self.player.attack():
                if monster.dodge():
                    print('{} dodged your attack.'.format(monster))
                else:

                    if self.player.attack_strength > self.monster.attack_defense:   
                            hp_lost = random.randint(1,6) + self.player.attack_strength - self.monster.attack_defense
                            self.monster.hit_points -= hp_lost
                    else:
                        hp_lost = 1
                        self.monster.hit_points -= hp_lost

                    print('\033[1;34mYou hit {} for {} HP.\033[1;m'.format(
                        monster,
                        self.player.attack_strength
                    ))
            else:
                print('Your attack misses.')

    def cleanup(self):
        """Cleans up the battle. Player gains xp for killing monsters. Add xp here
           Sets the monster location to be off the grid (removes monster from game)"""
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print('\033[1;34mYou killed {}!\033[1;m \n'.format(self.monster))
            print(self.player)
            

            
            self.monster.location = 0

    def __init__(self):
        """First runs character() class to have player build a character
           Runs setup to build the cells and populate them with character, monsters, backpack, and rat_trap.
           Loop has player move through grids and interact with instances in the cells.
        """
        self.setup()

        print("  ")
        print("Welcome to CS Hell.\n\n",
        "You've lost your backpack somewhere in the 'Love'-ly building basement.\n",
        "You must find it so you can submit your assignment.\n", 
        "Watch out though, rogue machine learned bots, bitter doctoral students,\n",
        "and untenured prof's roam these halls!\n")

        print("Your stats: {} \n".format(self.player))
        
        player = self.player.location
        

        while True:

            moves = self.get_moves(player)

            self.draw_map(player)
            print("\nYou current location is {} \n".format(player))

            for monster in self.monsters:
                self.monster = monster
                if player == self.monster.location:
                    print("\n\033[1;31mThere is a {}, HP: {}, XP: {}!\033[1;m".format(self.monster,
                                                                                      self.monster.hit_points,
                                                                                      self.monster.experience
                                                                                      ))
                    print("{}".format(monster.battlecry()))

                    
                    if player == self.backpack:
                        print("\033[1;33mThere's the backpack! It is guarded by a {}.\033[1;m".format(monster))

                    # Combat loop. Run monster and player turns until monster HP reaches 0
                    # or player successfully runs away.
                    if player == self.rat_trap:
                        print("You found the Untenured Prof (rat_trap)! You die")
                        sys.exit()

                    run = False

                    while self.monster.hit_points > 0:
                        if run is True:
                            print("RUN AWAY, RUN AWAY!")
                            player = self.move_player(player, random.choice(self.get_moves(player)))
                            moves = self.get_moves(player)
                            self.draw_map(player)
                            break

                        print("_" * 50 + "\n")
                        self.monster_turn(self.monster)
                        move = raw_input("Choose your action: [A]ttack, [D]rink, R[u]n away, or [Q]uit? \n").lower()

                        if move == 'a':
                            print('You attack {}!'.format(monster))
                            self.player_turn(self.monster)
                        elif move == 'd':
                            self.player.rest()
                            print("You recover {} HP. \n{} \n".format(self.player.potion, self.player))
                        elif move == 'u':
                            if self.player.run():
                                run = True
                            else:
                                print("You could not run away.")

                        elif move == 'q':
                            sys.exit()
                        else:
                            print("Invalid move.")
                            continue

                    # After combat run cleanup. Cleanup will run if monster has been killed.

                    self.cleanup()

            if player == self.backpack:
                print("\033[1;33mThere's the backpack!\033[1;m")
                if player not in self.monsters:
                    if raw_input("Do you open your backpack? (Y/N): ").lower() == "y":
                        print("You have your laptop and submit your CS homework!")
                        sys.exit()

            print("You can move {}".format(moves))
            print("Enter [Q]uit to end game, [H]elp to get help, [L]ife for player hit points.")
            move = raw_input("> ")
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
                print("Move again.\n")
                continue

Game()