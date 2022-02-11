"""i done this work more neetly in oops_practice"""
"""syntax of writing a class without constructor"""
class Student:
    pass


harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)

"""is code me hamne ye sekha ki agar hame class ke variable change karne hai to vo ham class ke naam se hi kar sakte hai.
   or class ke variable instance ke variable se kaise alag hai """
class Employee:
    no_of_leaves = 8
    pass
#creating instances of class
harry = Employee()
rohan = Employee()

#ye harry instance ke variable hai
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

#ye rohan instance ke variable hai
rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)# aise ham class ke variable ki value ko print kar sakte hai
print(Employee.__dict__)
print(rohan.__dict__)# ye __dict__ function ek dictionary return kar ta hai jisme us instance ke sare variable hote hai with value
Employee.no_of_leaves = 9
print(Employee.__dict__)# isko __dict__ ko ham class ke liye bhi use kar sakte hai
print(Employee.no_of_leaves)


"""isme hamne sikha self or __init__ constructor ke baare me"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")
# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)


"""isme hamne classmethod ke baarme sikha 
or ise ham alternative constructor ki terha bhi use kar sakte hai"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
# rohan.change_leaves(34)
#
# print(harry.no_of_leaves)


"""static method"""

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

#code of single inheritance
class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):# we don't need write attributes of parent class (read next line)
        self.name = aname#we can do this by using super which can seen this in just little below (read next line)
        self.salary = asalary#we can do this like this also but super do this work by just one line
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")
subham = Programmer("subham",736,"programmer","python")
Employee.printgood("Rohan")

subham.printgood("pyhon")
print(subham.printprog())

#code of multi heritance
class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"
class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

suraj = CoolProgramer("Karan",["Cricket"])
suraj.printlanguage()

#multilevel inheritance

class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone

"""public , protected and private variable in class"""
class Ppp :
    public = 1# public variable can obtain by any class like child class
    _private = 2# protected variable only used by main class or its methods other class doesn't inheritate private varibles
    __private = 3# private varible only used by main class by this syntax(_classname__private)

"""super and overwriting """
"""if we use same name multiple variables then which value class gona use here its priority list
   1. parent class instances variable
   2. child class instances variable
   3. parent class variable
   4. child class variable
   this is a cncept of overwriting"""
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        """if we run this program without using super() then we don't able to access child class variables 
         by making class instance here without using super() overwrite the instance method here.
         super() help to solve this problem by add all variable here. 
         we do this thing by add all instances variable but syper does this just by one line."""
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)

"""diamond shape problem of multiple inheritance"""
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()


"""operator overloading"""
"""if add to method this internally run dander merthod like this print(emp1 + emp2))
   for do this we need to use 'mapping operators for function' like 'add, truediv,str,repr,etc
   """
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))

"""Abstract base class"""

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
"""for using abstract method me need to import ABC or abstractmethod from abc module"""

class Shape(ABC):
    """we can't create instances by using this class"""
    @abstractmethod# if we write abstract method then this method is nessessary to use in his parent class otherwise u give an error
    def printarea(self):
        return 0

class Rectangle(Shape):
    """this is child class of shape class so its need to define printarea method bcz we
    create a abstract method of printarea"""
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

"""------------------IMPORTANT---------------------------------"""
"""setters and property decorators"""


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property# if we want to call class method without parenties at that place we use property decorator
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter# this is syntax of setter if u don't know how its work then go again and see vedio of cwh
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter# deleter is used for deleting the value of instances attributes value for that instance
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"# this code only change the value of fname not change the fname in email
print(hindustani_supporter.fname)

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
""" we want to change the instances attributes value already made in at that moment we need setter to the value"""

print(hindustani_supporter.fname)

del hindustani_supporter.email # thats how we can delete the value by creating deleter
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)

