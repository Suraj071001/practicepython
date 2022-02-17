# oh soldier prettify my folder
import os

def soldier(path,file,format) :
    list_of_files = os.listdir(path)
    os.chdir(path)
    print(list_of_files)

    #capitalise the first letter
    for item in list_of_files :
        with open(file) as f :
            a = f.readlines()
            if item not in a[0] :
                print(item)
                a = item[0].upper()+item[1:]
                os.rename(item,a)

    #change name of all files those have given format
    v=0
    for i in range(len(list_of_files)) :
        if list_of_files[i].endswith(format) :
            v = v + 1
            a = str(v)+".bmp"
            os.rename(list_of_files[i],a)
soldier("C:\\Users\87514\PycharmProjects\Oh_soldier","oh_soldier_file.txt",".bmp")

