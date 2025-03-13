# # Built-in Context Manager
# with open("example.txt", "w") as file:
#     file.write("Hello, World!")  

# # Creating a Custom Context Manager
# class MyContextManager:
#     def __enter__(self):  # Code before `with` block
#         print("Entering Context")
#         return self  # Value returned here is used inside `with`

#     def __exit__(self, exc_type, exc_value, traceback):  # Code after `with` block
#         print("Exiting Context")
#         if exc_type:
#             print(f"Exception Occurred: {exc_value}")  # Handles exceptions
#         return True  # Prevents the exception from propagating

# # Usage
# with MyContextManager():
#     print("Inside the Context")
#     # raise ValueError("Something went wrong!")  # Un-comment to see exception handling
# print("Outside the Context")


from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)  
    yield f 
    f.close()  

# Using the custom context manager
with open_file("test.txt", "w") as file:
    file.write("Hello, World!") 

print("File is closed:", file.closed)  
