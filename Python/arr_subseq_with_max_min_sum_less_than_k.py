# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
"""
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum
 and maximum element on it is less or equal to target. Since the answer may be too
 large, return it modulo 109 + 7.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the 
 condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106
"""

class Solution:
    
    def ceil(self, nums, s, e, _max, maxsum):
        _ceil = e+1
        while s<=e:
            mid = s + (e-s)//2
            t_sum = _max + nums[mid]
            if t_sum<=maxsum:
                s = mid+1
            else:
                _ceil = mid
                e = mid-1
        return _ceil
    
    def floor(self, nums, s, e, _min, maxsum):
        _floor = -1
        while s<=e:
            mid = s + (e-s)//2
            t_sum = _min + nums[mid]
            if t_sum<=maxsum:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor
    
    # This method is same as sliding window but just using binary search to set next i & j.
    # Not a fast method. numSubseq(...) is more fast
    def numSubseq1(self, nums: list[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        count = 0
        i, j = 0, length-1
        while i<=j:
            t_sum = nums[i] + nums[j]
            total_possiblities = (1<<(j-i+1)) - 1
            if t_sum>target:
                j = self.floor(nums, i, j, nums[i], target)
            else:
                t_i = self.ceil(nums, i, j, nums[j], target)
                count+=(total_possiblities-((1<<(j-t_i+1))-1))
                i = t_i
        return count%(10**9 + 7)
    
    def numSubseq(self, nums: list[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        total_possiblities = 0
        i, j = 0, length-1
        while i<=j:
            t_sum = nums[i]+nums[j]
            if t_sum>target:
                j-=1
            else:
                total_possiblities+=(1<<(j-i))
                i+=1
        return total_possiblities%(1000000007)