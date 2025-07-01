'''
Name: 45. Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/description/'''

# Approach 1: Greedy Algorithm
def jump(nums):
    max_jump = 0
    for i in range(len(nums)):
        if i > max_jump:
            return False
        max_jump = max(max_jump, i + nums[i])
    return True

# Test case:
nums = [2,3,1,1,4]
print(jump(nums)) #True
