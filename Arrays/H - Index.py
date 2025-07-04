'''
Name: 274. H - Index
Link: https://leetcode.com/problems/h-index/description/'''

# Approach 1: Selection sort

def hindex(citations):
    n = len(citations)
    paper_counts = [0] * (n + 1)
    h = n

    for i in citations[:]:
        paper_counts[min(n, i)] += 1
    
    papers = paper_counts[n]
    while papers < h:
        h -= 1
        papers += paper_counts[h]

    return h

# Test case:
citations = [5,1,2,8,9,3]
print(hindex(citations)) # 3


