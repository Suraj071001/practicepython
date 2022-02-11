def getdate():
    import datetime
    return datetime.datetime.now()
a = getdate()
print("enter 1 for suraj , 2 for harry , 3 for nitesh")
name = int(input("enter your name :"))
log = int(input("enter 1 for 'food log' or 2 for 'exercise log' :"))
choice = int(input("enter 1 for add or 2 for retreive"))
def add() :
    if name==2 :
        if log == 1 :
            with open("harry_food.txt","a" ) as f:
                p = input("what you want to add :")
                f.write("["+str(a)+"] : "+p)
        elif log == 2 :
            with open("harry_exercise.txt","a" ) as f:
                p = input("what you want to add :")
                f.write("[" + str(a) + "] : " + p)
    if name == 1:
        if log == 1:
            with open("suraj_food.txt","a" ) as f:
                p = input("what you want to add :")
                f.write("[" + str(a) + "] : " + p)
        elif log == 2:
            with open("suraj_exercise.txt","a" ) as f:
                p = input("what you want to add :")
                f.write("[" + str(a) + "] : " + p)
    if name == 3:
        if log == 1:
            with open("nitseh_food.txt","a" ) as f:
                p = input("what you want to add :")
                f.write("[" + str(a) + "] : " + p)
        elif log == 2:
            with open("nitesh_exercise.txt", "a") as f:
                p = input("what you want to add :")
                f.write("[" + str(a) + "] : " + p)

def retreive() :
    """take input as user name and give the users food or exercise log."""
    if name==2 :
        if log == 1 :
            with open("harry_food.txt", ) as f:
                print(f.readlines())
        elif log == 2 :
            with open("harry_exercise.txt", ) as f:
                print(f.readlines())
    if name == 1:
        if log == 1:
            with open("suraj_food.txt", ) as f:
                print(f.readlines())
        elif log == 2:
            with open("suraj_exercise.txt", ) as f:
                print(f.readlines())
    if name == 3:
        if log == 1:
            with open("nitseh_food.txt", ) as f:
                print(f.readlines())
        elif log == 2:
            with open("nitesh_exercise.txt", ) as f:
                print(f.readlines())
if choice==1 :
    add()
elif choice==2 :
    retreive()