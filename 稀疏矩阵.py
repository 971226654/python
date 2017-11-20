n = int(input())
a = [[0 for j in range(n)]for i in range(n)]
for i in range(n):
	a[i][i] = i+1
	a[i][n-1-i] = n-i

for i in range(n):
	for j in range(n):	
		print("{:>3}".format(int(a[i][j])),end='')
	print('')