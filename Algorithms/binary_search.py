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
    if arr[mid_point] < item:       #the midpoint was less than
        return binary_search(arr, item, mid_point + 1, high) #making new low midpoint + 1 the new low, evaluating right half of array
        
    return None

def main():
    '''
    Test cases
    '''
    array = [1,3,5,7,9]

    print(binary_search(array, 3, 0, len(array)))
    print(binary_search(array, -1, 0, 5))
    print(binary_search(array, 9, 0, 5))
    print(binary_search(array, 5, 0, 5))

if __name__ == "__main__":
    main()