while True:
	try:
		m,n = map(int,input().split())
		count = 0
		for i in range(m,n+1):
			if (i%3==2 and i%5==3 and i%7==2):
				print("{0: >7}".format(i),end='')
				count += 1
				if(count%10==0):
					print("")
		print("")
	except:
		break