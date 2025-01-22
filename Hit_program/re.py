#Open File
file = open("z.py", "r")
print(file.read())

#Append File

file = open("z.py", "a")
file.write("my new project")
file.close()

file = open("z.py", "r")
print(file.read())

#Delete file

import os
os.remove("z.py")