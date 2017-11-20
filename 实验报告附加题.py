import random
SUITS = ['club','diamond','heart','spade']
RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
n = eval(input())

deck = []
for suit in SUITS:
	for rank in RANKS:
		card = rank + '-' + suit
		deck += [card]

a = []
for i in range(52):
	a += [i]

for i in range(n):
	for j in range(5):
		random.shuffle(deck)
		print("{} ".format(str(deck[a[i]])),end='')
	print('')