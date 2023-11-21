#!/usr/bin/python3
# Store the values in variables a and b
a = 1
b = 2

# Import the function add from the file add_0.py
from add_0 import add
# Calculate the sum
result = add(a, b)

# Print the formatted output
print(f"{a} + {b} = {result}")

