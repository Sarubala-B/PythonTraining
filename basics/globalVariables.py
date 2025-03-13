def greet():
    message = "Hello"  # Local variable
    print(message)
greet()
# print(message)


name = "Alice"  # Global variable
def print_name():
    print(f"Name is {name}")
print_name()
print(name)


# global variable inside a function
count = 0
def increment():
    global count
    count += 1

increment()
print(count)  
