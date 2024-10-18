import os

fo = open("new_text_file.txt", "w+")
fo.writelines("1st line \n2nd line \n3rd line")
print(fo.read(5))
os.remove("new_text_file.txt")
fo = open("new_text_file.txt", "r")
print(fo.read(4))
fo.close()
