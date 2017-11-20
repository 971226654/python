m,n,r = map(int,input().split())
a = [[0 for j in range(n)]for i in range(m)]
b = [[0 for j in range(r)]for i in range(n)]
c = [[0 for j in range(r)]for i in range(m)]

for i in range(m):
	for j in range(n):
		a[i][j] = i*100+j+1

for i in range(n):
	for j in range(r):
		b[i][j] = i*10+j+1

for i in range(m):
	for j in range(r):
		s = 0
		for k in range(n):
			s += a[i][k]*b[k][j]
		c[i][j] = s

print(a,b,c)