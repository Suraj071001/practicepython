"""object oriented program pracice"""

# class Practice :
#     var1 = 12# class variable which can obtain by all instances
#
# # creating instances
# suraj = Practice()
# nitesh = Practice()
#
# #creating instances variable
# suraj.name = "Suraj"
# suraj.age = "20"
#
# nitesh.name = "Nitesh"
# nitesh.age = "19"
#
# print(suraj.__dict__)
# print(nitesh.__dict__)
# suraj.var1 = 23
# print(suraj.var1)
# print(suraj.__dict__)

"""class with constructor"""
class Game :
    """docstring"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def simple_method(self):
        print(f"my name is {self.name} and age is {self.age}")

    @classmethod
    def method(cls,name):
        return print(f"your name is {name}")

    @classmethod#as alternative constructor
    def alter_const(cls,all_arument):
        # paras = all_arument.split("_")
        # return cls(paras[0],paras[1])
        return cls(*all_arument.split("_"))# ye line bhi wahi kaam kar rahi jo upar wali line kar rahi hai

    """this class doesn't take any argument form init method or classmethod.
    this like simple function but we can create that method when we need to apply method just only on our class object 
    that time we use static method. and this method also cut unnessary work like take refrence from init method every time. """
    @staticmethod
    def static_method(string):
        print(f"static method doesn't need refrences like instances(self), class(cls) for work done{string}")


#instance
game = Game("Suarj","20")
game.simple_method()

Game.method("Suraj")
game1 = Game.alter_const("Suraj1_21")
print(game1.__dict__)
game1.static_method(".--->")