'''
Name: 189. Rotate Array
Link: https://leetcode.com/problems/rotate-array/'''

from typing import List
# Approach 1: Universal reversal algorithm
class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k %= n

        self.reverse_nums(nums, 0, n-1)
        self.reverse_nums(nums, 0, k-1)
        self.reverse_nums(nums, k, n-1)


    def reverse_nums(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    
# Approach 2: Using pop
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
 
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

# Approach 3: Slicing(best)
def rotate(nums, k):
    n = len(nums)
    k %= n
    temp = nums[-k:] + nums[:-k]
    nums[:] = temp
    return nums
        
# Test case:
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k)) #[5, 6, 7, 1, 2, 3, 4]