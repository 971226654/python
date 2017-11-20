i = 0
while True:
	try:
		ab,ac,ad,bc,bd,cd = map(int,input().split())
		e = ab+bd
		f = ac+cd
		g = ab+bc+cd
		h = ac+bc+bd
		i = i+1
		if i==1001:
			break
		print("Case #{0}: {1}".format(i,min(ad,e,f,g,h)))
		
	except:
		break