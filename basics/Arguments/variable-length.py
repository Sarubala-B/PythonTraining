def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  
print(add_all(5, 10))       


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

