# 3 classes (deck cards player) 
# shuffle method
# draw()
# reset()
import random
class Cards(object):
	def __init__(self, suits, numbers, values):
		self.suits = suits
		self.numbers = numbers
		self.values = values
	def __str__(self):
		return "Suits:{} Numbers:{} Values:{}".format(self.suits, self.numbers, self.values)

class Deck(object):
	def __init__(self):
		self.cards = []

	def create(self): 
		suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
		numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
		for suit in suits: 
			for number in numbers: 
				values = None
				if number == "King" or number == "Jack" or number  == "Queen": 
					values = 10
				elif number == 'Ace':
					values = 11 #add 1 later 
				else: 
					values = number
				self.cards.append(Cards(suit, number, values))
	def shuffle(self):
		for x in range(0,51):
			temp = self.cards[x]
			rand = random.randint(0,51)
			self.cards[x] = self.cards[rand]
			self.cards[rand] = temp

	def reset(self, player, dealer):
		player.hand = []
		dealer.hand = []
		self.cards = []
		# player and dealer's hand is emptied 
		# self.cards is emptied again

	def deal(self, player, dealer):
		for i in range(0,4):
			hand = self.cards.pop(0)
			if i<2: 
				player.hand.append(hand)
			else: 
				dealer.hand.append(hand)
		player.add()
		dealer.add()
		print "\nYou drew {} of {} and {} of {}".format(player.hand[0].numbers, player.hand[0].suits, player.hand[1].numbers, player.hand[1].suits)



class Player(object):
	def __init__(self, name, chips, bet):
		self.hand = []
		self.sum = 0
		self.name = name
		self.bet = bet
		self.chips = chips
	def hit(self, deck):
		# append from the deck 
		# add values in list	
		# if statements to check if it's over 21 
		# check Ace (1 or 11). Default to 11, but if it goes over 21 than 1 
		hand1 = deck.cards.pop(0)
		self.hand.append(hand1)
		hand_sum = self.add()
		print "\n{} drew {} of {}".format(self.name, hand1.numbers, hand1.suits)  
		for card in self.hand: 
			if card.numbers == "Ace" and self.sum>21:
				self.sum-=10
				print "Whoops almost busted! We changed your Ace to 1."
	def stay(self):
		pass 
	def add(self):
		self.sum = 0
		for i in self.hand: # not taking into consideration of Ace
			self.sum+=i.values

		return self.sum

class Dealer(Player):
	def __init__(self):
		super(Dealer, self).__init__(name='~Ray the Dealer~', chips=None, bet=None)
	def hit(self,deck):
		hand1 = deck.cards.pop(0)
		self.hand.append(hand1)
		hand_sum = self.add()
		print
		for card in self.hand: 
			if card.numbers == "Ace" and self.sum>21:
				self.sum-=10



		
# myDeck = Deck()
# myDeck.create()
# myDeck.shuffle()

# player1 = Player()
# player2 = Player()
# myDeck.deal(player1,player2)
# print player1.sum
# player1.hit(myDeck)
# print player1.sum





		


