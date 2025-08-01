'''
Name: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/description/'''

# Approach 1: Using string functions and two pointers, this method taks forever because there are many test cases with different string characters
def isPalindrome1(s):
    seperators = [',', ':', '.', ' ', '_', '@'] #....
    new_s = s.lower()

    for sep in seperators:
        new_s = new_s.replace(sep, '')
    left, right = 0, len(new_s) - 1

    while left < right:
        if new_s[left] != new_s[right]:
            return False
        left += 1
        right -= 1

    return True

# Appraoch 2: Same but simplified
def isPalindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    filtered_string = ''.join(char.lower() for char in s if char.isalnum())
    
    n = len(filtered_string)
    for i in range(n // 2):
        if filtered_string[i] != filtered_string[n - i - 1]:
            return False
    return True

# Approach 3: If reversed string is same as the original then palindrome too

# Test case
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))



