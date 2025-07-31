'''
Name: 380. Insert Delete GetRandom O(1)
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/'''

# Approach 1: Combining arrays and dictionaries 
class RandomizedSet(object):
    def __init__(self):
        import random
        self.r = random.choice
        self.arr = []
        self.pos = {}

    def insert(self, val):
        return False if val in self.pos else (self.pos.__setitem__(val,len(self.arr)), self.arr.append(val))[1] or True

    def remove(self, val):
        if val not in self.pos: return False
        i = self.pos[val]
        last = len(self.arr) - 1
        if i < last:
            self.arr[i], self.arr[last] = self.arr[last], self.arr[i]
            self.pos[self.arr[i]] = i
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        return self.r(self.arr)
    
    
# Test case
if __name__ == "__main__":
    # Operations and their arguments
    ops = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    args = [[], [1], [2], [2], [], [1], [2], []]
    obj = None
    results = []
    for op, arg in zip(ops, args):
        if op == "RandomizedSet":
            obj = RandomizedSet()
            results.append(None)
        elif op == "insert":
            results.append(obj.insert(arg[0]))
        elif op == "remove":
            results.append(obj.remove(arg[0]))
        elif op == "getRandom":
            results.append(obj.getRandom())
    print("Results:", results)
    