mystr = "suraj is a good boy"
print(len(mystr))
print(mystr[0:12])
#print(mystr[45])  gives error beacuse i don't use colon
print(mystr[0:45])#but not gives the error only
print(mystr[0:])#if after colon is empty then it takes len of string by default
print(mystr[:14])# if before colon is empty then it takes 0 by default
print(mystr[0:19:])# work normally
print(mystr[1:14:1])# also print normally
print(mystr[1:14:2])#ab ye ek chod ke 2nd value print karega
print(mystr[1:16:3])# ab do chod ke 3rd value print ho gi
print(mystr[::-1])# puri string ko ulta kar dega
print(mystr[0:13:-1])#magar ye kuch nahi print karega kiyuki 0 ke peche to kuch hai hi nahi
print(mystr[-2:1:-2])# ab ye print karega

#some useful function of strings
print(mystr.endswith("oy"))
print(mystr.count("s"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.title())