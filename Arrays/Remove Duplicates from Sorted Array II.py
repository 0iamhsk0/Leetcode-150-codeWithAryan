'''
Name: 80. Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/'''

# Approach 1:
def removeDuplicates(nums):
    slow = 2
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow

# Test case:
nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))