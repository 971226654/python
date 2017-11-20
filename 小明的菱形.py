import sys
n = eval(input())
for i in range(1,n+2):
    for j in range(1,n+2-i):
        print('.',end='')
    for j in range(i):
        print('*',end='')  
    for j in range(i-1):
    	print('*',end='')
    for j in range(1,n+2-i):
    	print('.',end='')
    print("")

for i in range(n+2,n*2+2):
	for j in range(i-n-1):
		print('.',end='')
	for j in range(1,n*2-i+3):
		print('*',end='')
	for j in range(1,n*2-i+2):
		print('*',end='')
	for j in range(i-n-1):
		print('.',end='')
	print("")
