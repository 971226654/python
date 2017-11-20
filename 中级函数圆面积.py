def findRadius(c):
	r = c / (2 * 3.1415926)
	return r
def findArea(r):
	s = 3.1415926 * r * r
	return s
while True:
	try:
		c = float(input())
		a = findArea(findRadius(c))
		print("{:.2f}".format(a))
	except:
		break