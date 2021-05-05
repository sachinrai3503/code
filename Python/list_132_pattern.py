# https://leetcode.com/problems/132-pattern/
"""
Given an array of n integers nums, a 132 pattern is a subsequence of three
 integers nums[i], nums[j] and nums[k] such that i < j < k and
  nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or
 the O(n) solution?

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: 
    [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 
Constraints:
n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
"""
from sys import maxsize

def get_greatest_element_before(nums):
    length = len(nums)
    stck = list()
    op = [-1 for i in range(length)]
    for i in range(length-1, -1, -1):
        t_num = nums[i]
        while len(stck)>0 and t_num>nums[stck[-1]]:
            op[stck[-1]] = i
            stck.pop()
        stck.append(i)
    while len(stck)>0:
        op[stck[-1]] = -1
        stck.pop()
    return op
    
def get_min_element(nums):
    length = len(nums)
    op = [-1 for i in range(length)]
    _min = -1
    for i in range(length):
        if _min==-1 or nums[i]<nums[_min]:
            _min = i
            op[i] = _min
        else:
            op[i] = op[i-1]
    return op

def get_farthest_smallest_element(nums, prefix_min_element, from_index):
    index = -1
    s = 0
    e = from_index-1
    while s<=e:
        mid = s + (e-s)//2
        if nums[prefix_min_element[mid]]<nums[from_index]:
            index = prefix_min_element[mid]
            e = mid-1
        else:
            s = mid+1
    return index

class Solution:
    def find132pattern_2(self, nums: list[int]) -> bool:
        greatest_element_before = get_greatest_element_before(nums)
        prefix_min_element = get_min_element(nums)
        # print(greatest_element_before)
        # print(prefix_min_element)
        length = len(nums)
        for i in range(length):
            greatest_ele_index = greatest_element_before[i]
            prefix_min_index = get_farthest_smallest_element(nums,prefix_min_element, i)
            if greatest_ele_index==-1 or prefix_min_index==-1: continue
            if greatest_ele_index>prefix_min_index: return True
        return False
    
    def find132pattern(self, nums: list[int]) -> bool:
        length = len(nums)
        stck = list()
        third_ele = -1*maxsize
        for i in range(length-1, -1, -1):
            if nums[i]<third_ele: return True
            while len(stck)>0 and nums[i]>stck[-1]:
                third_ele = stck[-1]
                stck.pop()
            stck.append(nums[i])
            # print(stck)
        return False