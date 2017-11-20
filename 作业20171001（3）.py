'''
while True :
	a,b,c = input().split()
	
	print(min(a,b,c))
'''
while True:
	try:
		a,b,c = input().split()
		a = int(a)
		b = int(b)
		c = int(c)
		if a < b and a < c:
			print(a)
		elif a == b and a < c :
			print(a)
		elif a == c and a < b :
			print(a)
		elif b == c and b < a :
			print(b)
		elif a == b == c:
			print(a)
		elif b < a and b < c:
			print(b)
		else:
			print(c)

	except:
		break