# filter_list
'''
filter()
Filter out values (`False`, `None`, `0`, and `""`)
Filter out other variables
'''

def falsy_filter(lst):
  # Remove falsy values from a list
  return list(filter(None, lst))

def str_filter(lst):
  # Remove strings from as list
  return [x for x in lst if not isinstance(x, str)]


def int_filter(lst):
  # Remove values from a list with a lambda
  return list(filter(lambda num: num >= 4 and num < 20, lst))


# print(falsy_filter([0, 1, False, 2, '', 3, 'a', 'b', 23]))
# print(str_filter([0, 1, False, 2, '', 3, 'a', 'b', 23]))
print(int_filter([0, 1, 2, 3, 4, 5, 6, 23]))
