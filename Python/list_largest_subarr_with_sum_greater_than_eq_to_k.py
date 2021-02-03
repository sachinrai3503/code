# https://www.geeksforgeeks.org/largest-subarray-having-sum-greater-than-k/
# https://www.geeksforgeeks.org/longest-subarray-with-sum-greater-than-equal-to-zero/
"""
Given an array of integers and a value k, find the length of largest subarray
 having a sum greater than k.

Examples:

Input : arr[] = {-2, 1, 6, -3}, k = 5
Output : 2
Largest subarray with sum greater than
5 is  {1, 6}.

Input : arr[] = {2, -3, 3, 2, 0, -1}, k = 3
Output : 5
Largest subarray with sum greater than
3 is {2, -3, 3, 2, 0}.
"""

# NOTE - For smallest subarr see - list_smallest_subarr_with_sum_greater_than_eq_to_k.py

from sys import maxsize

class Solution:
    
    def get_floor(self, stck, num):
        floor = -1
        s, e = 0, len(stck)-1
        while s<=e:
            mid = s + (e-s)//2
            if stck[mid][0]<num:
                floor = mid
                e = mid-1
            else:
                s = mid+1
        return floor if floor==-1 else stck[floor][1]
    
    def longestSubarray(self, A: list[int], K: int) -> int:
        length = len(A)
        max_len = -maxsize
        stck = list()
        t_sum = 0
        i = 0
        while i<length:
            t_sum+=A[i]
            if t_sum>K:
                max_len = i+1
            floor = self.get_floor(stck, t_sum-K)
            if floor!=-1 and (i-floor)>max_len:
                max_len = i-floor
            if len(stck)>0:
                if stck[-1][0]>t_sum:
                    stck.append([t_sum, i])    
            else:
                stck.append([t_sum, i])
            i+=1
        return max_len if max_len!=-maxsize else -1

def main():
    ip = [-2, 1, 6, -3]
    K = 5
    print('ip>',ip)
    print('K>',K)
    sol = Solution()
    print('Max len =',sol.longestSubarray(ip,K))

if __name__ == '__main__':
    main()