'''
Big O notation is log2(n)
Question 1: suppose you have a sorted list of 128 names, and you're searching through it using binary search. Whats the maximum number of steps it
would take?
log_2(128) = 7
Question 2: Suppose the size of the list is doubled, whats the maximum now?
128 x 128 = 16,384
log_2(16384) = 14

'''

def binary_search(arr: list[int], item: int, low: int, high: int):



    '''
    Recursive approach to binary search
    '''
    if(low > high):     #base case to verify inex out of range
        return -1

    mid_point = (low + high) // 2   #calculating the midpoint of the array 
    if arr[mid_point] == item:      #evaluating whats inside of index at array to value
        return mid_point            #returning if found
    if arr[mid_point] > item:       #the midpoint was bigger than the item 
        return binary_search(arr, item, low ,mid_point -1)  #making the mid point - 1 the new high, evaluating the left half of array
    return binary_search(arr, item, mid_point + 1, high) # the midpoint was less than making new low midpoint + 1 the new low, evaluating right half of array
        
    return None

def main():
    '''
    Test cases
    '''
    array = [1,3,5,7,9]

    print(binary_search(array, 3, 0, len(array) - 1))
    print(binary_search(array, -1, 0, len(array) - 1))
    print(binary_search(array, 9, 0, len(array) - 1))
    print(binary_search(array, 5, 0, len(array) - 1))

if __name__ == "__main__":
    main()