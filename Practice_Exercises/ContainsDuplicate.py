from ast import Return
from operator import truediv


def findDuplicates( nums: list[int]) -> list[int]:
    output = []
    """
        Since we have to solve this problem in constant space complexity so the only way is to use the space of given array and manipulate it.
        Since the elements in the array are in range [1..n], we can consider the elements as idexes also and to be precise (element - 1) as it is a 0-indexed array.
        Since we can't use any extra space so let us mark the elements encountered in the given array only. This can be done by multiplying the element with -1.
        Now for each element, we will treat it as the index and check whether the value present at that index is visited or not. If it is visited then it is a duplicate else we mark that element as visited(multiply by -1).
    """
    for num in nums:
        if nums[abs(num) - 1] < 0:
            output.append(abs(num))

        else:
            nums[abs(num) - 1] *= -1
    return output

print(findDuplicates([1,2,1]))