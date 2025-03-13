def greet(name, age):
    return f"Hello, my name is {name} and I am {age} years old."

info = {"name": "Alice", "age": 25}
print(greet(**info))  
