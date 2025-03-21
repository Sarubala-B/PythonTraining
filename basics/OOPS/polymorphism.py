class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Function demonstrating polymorphism
def make_it_fly(bird):
    bird.fly()

sparrow = Bird()
penguin = Penguin()

make_it_fly(sparrow)  
make_it_fly(penguin)  