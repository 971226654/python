while True:
	try:
		n = int(input())
		a = [0 for i in range(n)]
		for i in range(n):
			a[i] = input().split()
		for i in a:
			count = 0
			b = a[i]
			for j in a:
				if a[j]==b:
					count += 1
			if count >= n/2:
				c = 1
		if c == 1:
			print("YES")
		else :
			print("NO")
	except:
		break	