# map_to_func
'''
    Working with map
    Like the previous map of tTaking the input strings and converting them to integers
    I have added mapping the list of integers to a function
'''

def multiplier(x):
    return x*2

# Generatep a list of string numbers]
numbers = []
for x in range(3):
    input_string = input('Type a number\n')
    numbers.append(input_string)

# Convert the list of strings to a list of int
input_int = list(map(int, numbers))

# Map to a function
input_mult = list(map(multiplier, input_int))
# Output to console
print(input_mult)