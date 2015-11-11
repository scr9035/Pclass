#!/usr/bin/env python
"""Scott Riggs scr9035
This program creates a standard deck of 52 cards.
The user is allowed to make any of the 52 cards
and add them to the deck. From the deck a hand
of cards can be constructed"""

from __future__ import print_function
import random

GET_SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]
GET_RANK = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Card(object):
    """This class creates a card instance with a suit and
    rank stored as a number. It also can determine the BlackJack value"""

    def __init__(self, suit=0, rank=2):
        """sets the Card instance to have a suit and rank. If not sepecified
        the card is set to the 2 of clubs, the lowest card value"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """returns the suit and rank of a Card instance in human
        readable format, i.e. 9 of Spades insted of (3,9)"""
        return '{} of {}'.format(GET_RANK[self.rank], GET_SUIT[self.suit])

    def value(self):
        """returns the BlackJack value of the card
        except for the card Ace, which only returns a 1"""
        if self.rank >= 10:
            return  10
        elif self.rank == 0:
            return ["Joker"]
        else:
            return self.rank


class Deck(object):
    """Creates a deck of cards each with a suit and rank.
    default decks starts with normal 52 card deck"""

    def __init__(self):
        """Creates a standard deck of 52 cards"""
        self.card_deck = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.card_deck.append(card)

    def __str__(self):
        """prints cards in the card deck"""
        card_names = []
        for card in self.card_deck:
            card_names.append(str(card))
        return '\n'.join(card_names)

    def add_card(self, card):
        """add a card to the deck"""
        self.card_deck.append(card)

    def remove_card(self, card):
        """remove a card from the deck."""
        self.card_deck.remove(card)

    def pop_card(self, i=-1):
        """removes and returns a card from the deck at index i.
        by default pops the last card"""
        return self.card_deck.pop(i)

    def shuffle(self):
        """randomizes the cards in card_deck"""
        random.shuffle(self.card_deck)

    def sort(self):
        """ascending orders cards in card_deck"""
        self.card_deck.sort()

    def move_cards(self, hand, num):
        """deals num cards to hand"""
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """create a hand of cards"""
    def __init__(self):
        """creates an empty hand"""
        self.card_deck = []

    def __str__(self):
        """calls __str__ from Card class
        puts cards in Hand into readable format"""
        card_hand_names = []
        for card in self.card_deck:
            card_hand_names.append(str(card))
        return ', '.join(card_hand_names)


    def size(self):
        """returns the number of cards in Hand"""
        return len(self.card_deck)
		