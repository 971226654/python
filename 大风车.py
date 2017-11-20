while True:
    try:
    	n,a,b,c,d,e = map(int,input().split())
    	if n < 17:
    		sum = 0.5*(8*a+16*b+18*c+24*d+28*e)
    	else :
    		sum = 8*a+16*b+18*c+24*d+28*e
    	sum = int(sum)
    	print(sum)
    except:
    	break