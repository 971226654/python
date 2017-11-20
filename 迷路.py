while True:
	try:
		s,e = map(str,input().split())
		n = map(int,input().split())
		if 0 <= n <= 1500:
			n = n%4
		if s == '^' and e == '>':
			if n == 1:
				print('clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('anti-clockwise')
			else:
				print("I don't know!")
		
		elif s == '^' and e == '<':
			if n == 3:
				print('clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 1:
				print('anti-clockwise')
			else:
				print("I don't know!")
		
		elif s == '^' and e == 'v':
			print("I don't know!")
		
		elif s == '^' and e == '^':
			print("I don't know!")
		
		elif s == '>' and e == '^':
			if n == 1:
				print('anti-clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('clockwise')
			else:
				print("I don't know!")
		
		elif s == '>' and e == '<':
			print("I don't know!")
	

		elif s == '>' and e == '>':
			print("I don't know!")

		elif s == '>' and e == 'v':
			if n == 1:
				print('clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('anti-clockwise')
			else:
				print("I don't know!")

		elif s == 'v' and e == '^':
			print("I don't know!")

		elif s == 'v' and e == 'v':
			print("I don't know!")

		elif s == 'v' and e == '<':
			if n == 1:
				print('clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('anti-clockwise')
			else:
				print("I don't know!")

		elif s == 'v' and e == '>':
			if n == 1:
				print('anti-clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('clockwise')
			else:
				print("I don't know!")

		elif s == '<' and e == '<':
			print("I don't know!")

		elif s == '<' and e == '>':
			print("I don't know!")

		elif s == '<' and e == '^':
			if n == 1:
				print('clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('anti-clockwise')
			else:
				print("I don't know!")

		else :
			if n == 1:
				print('anti-clockwise')
			elif n == 2:
				print("I don't know!")
			elif n == 3:
				print('clockwise')
			else:
				print("I don't know!")
		break


	except:
		break
