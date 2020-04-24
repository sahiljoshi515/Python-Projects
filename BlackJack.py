#Import statements and variable declarations

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True


#Class Definitions:-



class Card:

	def __init__(self,suit,rank):   #card onject has two attributes 
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' of ' + self.suit


class Deck:

	def __init__(self):
		self.deck = []  #start with an empty deck
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))   #build card objects 

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

	def __str__(self):
		deck_comp = ''    #start with an empty string
		for card in self.deck:
			deck_comp += '\n' + card.__str__
		return 'The deck contains' + deck_comp     


class Hand:

	def __init__(self):
		self.cards = []     #Just assign them to starting values
		self.value = 0
		self.aces = 0

	def add_Card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_For_Ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1



class Chips:

	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

#function definitions:-


def take_bet(chips):

	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet?'))
		except ValueError:
			print('Sorry, bet must be an integer')
		else:
			if chips.bet > chips.total:
				print('Sorry your bet cannot exceed the total {}'.format(chips.total))
			else:
				break


def hit(deck,hand):
	hand.add_Card(deck.deal())
	hand.adjust_For_Ace()


def hit_or_stand(deck,hand):
	global playing 

	while True:

		x = input('Would you like to hit or stand? Select h or s ')

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print('Player stands. Dealer is Playing')
			playing = False
		else:
			print('Sorry please try again')
			continue
		break


def show_some(player, dealer):
	print("\nDealer's Hand:")
	print(" <card hidden>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player,dealer):
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)


def player_wins(player,dealer,chips):
	print('Player Wins')
	chips.win_bet()

def player_busts(player,dealer,chips):
	print('Player Busts')
	chips.lose_bet()

def dealer_wins(player,dealer,chips):
	print('Dealer Wins')
	chips.lose_bet()

def dealer_busts(player,dealer,chips):
	print('Dealer Busts')
	chips.win_bet()

def push(player,dealer):
	print("Dealer and Player tie! It's a push")




#Game Play begins


while True:


	print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')


	deck = Deck()
	deck.shuffle()

    #add cards to player_hand and dealer_hand

	player_hand = Hand()
	player_hand.add_Card(deck.deal())
	player_hand.add_Card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_Card(deck.deal())
	dealer_hand.add_Card(deck.deal())


	player_chips = Chips()
	take_bet(player_chips)
	show_some(player_hand,dealer_hand)

	while playing:
		#prompt user to hit or stand	
		hit_or_stand(deck,player_hand)
		show_some(player_hand,dealer_hand)
		
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		show_all(player_hand, dealer_hand)

    			#test different scenarios

		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)

		else:
			push(player_hand, dealer_hand)

	print('\nPlayer winnings stand at {}'.format(player_chips.total))
	newGame = input('Want to play again?')
	if newGame[0].lower() == 'y':
		playing = True
		continue
	else:
		break
		
   		
















































