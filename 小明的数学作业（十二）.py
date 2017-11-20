a,b,c = map(int,input().split())
def findMAX(n,m,k):
	if n>=m and n>=k :
		max = n
	elif m>=n and m>=k :
		max = m
	else :
		max = k
	return max
print(findMAX(a,b,c))