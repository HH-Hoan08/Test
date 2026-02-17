def my_enumerate(sequence):
    for element in sequence:
        yield element

fruits = ["apple", "banana", "cherry"]
list_food = my_enumerate(fruits)
for index, value in enumerate (list_food, start = 1):
    print(f"STT {index}: {value}")
