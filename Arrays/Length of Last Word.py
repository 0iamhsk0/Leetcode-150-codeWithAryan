'''
Name: 58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/description/
'''

# Approach 1:
def lengthOfLastWord(s):
# Strip any trailing spaces and split the string into words
    words = s.strip().split()
    return len(words[-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s)) # 4
