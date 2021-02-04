from random import shuffle

class Card():

	def __init__(self,cards):
		self.cards = cards
	
	def deal(self):
		shuffle(self.cards)
		card = deck.cards.pop()
		return card
	
class Computer():

	def __init__(self,cards):
		self.cards = cards

	def final_count(self):
		return sum(self.cards)

	def count(self,card):
		for card in self.cards:
			if card <= 11:
				if sum(self.cards) <= 21:
					return sum(self.cards)
				elif sum(self.cards) > 21 and (11 in self.cards):
					return sum(self.cards)-10 
			print(self)

	def ace_test(self):
		if str(self.cards[0]) == "Ace":
			if (11 + self.cards[1]) > 21:
				self.cards[0] = 1
			else:
				self.cards[0] = 11
		if len(self.cards) > 1: 
			for card in self.cards:
				if str(card) == 'Ace':
					if 11 + self.cards[0] > 21:
						self.cards[-1] = 1
					else:
						self.cards[-1] = 11

	def hit(self,card):
		self.cards.append(card)

	def __str__(self):
		count = sum(self.cards)
		return f'House Card Count: {str(count)}.'


class Player():

	def __init__(self,bankroll,cards):
		self.bankroll = bankroll
		self.cards = cards

	def winnings(self,bet,win):
		if win == "Player Wins":
			self.bankroll = self.bankroll + amount
			print('Player Wins')
		elif win == "House Wins":
			self.bankroll = self.bankroll - amount
			print('House Wins')
		else:
			print('Draw')


	
	def final_count(self):
		return sum(self.cards)

	def count(self,card):
		for card in self.cards:
			if card <= 11:
				if sum(self.cards) <= 21:
					return sum(self.cards)
				elif sum(self.cards) > 21 and (11 in self.cards):
					return sum(self.cards)-10 

	def ace_test(self):
		lst = self.cards
		for index, card in enumerate(lst):
			if str(card) == 'Ace':
				while True:
					try:
						value = int(input('Value 1 or 11: '))
					except:
						print("Invalid Input")
						continue
					else:
						if value == 1 or value == 11:
							self.cards[index] = value
							break
						else:
							print('Value must be 1 or 11')

	def hit(self,card):
		self.cards.append(card)	

	def __str__(self):
		count = sum(self.cards)
		return f'Player Card Count: {str(count)}\n Player Bankroll: {self.bankroll}.'



deck_cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
	'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
	'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
	'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = Card(deck_cards)
player = Player(100,[deck.deal(),deck.deal()])
computer = Computer([deck.deal()])

def win_check(player,computer):
	if computer.final_count() <=21:
		if player.final_count() <= 21:
			if player.final_count() > computer.final_count():
				return "Player Wins"
			elif player.final_count() == computer.final_count():
				return "Draw"
			else:
				return "House Wins"
		else:
			return "House Wins"
	else:
		return "Player Wins"

def bet():
	while True:
		try:
			amount = int(input('Select Bet Amount: '))
		except:
			print("Invalid Input")
			continue
		else:
			if player.bankroll < amount:
				print('You do not have a sufficient amount')
				continue
			else:
				return amount
				break

amount = bet()
while True:
	player.ace_test()
	if player.final_count() > 21:
		print("BUST")
		player.bankroll = player.bankroll - amount
		response = input('Play again?: ').lower()
		while response != "yes" and response != 'no':
			response = input('Play again?: ').lower()
		if response == 'no':
			break
		else:
			deck = Card(deck_cards)
			player = Player(player.bankroll,[deck.deal(),deck.deal()])
			computer = Computer([deck.deal()])
			print(f'Player bankroll is: {player.bankroll}')
			amount = bet()
			continue
	print(player.final_count())
	response = input('Hit or Stay?: ').lower()
	while response != 'hit' and response != 'stay':
		response = input('Hit or Stay?: ').lower()
	if response  == 'hit':
		player.hit(deck.deal())
	else:
		print(computer.cards)
		computer.ace_test()
		computer.hit(deck.deal())
		computer.ace_test()
		print(computer)
		while computer.final_count() <= 16:
			computer.hit(deck.deal())
			computer.ace_test()
		if computer.final_count() < player.final_count() and computer.final_count() < 17:
			computer.hit(deck.deal())
			computer.ace_test()
		win_check(player,computer)
		player.winnings(amount,win_check(player,computer))
		print(computer)
		print(player)
		response = input('Play again?: ').lower()
		while response != "yes" and response != 'no':
			response = input('Play again?: ').lower()
		if response == 'no':
			break
		else:
			amount = bet()
			deck = Card(deck_cards)
			player = Player(player.bankroll,[deck.deal(),deck.deal()])
			computer = Computer([deck.deal()])
			continue
		

