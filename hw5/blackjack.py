from card import *

class BlackjackGame():
	def __init__(self):
		''' Initialize games played and 
		games won to zero, and start a brand
		new game '''
		self.gamesPlayed = 0
		self.gamesWon = 0
		self.start_new_game()

	def start_new_game(self):
		''' Create hands for player and dealer. Create
		and shuffle deck, then deal 2 cards to dealer 
		and 1 card to the player. 
		Enter the game playing phase.'''
		self.dealer_hand = Hand()
		self.player_hand = Hand()
		self.deck = Deck()
		self.deck.shuffle()
		self.player_cards = self.deck.move_cards(self.player_hand, 1)
		self.dealer_cards = self.deck.move_cards(self.dealer_hand, 2)
		self.play_game()

	def play_game(self):
		''' Deal a single card to the player. 
		Check to see if an automatic end condition
		was encountered. If so, modify game counter
		and win counter accordingly. '''
		for i in self.deck.move_cards(self.player_hand, 1):
			self.player_cards.append(i)
		f = self.check_end()
		if f:      
			self.gamesPlayed = self.gamesPlayed + 1 
			if f == 1:   
				self.gamesWon = self.gamesWon + 1
				return 1
			return 0
		return None

	def stay_game(self):
		''' Deal cards to dealer until their 
		highest possible hand value is 17 or 
		greater. Increment the game counter and
		check for the winner. Increment the 
		win counter if necessary. '''
		d_hand_value = self.dealer_hand.values()
		while d_hand_value[-1] < 17:
			for i in self.deck.move_cards(self.dealer_hand, 1):
				self.dealer_cards.append(i)
			d_hand_value = self.dealer_hand.values()	
			

		self.gamesPlayed = self.gamesPlayed + 1
		f = self.check_end()
		if f:             
			if f == 1:    
				self.gamesWon = self.gamesWon + 1
				return 1
		elif self.check_winner() == 1:
			self.gamesWon = self.gamesWon + 1
			return 1
		return 0

	def check_winner(self): 
		''' Compares the greatest possible hand value 
		of the dealer and player that doesn't exceed 21.
		Whichever side has the higher hand value wins. 
		If there is a tie, the dealer wins by default. '''
		dealer_max_val = 0
		player_max_val = 0
		for v in self.dealer_hand.values():
			if v > dealer_max_val and v <= 21:
				dealer_max_val = v

		for v in self.player_hand.values():
			if v > player_max_val and v <= 21:
				player_max_val = v

		if dealer_max_val > player_max_val:
			return 0
		elif player_max_val > dealer_max_val:
			return 1
		else:
			return 0

	def check_end(self):
		''' Check for automatic win conditions: 
		when a player hits to reach or exceed 21
		or when the dealer is dealt a 21 at the
		start of the game. '''
		d_values = self.dealer_hand.values()
		p_values = self.player_hand.values()

		if(d_values[0] == 21 or p_values[0] > 21):
			return 2
		elif(d_values[0] > 21 or p_values[0] == 21):
			return 1
		else:
			return 0