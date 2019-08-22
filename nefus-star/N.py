a=int(input())
for i in range(0,a):
    for j in  range(0,a-i):
        print(" ",end='')
    if i==0:
        print("*")
        continue
    for j in range(0,i):
        print(" ",end='')
    print("*")