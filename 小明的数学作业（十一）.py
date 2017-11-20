year = int(input())
def leapyear(n):
	if (n%4==0 and n%100!=0) or (n%400==0):
		print("YES")
	else :
		print("NO")
	return
leapyear(year)