# dataframe_manipulation
'''
   justmarkham on github had written jupyter notebooks for this, but the way Python and pandas moves so quickly
    there was a lot of deperaction that needs sorted. So I have rewrote this in functions, in my prefered way.

    There was a little cross over on a couple of functions that I could have called the functions but
    it was only a couple lines of code, so I just copied them down to the next functions.

    The data is a list for cafe orders with costs for a time period and the functions break down the numbers etc.
    You could easily swap this data out for something else that has items sold for a price, just see the structure of the xlsx.
'''
import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
data = pd.read_csv(url, sep = '\t')
data = data.sort_values(by=['item_name'])

data.to_excel('out.xlsx', index=False) # Just so you can see the data


def get_each_item_ordered(data):
    # Used this to help determine other ways to complete the other functions
    print(f'Total unique items ordered {data.item_name.unique().size}')
    print(f'Total unique items ordered {data.item_name.value_counts()}')


def most_ordered_item(data):
    # Get a count of the unique values in the items order
    print(data.item_name.value_counts().index[0])
    # Below is deprecated
    # c = data.groupby('item_name')
    # c = c.sum()
    # c = c.sort_values(['quantity'], ascending=False)
    # print(c.head(1))


def count_most_ordered_item(data):
    print(data.item_name.value_counts().iloc[:1])
    # Below is deprecated
    # c = data.groupby('item_name')
    # c = c.sum()
    # c = c.sort_values(['quantity'], ascending=False)
    # print(c.head(1))

def most_ordered_choice_description(data):
    # Get a count of the unique values in the items order
    print(type(data.choice_description.value_counts().index[0])) # Found it was a string
    print((data.choice_description.value_counts().index[0])[1:-1]) # Removes the square brackets by slicing
    # Below is deprecated
    # c = data.groupby('choice_description').sum()
    # c = c.sort_values(['quantity'], ascending=False)
    # print(c.head(1))


def total_orders(data):
    print(data.quantity.sum())


def price_convertor(data):
    # Convert the string value to a float
    print(f'Original price type {data.item_price.dtype}') # Object is a string
    # print(f' Original price {data.item_price}') # Show the sting
    monetise = lambda x: float(x[1:-1]) # convert str to float
    print(f'Cash price type {data.item_price.apply(monetise).dtype}')
    print(f'Cash price type {data.item_price.apply(monetise)}')



def revenue_calculation(data):
    # Bringing in the price_convertor to change strings to floats
    monetise = lambda x: float(x[1:-1]) # convert str to float
    data.item_price = data.item_price.apply(monetise)
    revenue = (data['quantity']* data['item_price']).sum()
    print('Revenue was: £' + str(np.round(revenue,2)))


def count_orders_for_period(data):
    print(f'The total number of orders was {data.order_id.value_counts().count()} for this period')
    

def average_order_cost(data):
    # Bringing in the price_convertor to change strings to floats
    monetise = lambda x: float(x[1:-1]) # convert str to float
    data.item_price = data.item_price.apply(monetise)
    data['revenue'] = data['quantity'] * data['item_price']
    total_order_cost = np.round(data['revenue'].sum(),2)
    total_number_of_orders = data.shape[0]
    print(f' Average cost per order £{np.round((total_order_cost/total_number_of_orders),2)}')
    # Below deprecated
    # order_grouped = data.groupby(by=['order_id']).sum()
    # print(order_grouped.mean()['revenue'])
    # print(data.groupby(by=['order_id']).sum().mean()['revenue'])


def count_different_items(data):
    print(f'There was a total of {data.item_name.value_counts().count()} different items sold')


# Basic information about the data
# print(data.head(10)) # First 10 items
# print(data.shape[0] ) # Number of records
# print(data.info()) # Info on the df
# print(data.shape[1] ) # Number of columns 
# print(data.columns) # Show the column labels
# print(data.index) 

get_each_item_ordered(data)
# most_ordered_item(data)
# count_most_ordered_item(data)
# most_ordered_choice_description(data)
# total_orders(data)
# price_convertor(data)
# revenue_calculation(data)
# count_orders_for_period(data)
# average_order_cost(data)
# count_different_items(data)