# filters
'''
    A list of cafe orders
    Filtered in a variety of ways
'''
import pandas as pd
from  random import randint


# Get the orders list
url = 'https://raw.githubusercontent.com/vchealy/__days_of_python__/main/cafe_orders.csv'
orders = pd.read_csv(url, index_col=[0])

# print(orders.columns)   # order_id,quantity,item_name,choice_description,item_price
# print(orders.dtypes)
# print(orders.head)
# print(orders)

def sort_prices_to_floats(orders):
    # Convert the string values into floats for the order prices
    # This is used by some of the functions below
    prices = [float(value[1 : -1]) for value in orders.item_price]
    orders.item_price = prices # Convert column of prices from string object to float
    return orders


def item_prices(orders):
    # A list of the items and their price
    orders = sort_prices_to_floats(orders)
    # Chained Output
    print (
        orders # 
        .drop_duplicates('item_name') #  Reduce to single entry for each item
        # .sort_values(by='item_price', ascending=False) # Sort expensive first
        .sort_values(by='item_name', ascending=True) # Sort Alphabetical
        [['item_name', 'item_price']] # Remove other columns
        )


def items_cost_more_than(orders):
    # Set the more_than value, and see which items cost more than that value
    orders = sort_prices_to_floats(orders)
    more_than = 10.00 # Change this to what you want to check
    # Chained Output
    print (
        orders[orders.item_price > more_than] # Items costing more than variable
        .drop_duplicates('item_name') #  Reduce to single entry for each item
        .sort_values(by='item_price', ascending=False) # Sort expensive first
        [['item_name', 'item_price']] # Remove other columns
        )


def most_expensive_item_orders(orders):
    # How many of the most expensive item were ordered and in how many orderse
    orders = sort_prices_to_floats(orders)
    # Get the item
    most_expensive_ordered_item =(orders
                                    .sort_values(by= 'item_price', ascending= False)
                                    .iloc[0]
                                    .item_name
                                  )
    # Chained output
    print(
        most_expensive_ordered_item,
        'There were ',
        orders
        [orders.item_name == most_expensive_ordered_item]
        .quantity.sum(),
        ' ordered'
    )
    print(
        'That was from ',
        orders
        [orders.item_name == most_expensive_ordered_item]
        .quantity.count(),
        ' orders'
    )


def how_many_orders_of_specific_item(orders):
    # Randomly selects an item and states how many were ordered and on how many orders
    orders = sort_prices_to_floats(orders)
    random_choice = randint(0, len(orders.index)) # This allows the specific item to be random everytime
    specific_item = (
        orders
        .iloc[random_choice]
        .item_name
    )
    print(
        'The item ',
        specific_item,
        ' was ordered ',
        orders
        [orders.item_name == specific_item]
        .quantity.sum(),
        ' times'
    )
    print(
        'From a total of ',
        orders
        [orders.item_name == specific_item]
        .quantity.count(),
        ' orders'
    )
 

def orders_with_multiples_of_certain_item(orders):
    # This is shows where an order had multiples of any one item
    ordered = [int(value) for value in orders.quantity]
    orders.quantity = ordered
    print(
        orders
        [orders.quantity > 1] # More than one ordered
        .drop(columns= ['choice_description','item_price']) # Drop columns not needed
        # .sort_values(by='item_name') # Sort by items name
        .sort_values(by='quantity', ascending= False) # Sort by largest single order
        .to_string(index=False)
    )


# items_cost_more_than(orders)
# item_prices(orders)
# most_expensive_item_orders(orders)
# how_many_orders_of_specific_item(orders)
# orders_with_multiples_of_certain_item(orders)