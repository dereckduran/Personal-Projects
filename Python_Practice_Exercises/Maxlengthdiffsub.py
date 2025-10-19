''''
Given an array of n integers. The problem is to find maximum length of the subsequence with difference between adjacent elements in the subsequence as either 0 or 1. Time Complexity of O(n) is required.
Examples: 
 

Input : arr[] = {2, 5, 6, 3, 7, 6, 5, 8}
Output : 5
The subsequence is {5, 6, 7, 6, 5}.

Input : arr[] = {-2, -1, 5, -1, 4, 0, 3}
Output : 4
The subsequence is {-2, -1, -1, 0}.

from typing import Any
def max_subsequence(nums: list):
    hash = {}
    nums.sort()
    
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i] == nums[i + 1]) or (nums[i + 1] - nums[i] == 1):
                hash[nums[i]] += 1

    return max(hash.keys())

nums = [2, 5, 6, 3, 7, 6, 5, 8]

print(max_subsequence(nums))

def maxLenSub( arr, n):
    mls=[]
    max = 0
     
    #Initialize mls[] values for all indexes
    for i in range(n):
        mls.append(1)
     
    #Compute optimized maximum length subsequence
    # values in bottom up manner
    for i in range(n):
        for j in range(i):
            if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1):
                mls[i] = mls[j] + 1
                 
    # Store maximum of all 'mls' values in 'max'
    for i in range(n):
        if (max < mls[i]):
            max = mls[i]
     
    #required maximum length subsequence
    return max
     
#Driver program to test above
arr = [2, 5, 6, 3, 7, 6, 5, 8]
n = len(arr)
print("Maximum length subsequence = ",maxLenSub(arr, n))
'''
# Python3 implementation to find maximum
# length subsequence with difference between
# adjacent elements as either 0 or 1
from collections import defaultdict

# Function to find maximum length subsequence with
# difference between adjacent elements as either 0 or 1
def maxLenSub(arr, n):

	# hash table to map the array element with the
	# length of the longest subsequence of which it is a
	# part of and is the last element of that subsequence
	um = defaultdict(lambda:0)
	
	# to store the maximum length subsequence
	maxLen = 0
	
	# traverse the array elements
	for i in range(0, n):
	
		# initialize current length
		# for element arr[i] as 0
		length = 0
		
		# if 'arr[i]-1' is in 'um' and its length of
		# subsequence is greater than 'len'
		if (arr[i]-1) in um and length < um[arr[i]-1]:
			length = um[arr[i]-1]
		
		# if 'arr[i]' is in 'um' and its length of
		# subsequence is greater than 'len'
		if arr[i] in um and length < um[arr[i]]:
			length = um[arr[i]]
			
		# if 'arr[i]+1' is in 'um' and its length of
		# subsequence is greater than 'len'	
		if (arr[i]+1) in um and length < um[arr[i]+1]:
			length = um[arr[i]+1]
		
		# update arr[i] subsequence length in 'um'
		um[arr[i]] = length + 1
		
		# update maximum length
		if maxLen < um[arr[i]]:
			maxLen = um[arr[i]]
	
	# required maximum length subsequence
	return maxLen

# Driver program to test above


arr = [2, 5, 6, 3, 7, 6, 5, 8]
n = len(arr)
print("Maximum length subsequence =", maxLenSub(arr, n))

# This code is contributed by Rituraj Jain

