n = [[0 for j in range(4)]for i in range(4)]
for i in range(4):
	n[i] = input().split()
for j in range(4):
	for i in range(4):
		print("{} ".format(n[i][j]),end='')
	print('')