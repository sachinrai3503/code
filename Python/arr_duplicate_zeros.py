# https://leetcode.com/problems/duplicate-zeros/
"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting
 the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the
 above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
class Solution:

    # O(n) space
    def duplicateZeros1(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        zero_count = [0 for i in range(length)]
        t_count = 0
        for i in range(length):
            if arr[i]==0: t_count+=1
            zero_count[i] = t_count
        # print(zero_count)
        for i in range(length-1,-1,-1):
            z_count = 0 if i==0 else zero_count[i-1]
            t_i = i + z_count
            if t_i<length:
                arr[t_i] = arr[i]
                if arr[t_i]==0 and (t_i+1)<length:
                    arr[t_i+1] = 0
        
    # O(1) space
    def duplicateZeros(self, arr: list[int]) -> None:
        zero_count = 0
        length = len(arr)
        i = 0
        while i<length:
            if (i+zero_count) >= length: break
            if arr[i]==0: zero_count+=1
            i+=1
        if i==length: return # Either no 0's or [1,1,1,0]
        # print('i',i)
        k = i-1
        j = length-1
        while k>=0:
            arr[j] = arr[k]
            j-=1
            if arr[k]==0 and (k!=(i-1) or (k+zero_count)<length):
                arr[j] = 0
                j-=1
            k-=1
        return