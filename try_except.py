
f1 = open("harry.txt")

try:# IF code inside try is not giving error then it will run otherwise compiler ignore code inside it
    f = open("does2.txt")

except EOFError as e:#this will run when try is not run
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:#this will run when except not run
    print("This will run only if except is not running")

finally:# this will always run
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
