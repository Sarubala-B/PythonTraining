my_set = {"apple", "banana", "cherry","mango","strawberry"}
my_set.add("orange")  # Adding an item
my_set.add("apple")   # "Duplicate, so it will not be added again
print(my_set)
print(len(my_set))
print(type(my_set))
my_set.remove("cherry")
my_set.discard("strawberry")
print(my_set)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)