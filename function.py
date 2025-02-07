# 1. Decimal to Binary Conversion
# Use the bin() function to convert a decimal number to its binary representation.
decimal_number = 13
binary_string = bin(decimal_number)[2:]
print(binary_string)  # Output: 1101

# 2. Binary to Decimal Conversion
# Use the int() function with base 2 to convert a binary string to a decimal number.
binary_string = "1101"
decimal_number = int(binary_string, 2)
print(decimal_number)  # Output: 13