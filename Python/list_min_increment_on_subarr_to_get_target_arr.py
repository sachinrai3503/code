# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
"""
Given an array of positive integers target and an array initial of same size with all zeros.

Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:

Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.
 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).
Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).
Example 4:

Input: target = [1,1,1,1]
Output: 1
 
Constraints:

1 <= target.length <= 10^5
1 <= target[i] <= 10^5
"""
from sys import maxsize

def get_index_map(nums):
    index_map = {}
    for i in range(len(nums)):
        num = nums[i]
        index_list = index_map.get(num,None)
        if index_list is None:
            index_list = list()
            index_map[num] = index_list
        index_list.append(i)
    return index_map

class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        index_map = get_index_map(target)
        # print(index_map)
        length = len(target)
        count = 0
        base_element = 0
        is_done = [False]*length
        active_partition = 1
        remaining = length
        for num, index_list in sorted(index_map.items()):
            count+=((num-base_element)*active_partition)
            for index in index_list:
                is_done[index] = True
                if index!=0 and index!=length-1:
                    if not is_done[index-1] and not is_done[index+1]:
                        active_partition+=1
                if (index==0 or is_done[index-1]) and (index==length-1 or is_done[index+1]):
                    active_partition-=1
            base_element = num
            # print(num,base_element,is_done,active_partition,'count=',count)
        return count