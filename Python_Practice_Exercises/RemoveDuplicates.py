def removeDuplicates(nums: list[int], val: int) -> int:
    counter = 0
    for number in range(0 , len(nums)- 1):
        if val == nums[number]:
            nums.remove(nums[number])
            counter += 1
        else:
            nums[number - counter] = nums[number]
        

    return len(nums)
'''
hash = {}
counter = 0
for number in nums:
    if number in hash:
        nums.remove(nums[number])
        counter += 1
    hash[number] = number 
    
return len(nums) - counter
'''


print(removeDuplicates([3,2,2,3], 3))