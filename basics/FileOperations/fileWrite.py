file = open("example.txt", "w") 
file.write("Hello, World!\n")
file.write("Python file handling is easy.\n")
file.close()

# Appending to a File
file = open("example.txt", "a") 
file.write("This is an appended line.\n")
file.close()

#  Writing Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("example.txt", "w")
file.writelines(lines)
file.close()

# Using with Statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  

# Checking if a File Exists
import os
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File not found!")
