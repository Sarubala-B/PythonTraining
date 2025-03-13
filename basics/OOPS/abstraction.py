from abc import ABC, abstractmethod  # Import Abstract Base Class module

# Define Abstract Class
class Animal(ABC):  
    @abstractmethod
    def make_sound(self):  
        pass  

# Concrete Class (Subclass implementing the abstract method)
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating objects of concrete classes
dog = Dog()
print(dog.make_sound())  

cat = Cat()
print(cat.make_sound())  


