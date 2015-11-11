# Definition of Card, Deck and Hand classes based on 
# originals created by Allen B. Downey. 

import random	

class Card():

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    values = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.fname = self.filename()

    def __str__(self):
        """Returns a human-readable string representation."""
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def value(self):
    	"""Returns the face value of the card"""
    	return Card.values[self.rank]

    def filename(self):
        f = Card.suit_names[self.suit].rstrip('s').lower() + '_'
        if Card.rank_names[self.rank] in ["Ace", "Jack", "Queen", "King"]:
            f = f + Card.rank_names[self.rank][0]
        else:
            f = f + Card.rank_names[self.rank]
        f = "cards/" + f + ".png"
        return f


class Deck():
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        """ Initialize deck of cards """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        fname_list = []
        for i in range(num):
            c = self.pop_card()
            #print "appending ", c
            fname_list.append(c.fname)
            hand.add_card(c)

        return fname_list

class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self):
        """ Initializa hand to be empty """
        self.cards = []

    def __str__(self, start=0):
        """ return string representation of 
        cards in hand, starting with card index start """
    	s = ''
    	for i in range(start, len(self.cards)):
    		s = s + '  ' + self.cards[i].__str__()
    	return s

    def values(self):
        """ Returns a list of the possible 
        values of the entire hand. 

        For example, two Aces could be a value
        of 2, 12, or 22. 
        """
    	val = 0
    	aces = 0
    	for i in self.cards:
    		val = val + i.value()
    		if i.value() == 1:
    			aces = aces + 1

        """ Append lowest possible value to value
        list and add 10 for every possible high ace """
    	value_list = [val]
    	for a in range(aces):
    		# Add aces high values
    		value_list.append(val+10)
    	return value_list

    def size(self):
    	return len(self.cards)