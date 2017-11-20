while True:
	try:
		n,m,k = map(int,input().split())
		a = (n/(n+m+k))*(m/(n+m+k))
		b = (n/(n+m+k))*(k/(n+m+k))
		c = (m/(n+m+k))*(k/(n+m+k))
		ans = (a+b+c)*2
		print("{:.2f}".format(ans))
	except:
		break