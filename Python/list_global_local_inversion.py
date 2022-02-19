class BIT:
    def __init__(self, length):
        self.length = length
        self.bit = [0 for i in range(length)]
    
    def update(self, index, value):
        while index<self.length:
            self.bit[index]+=value
            index = index + (index&-index)
    
    def query(self, index):
        t_sum = 0
        while index>0:
            t_sum+=self.bit[index]
            index = index - (index&-index)
        return t_sum

class Solution:

    # This would time out
    def isIdealPermutation2(self, nums: list[int]) -> bool:
        length = len(nums)
        bit = BIT(length+1)
        g_inv_count, l_inv_count = 0, 0
        for i in range(length-1,-1,-1):
            num = nums[i]
            g_inv_count+=bit.query(num)
            bit.update(num+1, 1)
            l_inv_count+=(1 if (i!=0 and nums[i-1] > nums[i]) else 0)
        # print(g_inv_count, l_inv_count)
        return g_inv_count==l_inv_count
        
    # https://leetcode.com/problems/global-and-local-inversions/discuss/1499983/Python-3-straightfoward-O(n)-with-explanation
    # https://leetcode.com/problems/global-and-local-inversions/discuss/1509656/O(N)-and-O(NlogN)-(two-C%2B%2B-solutions)
    def isIdealPermutation(self, nums: list[int]) -> bool:
        length = len(nums)
        for i in range(length):
            if abs(nums[i]-i)>1:
                return False
        return True