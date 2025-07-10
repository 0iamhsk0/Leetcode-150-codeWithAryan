'''
Name: 151. Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/description/'''

# Approach 1: Using slpit and reversing + joining the list
def reverseWords(s):
    stripped_string = s.split()
    ans = []

    for i in range(len(stripped_string) - 1, -1, -1):
        ans.append(stripped_string[i])
        if i != 0:
            ans.append(" ")

    return "".join(ans) 

# Approach 2: Much simplified join type
def reverseWords1(s):
    return " ".join(reversed(s.split()))

s = "a good   example"
print(reverseWords(s))