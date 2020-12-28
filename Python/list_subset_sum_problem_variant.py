# https://www.geeksforgeeks.org/count-of-ways-to-obtain-given-sum-from-the-given-array-elements/
# https://leetcode.com/problems/target-sum/
"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers == S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

def get_sum(nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum

class Solution:
    def findTargetSumWays(self, nums: list[int], S: int) -> int:
        total_sum = get_sum(nums)
        if S<0: S*=-1
        if S>total_sum: return 0
        req_sum = (S+total_sum)/2
        if isinstance(req_sum,float) and not req_sum.is_integer(): return 0
        req_sum = int(req_sum)
        # print(req_sum)
        op = [0]*(req_sum+1)
        for i in range(len(nums)-1, -1, -1):
            for j in range(req_sum, nums[i]-1, -1):
                if j == nums[i]: op[j]+=(1 + op[0])
                elif op[j-nums[i]]!=0: op[j]+=op[j-nums[i]]
        #Here checking for total sum since [1,2,1] can also give sum=0 and in that
        #case no need to add extra 1 for -0.
        if S==0 and total_sum==0:
            return op[req_sum] + 1 #Because 0 and -0 both are needed.
        return op[req_sum]