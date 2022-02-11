n = int(input("enter no. of rows :"))
boolen = int(input("enter 1 for true or 0 for false :"))
if boolen==1 :
    for i in range(1,n+1) :
        for j in range(1,i+1) :
            print(("*"),end="")
        print()
elif boolen==0 :
    for i in range(n,0,-1) :
        for j in range(1,i+1) :
            print("*",end="")
        print()
else :
    print("enter boolen value(0 or 1)")