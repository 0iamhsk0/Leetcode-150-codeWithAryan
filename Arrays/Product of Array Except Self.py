'''
Name: 238. Product of Array Except Self 
Link: https://leetcode.com/problems/product-of-array-except-self/description/
'''

# Approach 1:
from typing import List
def productExceptSelf(nums):
    temp = [1] * len(nums)
    
    left = 1
    for i in range(len(nums)):
        temp[i] *= left
        left *= nums[i]
    
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        temp[i] *= right
        right *= nums[i]

    return temp 

# Test case:
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
