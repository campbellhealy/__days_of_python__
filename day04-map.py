# map
'''
    Working with map
    Taking the input strings and converting them to integers
    Quicker to type than iterating over a list
'''
# Generatep a list of string numbers]
numbers = []
for x in range(3):
    input_string = input('Type a number\n')
    numbers.append(input_string)

# Convert the list of strings to a list of int
input_int = list(map(int, numbers))

# Output to console
print(f'The numbers you entered were added to a {type(numbers)}')
print(f'The numbers you entered were a type {type(input_string)}')  
print(numbers, '\n')
print(f'Map converted the {type(input_string)} numbers to {type(input_int[2])} numbers')  