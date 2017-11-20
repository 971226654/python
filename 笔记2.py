'''
R = eval(input("请输入正整数："))
i,s = 0,0
while (i<=R):
    s = s +i
    i = i+1
print("累加求和：",s)
'''

'''
##偶数累加
R = eval(input())
i,s = 0,0
while(i<R):
    i+=2
    s=s+i
    print(i,s,sep=':')
print("Sigma=",s)


##奇数累加
R = eval(input())
i,s = -1,0
while(i<R):
    i+=2
    s=s+i
    print(i,s,sep=':')
print("Sigma=",s)
'''

'''
R = eval(input())
s = 0
for i in range(0,R+1,3):
    s = s + i
    print(i,s,sep=':')
print("Sigma=",s)
'''

'''
s = input()
for i in s:
    print(i)
'''


##s = input()#ABCD>DBCA
##l = len(s)
##index = l-1
##while index >= 0:
##    print(s[index],end='')
##    index -= 1


'''
for i in range(20):
    if i == 10:
        continue
    print(i,end=' ')
'''


for s in "BIT":
    for i in range(10):
        print(s,end=" ")
        if s == "I":
            break





















