# Bitwise operations are operations that directly manipulate bits (binary digits) of integers.
# Python supports bitwise operators for binary manipulation:

# & (AND): Sets each bit to 1 if both bits are 1
a = 12  # Binary: 1100
b = 10  # Binary: 1010
result = a & b  # Binary: 1000 (8 in decimal)
print(result)   # Output: 8

# | (OR): Sets each bit to 1 if at least one of the bits is 1
a = 12  # Binary: 1100
b = 10  # Binary: 1010
result = a | b  # Binary: 1110 (14 in decimal)
print(result)   # Output: 14

# ^ (XOR): Sets each bit to 1 if only one of the bits is 1
a = 12  # Binary: 1100
b = 10  # Binary: 1010
result = a ^ b  # Binary: 0110 (6 in decimal)
print(result)   # Output: 6

# ~ (NOT): Inverts all the bits (flips 0 to 1 and 1 to 0)
# In Python, integers are represented using two's complement, 
# which means the result of ~ will also depend on the sign of the number.
# Two's Complement Representation:
# For positive numbers, ~ will produce a negative number.
# For negative numbers, ~ will produce a positive number.
# The ~ operator is equivalent to: ~x = -x - 1
a = 12  # Binary: 1100
result = ~a  # Inverts bits: -13 (two's complement representation)
print(result)  # Output: -13

# << (Left shift): Shifts bits to the left, filling with 0s on the right
a = 5  # Binary: 0101
result = a << 1  # Binary: 1010 (10 in decimal)
print(result)    # Output: 10

# >> (Right shift): Shifts bits to the right, filling with 0s on the left (for unsigned numbers)
a = 10  # Binary: 1010
result = a >> 1  # Binary: 0101 (5 in decimal)
print(result)    # Output: 5
