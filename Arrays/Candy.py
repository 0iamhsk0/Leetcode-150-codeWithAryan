# '''
# Name: 135.Candy
# Link: https://leetcode.com/problems/candy/description/'''

# # Approach 0: Greedy(ONLY COVERS ONE SIDE - Left to right)

# def candy(ratings):
#     total_candies = len(ratings)
#     current_peak = 0
#     current_valley = 0

#     # Only traversing from left to right:

#     for i in range(1, len(ratings)):
#         # case 1:
#         if ratings[i] == ratings[i - 1]:
#             continue
#         # case 2:
#         elif ratings[i] > ratings[i - 1]:
#             current_peak += 1
#             total_candies += current_peak
#         # case 3:
#         elif ratings[i] < ratings[i - 1]:
#             current_valley += 1
#             total_candies += current_valley

#     # Similarly from right to left needed to be done
    
                
#     return total_candies

# # Test case
# ratings = [6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]
# print(candy(ratings))

# Approach 1: Greedy
def candy1(ratings):
    n = len(ratings)
    total_candies = n
    i = 1

    while i < n:
        if ratings[i] == ratings[i - 1]:
            i += 1
            continue

        current_peak = 0
        while i < n and ratings[i] > ratings[i - 1]:
            current_peak += 1
            total_candies += current_peak
            i += 1
        
        if i == n:
            return total_candies

        current_valley = 0
        while i < n and ratings[i] < ratings[i - 1]:
            current_valley += 1
            total_candies += current_valley
            i += 1

        total_candies -= min(current_peak, current_valley)

    return total_candies

# Approach 2: Greedy simplified

def candy2(ratings):
    cands = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i] < ratings[i + 1] and cands[i] >= cands[i + 1]:
            cands[i + 1] = cands[i] + 1
    for j in range(len(ratings) - 1, 0, -1):
        if ratings[j] < ratings[j - 1] and cands[j] >= cands[j - 1]:
            cands[j - 1] = cands[j] + 1
    return sum(cands)

# Approach 3: Greedy left to right in depth
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


ratings = [6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]
print(candy(ratings))