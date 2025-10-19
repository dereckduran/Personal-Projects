'''
Recursion is when a function calls itself
Used when it makes the solution clearer 
Splits the problem into subproblems
Calls on itself n times until base case is reached 
'''

def countdown(i):
    print(i)
    if i <= 0:      #base case, its needed so the funtion doesnt run forever
        return 
    else:           #recursive case
        countdown(i-1)


def sum(arr: list[int]):

    if arr == []:      #base case for arrays is an empty list
        return 0  
    return arr[0] + sum(arr[1:]) #recursive call, first element plus the second and 


print(sum([2,4,6,3]))


def count(arr: list):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count([1,2]))

def find_max(arr: list) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max 

print(find_max([40,100,50,3]))