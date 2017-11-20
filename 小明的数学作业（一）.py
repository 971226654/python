n,k = map(int,input().split())
sum = 0
if n>k:
	t = n
	n = k
	k = t
for i in range(n,k+1):
	sum = sum+i
print(sum)