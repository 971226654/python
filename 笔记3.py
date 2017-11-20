##n = eval(input())
##a = [True]*(n+1)
##for i in range (2,n):
##    for j in range(2,n//i+1):
##        a[i*j]= False
##count = 0
##for i in range(2,n+1):
##    if a[i]:
##        count+=1
##print(count)
##    
    
##a=[[1,2,3],[4,5,6],[7,8,9]]
##print(len(a),len(a[1]),sep=':')
##print(a[0],a[1],a[:1],sep=':')
##print(a[:0],a[:1],a[:2],sep=':')

'''
import random
score = [[0 for i in range (6)]for i in range(11)]
for i in range(10):
    for j in range(5):
        score[i][j] = random.randrange(60,100)
for i in range(10):
    s = 0
    for j in range(5):
        s+=score[i][j]
    score[i][5]=s/5
for j in range(6):
    s=0
    for i in range(10):
        s+=score[i][j]
    score[10][j]=s/10
print(score)
'''
'''
import random
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']
deck = []
for suit in SUITS:
    for rank in RANKS:                #按顺序输出牌
        card = rank +'of'+ suit
        deck +=[card]
random.shuffle(deck)
print(deck)


n = len(deck)
for i in range(n):
    r = random.randrange(i, n)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp
'''

import random
import sys

SUITS = ['club', 'diamond', 'heart', 'spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

n = int(input())

deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + '-' + suit
        deck += [card]

perm = [0] * 52

for i in range(52):
    perm[i] = i

for i in range(n):
    for i in range(5):
        r = random.randrange(i, 52)

        temp = deck[perm[r]]
        deck[perm[r]] = deck[perm[i]]
        deck[perm[i]] = temp

        print(str(deck[perm[i]]),end='')
        print(' ', end='')
    print()