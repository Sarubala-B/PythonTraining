# If statements
x = 20
if x > 30:
    print("x is greater than 30")
elif x > 10:
    print("x is greater than 10 but less than or equal to 30")  # Output
else:
    print("x is 10 or less")

# Nested if Statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")


# For
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Range 
for i in range(5):  # range(5) generates numbers 0 to 4
    print(i)


# while
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment to avoid infinite loop


# break and continue
for i in range(1, 10):
    if i == 5:
        break 
    print(i) 

for i in range(1, 6):
    if i == 3:
        continue  
    print(i)  

