'''
Problem: 88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
'''

# Approach 1: Slice and Sort (simple, but not optimal)
def merge_v1(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()

# Approach 2: Two Pointers
def merge_v2(nums1, m, nums2, n):
    m1, n1, r = m - 1, n - 1, m + n - 1

    while m1 >= 0 and n1 >= 0:
        if nums1[m1] > nums2[n1]:
            nums1[r] = nums1[m1]
            m1 -= 1
        else:
            nums1[r] = nums2[n1]
            n1 -= 1
        r -= 1

    while n1 >= 0:
        nums1[r] = nums2[n1]
        r -= 1
        n1 -= 1

# (alt)
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]

# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
