'''
Name: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

# Approach 1: Two Pointers Technique
from typing import List

def removeDuplicates1(nums):
    if not nums:
        return 0
    
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            nums[k] = nums[i]
            k += 1

    
    return k + 1

# Approach 2: Using set (slow and violates rules)
def removeDuplicates2(nums):
    unique = sorted(set(nums))
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)

# (alt) optimal
def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k

# Test case
nums = [1,1,2]
print(removeDuplicates(nums))        
