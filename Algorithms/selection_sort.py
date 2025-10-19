def find_smallest(arr):     #helper function
    smallest = arr[0]       #stores smallest number
    smallest_index = 0      #returns index of smallest value

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    '''
    Recursive approach to selection sort
    '''
    new_arr = []       #blank array to return
    for i in range(len(arr)):
        smallest = find_smallest(arr)   #finds smallest element and adds it to new array
        new_arr.append(arr.pop(smallest))

    return new_arr

print(selection_sort([50,3,6,2,10]))