'''
Name: 169. Majority Element
Link: https://leetcode.com/problems/majority-element/description/
'''

# Approach 1: Using the mentioned conditions
def majorityElement1(nums):
    n = len(nums)
    nums.sort()
    return nums[n//2]


# Approach 2: Using in built Counter
from collections import Counter
from typing import List

def majorityElement(self, nums: List[int]) -> int:
    count = Counter(nums)
    return max(count.keys(), key=count.get)


# Approach 3: Using Baoyer-Moore Voting Algorithm
def majorityElement(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Test case
nums = [3, 2, 3]
print(majorityElement(nums))