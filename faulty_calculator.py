n1 = int(input("enter 1st number :"))
n2 = int(input("enter 2nd number :"))
op = input("enter operator:")
if op=="+" and n1==56 or n1==9 and n2==9 or n2==56 :
    print("56 + 9 = 77")
elif op=="*" and n1==45 or n1==3 and n2==3 or n2==45 :
    print("45 * 3 = 555")
elif op=="/" and n1==56 and n2==6 :
    print("56/6 = 4")
else :
    if op == "+":
        print(str(n1)+"+"+str(n2)+"=",n1+n2)
    if op == "-":
        print(str(n1) + "-" + str(n2) + "=", n1 - n2)
    if op == "*":
        print(str(n1) + "*" + str(n2) + "=", n1 * n2)
    if op == "/":
        print(str(n1) + "/" + str(n2) + "=", n1 / n2)