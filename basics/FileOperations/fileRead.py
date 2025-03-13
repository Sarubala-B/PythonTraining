# Open file in read mode
file = open("example.txt", "r")
# Read entire content
content = file.read()
print(content)
file.close()  

# Read Only Parts of the File
f = open("example.txt", "r")
print(f.read(5))


file = open("example.txt", "r")
print(file.readline())  # Read first line
print(file.readlines())  # Read remaining lines as a list
file.close()
