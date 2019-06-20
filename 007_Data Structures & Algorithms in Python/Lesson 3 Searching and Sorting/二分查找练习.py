"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    return binary_search_(input_array, value, 0, len(input_array))


def binary_search_(input_array, value, start, end):
    if value >= input_array[start] and value <= input_array[end - 1]:
        index = (start + end) // 2
        if input_array[index] == value:
            return index
        elif input_array[index] > value:
            return binary_search_(input_array, value, start, index)
        else:
            return binary_search_(input_array, value, index + 1, end)
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
