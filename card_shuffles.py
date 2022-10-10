import random

def set_up_deck():
	
	fresh_deck = []
	card_family = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
	card_value = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
	
	for i in range(len(card_family)):
		for j in range(len(card_value)):
			fresh_deck.append([card_family[i], card_value[j]])
	return fresh_deck	

def shuffle():
	deck = set_up_deck()
	for i in range(0, len(deck)-1):
		random_number = random.randint(0,len(deck)-1)
		if random_number != i:
			card_storage = deck[i]
			deck[i] = deck[random_number]
			deck[random_number] = card_storage
	return deck

def deal(number_of_cards):
	hand = []
	deck = shuffle()
	for i in range(0, number_of_cards):
		hand.append(deck.pop())
	return hand

	
print(deal(5))


					
