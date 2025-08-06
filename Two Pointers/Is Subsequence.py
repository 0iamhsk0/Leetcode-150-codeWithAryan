'''
Name: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/description/
'''

# Approach 1: 
def isSubsequence(s, t):
    if len(s) > len(t):
        return False 
    if len(s) == 0:
        return True
    
    left = right = 0
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1
    return left == len(s)

# Test Case:
s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t)) # True
