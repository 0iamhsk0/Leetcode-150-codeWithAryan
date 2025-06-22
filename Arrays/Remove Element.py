'''
Problem: 27. Remove Element
Link: https://leetcode.com/problems/remove-element/description/
'''

# Approach 1: Two Pointers Technique (In-Place Overwrite Method)
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Test case
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

