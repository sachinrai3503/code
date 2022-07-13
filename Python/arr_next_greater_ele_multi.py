# https://leetcode.com/problems/next-greater-element-i/
"""
The next greater element of some element x in an array is the first greater
 element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1
 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and 
 determine the next greater element of nums2[j] in nums2. If there is no next greater 
 element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element
 as described above.
 
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        stck = list()
        len1 = len(nums1)
        len2 = len(nums2)
        index_map = dict()
        op = [-1 for i in range(len1)]
        for i in range(len1):
            index_map[nums1[i]] = i
        for num in nums2:
            while len(stck)>0 and stck[-1]<num:
                index = index_map.get(stck.pop(), -1)
                if index!=-1:
                    op[index] = num
            stck.append(num)
        return op

# https://leetcode.com/problems/next-greater-element-ii/
"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] 
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order
 next in the array, which means you could search circularly to find its next greater number.
  If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
class Solution2:
    def nextGreaterElements(self, nums):
        length = len(nums)
        op = [-1 for i in range(length)]
        stck = list()
        for i in range(length):
            num = nums[i]
            while len(stck)>0 and nums[stck[-1]]<num:
                op[stck.pop()] = num
            stck.append(i)
        if len(stck)>0:
            for i in range(length):
                num = nums[i]
                while len(stck)>0 and nums[stck[-1]]<num:
                    op[stck.pop()] = num
        return op
    
