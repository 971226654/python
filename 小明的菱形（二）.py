n,c = input().split()
n = int(n)
def diamond(n,c):
	for i in range(1,n+2):
	    for j in range(1,n+2-i):
	        print('.',end='')
	    for j in range(i):
	        print("{}".format(c),end='')  
	    for j in range(i-1):
	    	print("{}".format(c),end='')
	    for j in range(1,n+2-i):
	    	print('.',end='')
	    print("")

	for i in range(n+2,n*2+2):
		for j in range(i-n-1):
			print('.',end='')
		for j in range(1,n*2-i+3):
			print("{}".format(c),end='')
		for j in range(1,n*2-i+2):
			print("{}".format(c),end='')
		for j in range(i-n-1):
			print('.',end='')
		print("")

diamond(n,c)