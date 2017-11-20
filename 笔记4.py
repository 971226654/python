#用函数做简单的阶乘
##def factorial(n):
##    f = 1
##    for i in range(1,n+1):
##        f = f * i
##    return f
##a = factorial(5)+ factorial(3)
##print(a)
##
##

#用函数做所输入的字符打印（不返回数值）
##n = int(input())
##c = input()
##def printf(n,c):
##    for i in range(1,n+1):
##        print(c,end='')        
##printf(n,c)

#用函数做所输入的字符打印（返回数值）
##n = int(input())
##c = input()
##def printf(n,c):
##    s = ''
##    for i in range(1,n+1):
##        s = s + c
##    return s
##print(printf(n,c))

#用函数比较一个范围内的大小
##def vfunc(a,*b):
##    for n in b:
##        a += n
##    return a
##
##print(vfunc(1,2,3,4,5))

'''
#用函数比较所有数的大小
def vmin(*n):
    min = 0
    isFirst = False
    for i in n:
    	if (not isFirst):
    		min = i
    		isFirst = True
    	else:
	        if i<min:
	            min = i
    return min       
print(vmin(1,5,-8,12))
'''

'''
#普通的二维数组输入和打印
m,n = map(int,input("m row and n col :").split())
a = [[0 for j in range(n)]for i in range(m)]
for i in range(m):
	a[i][0:] = map(int,input("please "+str(i)+"the line:").split())
print(a)
for i in range(m):
	for j in range(n):
		print(a[i][j],end='')
	print('')
'''


#用函数做个普通的二维
def print2DArray(a):
	for row in a:
		for col in row:
			print("{:>6}".format(col),end='')
		print('')
a = [[1,30],[1222,4]]
b = [[1,30,89],[1222,4,99],[5246,48,999]]
print2DArray(a)
print("******************")
print2DArray(b)