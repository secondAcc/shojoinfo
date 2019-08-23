a=int(input("only input odd!!\n"))
for i in range(0,a):
    if i==0 or i==a-1 or i==a//2:
        for i in range(0,a):
            print("* ",end='')
        print("")
    else:
        print("*")