'''
import random
n = int(input())
win,draw,lose = 0,0,0
for i in range(n):
    a = random.randint(1,6)
    b = random.randint(1,6)
    if a>b:
        win = win+1
    elif a==b:
        draw = draw+1
    else:
        lose = lose+1
print("{}:{}:{}".format(win,draw,lose))
'''
'''
import sys
n = eval(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i%j==0)or(j%i==0):
            print('* ',end='')
        else:
            print('  ',end='')
    print(i)
'''


import sys
n = eval(input())
##for i in range(n):
##    for j in range (i):
##        print('* ',end='')
for i in range(n):
    print('*'*i)
print("")


'''
import sys
n = eval(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print('  ',end='')
    for j in range(i):
        print('* ',end='')
    print('')
'''

'''
n,k = map(int,input().split())
s = 0
if n>k:
    t = n
    n = k
    k = t
for i in range(n,k+1):
    s = s+i
    
print(s)
'''



















        
        
        
