n = int(input())
a = [[0 for j in range(n)]for i in range(n)]
if n%2==0:
	for i in range(n//2):
		for j in range(n//2):
			a[i][j] = j+1 if j<i else i+1
			a[i][n-1-j] = a[i][j]
			a[n-1-i][j] = a[i][j]
			a[n-1-i][n-1-j] = a[i][j]
		
else:
	for i in range(n//2+1):
		for j in range(n//2+1):
			a[i][j] = j+1 if j<i else i+1
			a[i][n-1-j] = a[i][j]
			a[n-1-i][j] = a[i][j]
			a[n-1-i][n-1-j] = a[i][j]
			
for i in range(n):
	for j in range(n):
		print("{:>3}".format(int(a[i][j])),end='')
	print('')