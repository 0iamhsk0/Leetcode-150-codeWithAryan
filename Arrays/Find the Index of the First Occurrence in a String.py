'''
Name: 28. Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/'''

# Approach 1: Slicing
def strStr(haystack, needle):

    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

# Test case
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))