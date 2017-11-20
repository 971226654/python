a,b,c = map(int,input().split())
def triangle(a,b,c):
	if a+b>c and a+c>b and b+c>a:
		print("YES")
	else :
		print("NO")
	return
triangle(a,b,c)