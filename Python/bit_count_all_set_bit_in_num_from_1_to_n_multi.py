# https://leetcode.com/problems/counting-bits/
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-3/
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-2/
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n/
"""
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in 
their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]
"""

class Solution:
    def countSetBit(self, num):
        count = 0
        while num>0:
            count+=1
            num = num - (num&-num)
        return count
    
    #https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-2/
    # See above for hint to logic
    def countTotalSetBit(self, num):
        count = 0
        i, temp = 1, num
        while temp>0:
            quo, rem = (num+1)//(i*2), (num+1)%(i*2)
            count+=(quo*i + (0 if rem<i else rem-i))
            temp = temp//2
            i*=2
        return count
    
    #https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-3/?ref=rp
    def countTotalSetBitDP(self, num):
        if num<=0: return 0, [0]
        if num==1: return 1, [0, 1]
        total_count = 1
        count = [0, 1]
        for n in range(2, num+1):
            if n%2==0: count.append(count[n//2])
            else: count.append(count[n-1]+1)
            total_count+=count[-1]
        return total_count, count
        
    def countBits(self, num: int) -> list[int]:
        total_set_bit = 0
        counts = list()
        for i in range(num+1):
            counts.append(self.countSetBit(i))
            total_set_bit+=counts[-1]
        print('method 1 =',total_set_bit)
        print('method 2 =',self.countTotalSetBit(num))
        total_count, count_list_dp = self.countTotalSetBitDP(num)
        print('method 3 =',total_count)
        return count_list_dp