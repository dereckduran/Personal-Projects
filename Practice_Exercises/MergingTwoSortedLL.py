# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

l1 = [2,3,4,5]
l2 = [5,56,3,3,4,5]
print(mergeTwoLists(l1,l2))

nums = [1,2,3,3]
set(nums)
print(nums)