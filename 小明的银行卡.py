a = []
for i in input().split():
	a.append(int(i))
sum1,t,x,y,m = 0,0,0,0,0
for j in range(len(a)):
	if (j%2==0):
		sum1 += a[j]
	else :
		t = 2*a[j]
		x = t//10
		y = t%10
		sum1 = sum1+x+y
m = 10-(sum1%10)
a.append(m)
for k in range(len(a)):
	print(a[k],end='')
print('')