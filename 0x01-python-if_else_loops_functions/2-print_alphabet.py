# Using a single print function without .format()
# Using only one loop and no variable storage

# ASCII value for 'a'
start = ord('a')

# Loop through ASCII values, printing characters using string concatenation
for i in range(start, start + 26):
    print(chr(i), end='')
print()

