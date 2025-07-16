'''
Name: 6. Zigzag Conversion
Link: https://leetcode.com/problems/zigzag-conversion/'''

# Approach 1:
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    idx, d = 0, 1
    rows = [[] for _ in range(numRows)]

    for char in s:
        rows[idx].append(char)
        if idx == 0:
            d = 1
        elif idx == numRows - 1:
            d = -1
        idx += d

    for i in range(numRows):
        rows[i] = ''.join(rows[i])

    return ''.join(rows)   

# Test case:
s = "PAYPALISHIRING"
numRows = 4 #"PINALSIGYAHRPI"
