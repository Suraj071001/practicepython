# r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.

# w : w mode does not concern itself with what is present in the file. It just opens a file for writing and
# if there is already some data present in the file, it overwrites it.

# x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.

# a : a stands for append, which means to add something to the end of the file. It does exactly the same.
# It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file.
# It also does not have the permission of reading the file.

# t : t mode is used to open our file in text mode and only proper text files can be opened by it.
# It deals with the file data as a string.

# b : b stands for binary and this mode can only open the binary files, that are read in bytes.
# The binary files include images, documents, or all other files that require specific software to be read.

# + : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file.

f = open("suraj.txt", "rt")
print(f.readlines())# ye file ki saari line ko read kar leta hai
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read() #agar ek baar hamne file read kar li to fir or kuch operation kaam nahi karegi
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()

# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("suraj.txt", "r+")
print(f.read())
f.write("thank you")

f = open("suraj.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()

with open("harry.txt") as f:
    a = f.readlines()
    print(a)

# f = open("harry.txt", "rt")
# Question of the day - Yes or No and why?
# f.close()

