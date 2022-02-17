"""
Iterable - __iter__() or __getitem__() - those object which have these methods then we called those methods iterable
Iterator - __next__() - iterators are those methods which we used on iterable objects
Iteration - is  process of generating value
"""
"""generator and for loop is almost same but it helps us to safe storage at large operation by not doing unnessessary work"""

def gen(n):# this is generator not function
    for i in range(n):
        yield i # return store value then end the function but yeild change value time by time according to function

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
