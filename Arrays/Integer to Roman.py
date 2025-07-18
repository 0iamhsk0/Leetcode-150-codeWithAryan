'''
Name: 12. Integer to Roman
Link: https://leetcode.com/problems/integer-to-roman/description/'''

# Approach 1: Hash table/Mapping using dictionaries

def intToRoman(num):
    M = ['', 'M', 'MM', 'MMM']
    C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] 
    
    return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]     

# Test case: 
num = 465
print(intToRoman(num)) #CDLXV