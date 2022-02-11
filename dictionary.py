# dictionary is nothing but key value pairs
"""dictionary is closed by curly brackets"""
d1 = {"suraj":{"age":"20","eat":"maggi"},"rohit":"doctor","ankit":"scientist"}
print(d1["suraj"])
print(d1["suraj"]["age"])
d1["nitesh"] = "programmer"# syntax of adding key value pair in dictionary
del d1["ankit"] #aise ham del kar sakte hai key value pairs
print(d1)

#some dictionary functions
d2 = d1.copy()# ye d1 ki ek copy banake usko d2 me store kar dega
d2.update({"leena":"toffee"})
print(d2.items())# ye saare key value pair print karta hai
print(d2.keys())#ye saari keys print karte hai
print(d2.values())#ye saari valyes ko print karta hai
