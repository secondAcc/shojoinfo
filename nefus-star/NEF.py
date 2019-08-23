def e():
    for i in range(0,a):
        if i==0 or i==a-1 or i==a//2:
            for i in range(0,a):
                print("* ",end='')
            print("")
        else:
            print("*")
    print("")
def n():
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
    print("\n")
def f():
    for i in range(0,a):
        print("* ",end='')
        if i==0 or i==a//2:
            for i in range(0,a-1):
                print("* ",end='')
        print("")
global a
a=int(input("only input odd!!\n"))
n()
e()
f()