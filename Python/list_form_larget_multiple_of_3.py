# https://leetcode.com/problems/largest-multiple-of-three/
# https://www.geeksforgeeks.org/find-the-largest-number-multiple-of-3/
# https://www.geeksforgeeks.org/find-largest-multiple-3-array-digits-set-2-time-o1-space/
"""
Given an integer array of digits, return the largest multiple of three that can
 be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

Example 1:
Input: digits = [8,1,9]
Output: "981"

Example 2:
Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""

Example 4:
Input: digits = [0,0,0,0,0,0]
Output: "0"
 
Constraints:
1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.
"""
class Solution:
    
    def get_freq(self, digits):
        freq = [0 for i in range(10)]
        for digit in digits:
            freq[digit]+=1
        return freq
    
    def remove_digit(self, freq, rem1, rem2):
        """
        Tries to find 1 num with rem as rem1 or 2 nums with rem as rem2
        """
        i = rem1
        while i<10:
            if freq[i]>0:
                freq[i]-=1
                return
            i+=3
        count = 0
        i = rem2
        while i<10:
            if freq[i]>=2:
                freq[i]-=2
                count+=2
            elif freq[i]==1:
                freq[i]=0
                count+=1
            if count==2:
                return
            i+=3
    
    def get_num_as_str(self, freq):
        num = list()
        for i in range(9, -1, -1):
            if freq[i]>0:
                num.extend([chr(i+48)]*freq[i])
        num_str = ''.join(num)
        if num_str!='' and num_str[0]=='0': return '0'
        return num_str
    
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        total_sum = sum(digits)
        freq = self.get_freq(digits)
        rem = total_sum%3
        if rem==1:
            self.remove_digit(freq, 1, 2)
        elif rem==2:
            self.remove_digit(freq, 2, 1)
        return self.get_num_as_str(freq)
        
        