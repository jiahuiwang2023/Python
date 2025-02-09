# Mathematical Functions
print(abs(-5))          # Output: 5
print(round(3.14159, 2))  # Output: 3.14
print(min(1, 2, 3))     # Output: 1
print(max(1, 2, 3))     # Output: 3
print(sum([1, 2, 3]))   # Output: 6
print(pow(2, 3))        # Output: 8 (2^3)

# Iterable and Sequence Functions
# These functions work with iterables (e.g., lists, tuples, strings).
# len(): Returns the length of an object.
print(len("Python"))  # Output: 6
# range(): Generates a sequence of numbers.
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
# enumerate(): Adds a counter to an iterable and returns it as an enumerate object.
for i, char in enumerate("abc"):
    print(i, char)
# Output:
# 0 a
# 1 b
# 2 c
# sorted(): Returns a sorted list from the items in an iterable.
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
# reversed(): Returns a reversed iterator.
print(list(reversed("abc")))  # Output: ['c', 'b', 'a']

# Decimal to Binary Conversion
# Use the bin() function to convert a decimal number to its binary representation.
decimal_number = 13
binary_string = bin(decimal_number)[2:]
print(binary_string)  # Output: 1101

# Binary to Decimal Conversion
# Use the int() function with base 2 to convert a binary string to a decimal number.
binary_string = "1101"
decimal_number = int(binary_string, 2)
print(decimal_number)  # Output: 13

# Boolean Functions
print(all([True, False, True]))  # Output: False
print(any([True, False, True]))  # Output: True

# zip(): Combines multiple iterables into tuples.
names = ["Alice", "Bob"]
scores = [85, 90]
print(list(zip(names, scores)))  # Output: [('Alice', 85), ('Bob', 90)]

# map(): Applies a function to all items in an iterable.
numbers = [1, 2, 3]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9]

# filter(): Filters items in an iterable based on a condition.
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2]

# help(): Displays documentation for a function or module.
help(print)  # Displays documentation for the print function

