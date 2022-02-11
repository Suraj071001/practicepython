s = set()
print(type(s))
l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
s.add(1)
s.add(2)
print(s.union(s))
print(s)
