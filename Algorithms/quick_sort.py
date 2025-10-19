'''
QuickSort is an algorithm that picks a pivot and makes sub arrays of the elements 
that are less than and bigger than the pivot, then calls itself to sort subarrays

n * log n time but depends on pivot, usuallu try to pick random element
'''

def qsort(arr: list):
    if len(arr) < 2:
        return arr
    pivot = arr[0]

    less = [i for i in arr[1:] if i < pivot]

    greater = [i for i in arr[1:] if i > pivot]

    return qsort(less) + [pivot] + qsort(greater)

print(qsort([100,30405,1,45,59,294,10,6]))