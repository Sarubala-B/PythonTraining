my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[1])
print(thistuple[-1])

print(len(my_tuple))
print(type(my_tuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

y = list(thistuple)
y.append("grapes")
thistuple = tuple(y)
print(thistuple)

y.remove("grapes")
thistuple = tuple(y)
print(thistuple)