n = int(input())
b,c,d = 0,0,1
for i in range(n):
	if i==0:
		a = 0
	elif i==1:
		a = 1
	else:
		e = c+d
		c = d
		d = e
		a = e	
	b = b+1
	print("{},".format(a),end='')
	if b == 5:
		print("")
print("")