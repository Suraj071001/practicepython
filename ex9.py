"""----------------Pickle iris---------------"""
import pickle

with open("ex9_file.txt","r") as f :
    list = f.readlines()
l2 = [item.split(",") for item in list if item != 0 ]

with open("iris.pkl", "wb") as f :
    pickle.dump(l2,f)

with open("iris.pkl","rb") as f :
    i = pickle.load(f)
print(i)