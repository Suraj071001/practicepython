"""join function only take one argument """
# lis = ["John", "cena", "Randy", "orton",
#        "Sheamus", "khali", "jinder mahal"]
#
#  for item in lis:
#      print(item, "and", end=" ")

# a = ", ".join(lis)
# print(a, "other wwe superstars")

"""join function ek character ko join kar deta hai"""
a = "suraj"
print("      ".join(a))

"""join function only join key pairs of dictionary"""
myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))