m,n = map(int,input().split())
a = [0 for i in range(m*n)]
b = [[0 for j in range(n)]for i in range(m)]

for i in range(m*n):
	a[i] = i

count = 0
for i in range(m):
	for j in range(n):
		b[i][j] = a[count]
		count += 1

print(a,b)