"""
a = 3
b = 5
c = int(input())
if c>b :#phale ye isko check karega agar ye true hai to iske andar ka saara code run kar dega
    print("greater")
else :#agar sab false hai to ye run ho jayega
    print("lesser")

l = [1,4,6,8]
if 1 in l :#1st check
    print("yes 3 in list")
if 4 in l :#2nd check agar 1st run bhi tab bhi isko check or run karega
    print("yes 4 in list")
elif 8 not in l :# agar upar me koi ek bhi chalega to ye nahi chalega
    print("8 not in list")
else :#3rd run agar agar koi or run nahi karta
    print("3 and 4 not in list")

age = int(input("Enter your age :"))
if age<18 :
    print("You are not ready for driving")
elif age==18 :
    print("first we check than we are able to tell you can drive or not")
elif age>18 and age<100:
    print("you can drive")
else :
    print("enter valid age")
"""
#short hand if else
a = 1
b = -1
print("a is graeter than b")if a>b else print("b is greater than a")