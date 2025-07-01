'''
Name: 45. Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/description/'''

# Approach 1: Greedy Algorithm
def jump(nums):
    current_end = jumps = farthest = 0
    for i in range(len(nums) - 1): 
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
    return jumps



# Test case:
nums = [2,3,1,1,4]
print(jump(nums)) #2
