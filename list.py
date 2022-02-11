"""list is enclosed in square bracket and items is seperate with comma"""
fruits = ["apple","mango","kiwi","banana","orangre","strawberry"]
print(fruits)
print(fruits[5])#syntax of print seperate item
numbers = [2,5,2,4,8,3]
print(numbers[2])

#some important functions of string
numbers.sort()#ye hame no. sequence me laga ke deta hai
print(numbers)
numbers.reverse()
print(numbers)# ye items ko reverse kar deta hai
print(max(numbers))#give maximum no.
print(min(numbers))
numbers.append(4)#ye item add kar deta hai list ke last me
numbers.insert(3,34)# ye 3rd position pe 34 add kar dega
numbers.remove(2)
print(numbers)
numbers.pop()# last wala item hata dega
numbers[2] = 45 # change kar 2nd position value ko 45 se
print(numbers)

"""mutable - can change
   unmutable - can't change"""
tp = (1,3,5)#tuble ko parentitis se close kiya jata hai or tuble mutable hai
#tp[1] = 23 give error bcz we can't change the value of tuple hai

"""ham list ki slicing same string ki tera kar sakte hai"""