n = [[0 for j in range(4)]for i in range(3)]
for i in range(3):
	n[i] = input().split()
for j in range(4):
	for i in range(3):
		print("{} ".format(n[i][j]),end='')
	print('')	