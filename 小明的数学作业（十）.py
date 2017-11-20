def change(quo):
	a = []
	while quo:
		mod = quo%2
		quo = quo//2
		a.append(mod)
	for i in range(len(a)-1,-1,-1):
		print(a[i],end='')
	return
decimal = int(input())
change(decimal)
print('')