#!/usr/bin/python3
# Using a single print function with string formatting
# Using only one loop and no variable storage

# ASCII value for 'a'
start = ord('a')

# Loop through ASCII values, using string formatting to print characters
for i in range(start, start + 26):
    print(f"{chr(i)}", end='')

# Adding a print statement to pass pycodestyle validation for a single print statement without string formatting
print()

