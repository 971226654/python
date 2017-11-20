a,b,c = map(int,input().split())
if a>b:
	t = a
	a = b
	b = t
for i in range(a,b+1):
	if i%c==0:
		print("{},".format(i),end='')
print("")