# https://leetcode.com/problems/find-the-closest-palindrome/
"""
Given a string n representing an integer, return the closest integer
 (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 
Constraints:
1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
"""

class Solution:
    
    def decrement(self, num_arr):
        length = len(num_arr)
        i = length-1
        while i>=0 and num_arr[i]==0:
            num_arr[i]=9
            i-=1
        num_arr[i]-=1
    
    def get_next_smallest_number(self, num_arr):
        length = len(num_arr)
        mid = (length-1)//2
        t_num = num_arr[:mid+1]
        self.decrement(t_num)
        if t_num[0]==0:
            del(num_arr)
            return [9 for i in range(length-1)]
        else:
            for i in range(mid+1):
                num_arr[i], num_arr[-(i+1)] = t_num[i], t_num[i]
            return num_arr
    
    def increment(self, num_arr):
        length = len(num_arr)
        i = length-1
        while i>=0 and num_arr[i]==9:
            num_arr[i]=0
            i-=1
        if i==-1: return 1
        num_arr[i]+=1
        return 0
    
    def get_next_larger_number(self, num_arr):
        length = len(num_arr)
        mid = (length-1)//2
        t_num = num_arr[:mid+1]
        carry = self.increment(t_num)
        if carry == 1:
            del(num_arr)
            t_arr = [0 for i in range(length+1)]
            t_arr[0], t_arr[-1] = 1, 1
            return t_arr
        else:
            for i in range(mid+1):
                num_arr[i], num_arr[-(i+1)] = t_num[i], t_num[i]
            return num_arr
    
    def make_palin(self, n_int_arr):
        length = len(n_int_arr)
        mid = (length-1)//2
        i = 0
        while i<=mid:
            n_int_arr[-(i+1)] = n_int_arr[i]
            i+=1
        return n_int_arr
    
    def compare(self, num_arr1, num_arr2):
        len1 = len(num_arr1)
        len2 = len(num_arr2)
        if len1>len2: return 1
        if len1<len2: return -1
        for i in range(len1):
            if num_arr1[i]<num_arr2[i]: return -1
            elif num_arr1[i]>num_arr2[i]: return 1
        return 0
    
    def to_int(self, num_arr):
        n = 0
        for num in num_arr:
            n = n*10 + num
        return n
    
    def nearestPalindromic(self, n: str) -> str:
        n_int = int(n)
        if n_int<=0: return None
        if n_int<=10: return str(n_int-1)
        if n_int==11: return '9'
        n_int_arr = [int(num) for num in n]
        palin_n_arr = self.make_palin(list(n_int_arr))
        # print(n_int_arr, palin_n_arr)
        compare_res = self.compare(n_int_arr, palin_n_arr)
        next_smaller_int_arr = None
        next_greater_int_arr = None
        if compare_res==0:
            next_smaller_int_arr = self.get_next_smallest_number(list(n_int_arr))
            next_greater_int_arr = self.get_next_larger_number(list(n_int_arr))
        elif compare_res==-1:
            next_smaller_int_arr = self.get_next_smallest_number(list(n_int_arr))
            next_greater_int_arr = palin_n_arr
        else:
            next_smaller_int_arr = palin_n_arr
            next_greater_int_arr = self.get_next_larger_number(list(n_int_arr))
        # print('--', next_smaller_int_arr, next_greater_int_arr)
        smaller_int = self.to_int(next_smaller_int_arr)
        greater_int = self.to_int(next_greater_int_arr)
        if (n_int-smaller_int)<=(greater_int-n_int):
             return str(smaller_int)
        else:
             return str(greater_int)