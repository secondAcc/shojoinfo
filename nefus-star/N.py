a=int(input())
for i in range(0,a):
    for j in  range(0,a-i):
        print(" ",end='')
    print("*",end='')
    if i==0:
        for i in range(0,((a-1))*2-1):
            print(" ",end='')
        print("*")
        continue
    for j in range(0,i*2-1):
        print(" ",end='')
    print("*",end='')
    if i==a-1:
        continue
    for i in range(0,((a-1)-i)*2-1):
        print(" ",end='')
    print("*")