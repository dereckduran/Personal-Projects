def longestcommonsubsequence(nums):
    hash = set()
    longest = 0
    n = len(nums)
    for i in nums:
        hash.add(i)
    
    for i in range(n):
        if nums[i] - 1 not in hash: #checking if this is starting point

            j = nums[i] 
            while j in hash: #incrementing a counter
                j+= 1
            
            longest = max(longest, j - nums[i]) #resetting longest streak if needed

    return longest

print(longestcommonsubsequence([1, 9, 3, 10, 4, 20 , 2]))