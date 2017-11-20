def sum(a):
	sum = 0
	for i in a:
		sum += i
	return sum
n = int(input())
a = []
for i in input().split():
	a.append(int(i))
print(sum(a))
