# map_to_func
'''
    Working with map
    Like the previous map of taking the input strings and converting them to integers
    I have added mapping to a function
'''

import pandas as pd

data = pd.Series(['Vegan', 'Veggie','Chicken', 'Fish', 'Beef'], copy=False)

def add_statement(x):
    return 'Today\'s dinner is ' + x

# Map to a function
dinners = list(map(add_statement, data))
# Output to console
print(dinners)