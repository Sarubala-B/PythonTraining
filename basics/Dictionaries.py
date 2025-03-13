my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["age"] = 26  # Modifying a value
my_dict["country"] = "USA"  # Adding a new key-value pair

try:
    print(True + "test")
except TypeError as e:
    print(f"Got error {str(e)}")


my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["age"] = 26  
my_dict["country"] = "USA"  

try:
    print(my_dict["number"]) 
except KeyError as e:
    print(f"Got KeyError: {str(e)}")
