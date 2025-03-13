# Without Data Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 25)
print(p) 


# With Data Class
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 25)
print(p)  
