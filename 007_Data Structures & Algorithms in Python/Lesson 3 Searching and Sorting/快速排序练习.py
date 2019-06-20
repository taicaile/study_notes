"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quicksort_(array, 0, len(array))
    return array
    
def quicksort_(array, start, end):
    if start >= end:
        return None
    pivot = end-1
    for i in range(start, end-1):
        if array[i] > array[pivot]:
            array[i], array[pivot] = array[pivot], array[i]
    quicksort_(array, start, pivot)
    quicksort_(array, pivot+1, end-1)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
