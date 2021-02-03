# https://www.geeksforgeeks.org/find-subarray-with-given-sum/
# https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
# https://www.geeksforgeeks.org/find-subarray-with-given-sum-with-negatives-allowed-in-constant-space/
# https://leetcode.com/problems/subarray-sum-equals-k/

# Note - Link 1 - Is only for non-negative integers - Sliding window
# Link 2 - Handles +ve & -ve integers - Using map
# Link 3 - Tries to handle +ve & -ve - Wrong solution 
#          ip_arr=[84,-37,32,40,95], sum = 167 
#          it gives "no subarray" but answer is actually [32,40,95]


"""
Given an array of integers nums and an integer k, return the total number of
 continuous subarrays whose sum equals to k. 

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

class Solution:
    
    # This would print the subarray also
    # https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
    # https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/
    def subarraySum1(self, nums: list[int], k: int) -> int:
        count = 0
        sum_index_map = dict()
        length = len(nums)
        t_sum = 0
        i = 0
        while i<length:
            t_sum+=nums[i]
            if t_sum==k:
                count+=1
                print(nums[:i+1])
            t_list = sum_index_map.get(t_sum-k, None)
            if t_list is not None:
                count+=(len(t_list))
                for index in t_list:
                    print(nums[index+1: i+1])
            if not sum_index_map.__contains__(t_sum):
                sum_index_map[t_sum] = list()
            sum_index_map[t_sum].append(i)
            i+=1
        return count

    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum_index_map = dict()
        length = len(nums)
        t_sum = 0
        i = 0
        while i<length:
            t_sum+=nums[i]
            if t_sum==k:
                count+=1
            if t_sum-k in sum_index_map:
                count+=sum_index_map.get(t_sum-k)
            sum_index_map[t_sum] = (sum_index_map[t_sum] + 1) if t_sum in sum_index_map else 1
            i+=1
        return count