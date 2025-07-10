'''
Name: 134. Gas Station
Link: https://leetcode.com/problems/gas-station/description/'''

# Approach 1: Greedy
def canCompleteCitcuit(gas, cost):
    # base case:
    if sum(gas) < sum(cost):
        return -1
    
    gas_tank = 0
    start = 0

    for i in range(len(gas)):
        gas_tank += gas[i] - cost[i]
        if gas_tank < 0:
            gas_tank = 0
            start = i + 1
        
    return start

# Test Case:
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCitcuit(gas, cost)) #4

