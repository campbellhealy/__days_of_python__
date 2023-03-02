# lists_compare
'''
1. Check all of the elements in a list to see if they are the same
  Remove duplicates, and there should only be one element left if all the same.
2a. Check two lists to see if they are the same length.
2b. Check all the elements in a list to see if they are equal to a second list
'''
# 1
def item_compare_explained(input_list):
  # Use set() to remove duplicates
  setted_list = set(input_list)
  return len(setted_list) == 1


def item_compare(input_list):
  # Use set() to remove duplicates in the return
  return len(set(input_list)) == 1


#2a
def list_compare_length(lst1, lst2):
  # Compare list length
  if len(lst1) != len(lst2):
    return False
  else:
    return len(lst1) == len(lst2)


#2b
def list_item_compare(lst1, lst2):
    # Compare list length
  if len(lst1) == len(lst2):
    # Sort order of elements in both lists
    lst1.sort()
    lst2.sort()
    # Do the lists look identical
    if lst1 == lst2:
      return 'Matched lists'
  else:
    return 'List Mismatch'




# print(item_compare_explained([1, 2, 3, 4, 5, 6])) # False
# print(item_compare_explained([1, 1, 1, 1])) # True

# print(item_compare([1, 2, 3, 4, 5, 6])) # False
# print(item_compare([1, 1, 1, 1])) # True

# print(list_compare_length([1, 2, 3, 4, 5, 6],[1, 1, 1, 1])) # Length False
# print(list_compare_length([1, 2, 3, 4, 5, 6],[1, 2,3,4,5,6])) # Length True


# print(list_item_compare([1, 2, 3, 4, 5, 6],[1, 1, 1, 1])) # Length False, Do not match
# print(list_item_compare([1, 2, 3, 4, 5, 6],[1, 2,3,5,6,4])) # Length True, Same elements in both lists
