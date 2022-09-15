# https://leetcode.com/problems/sequential-digits/
"""
An integer has sequential digits if and only if each digit in the number is one more
 than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have
 sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9
"""

class Solution:
    
    def count_digit(self, n):
        count = 0
        while n>0:
            # print(n)
            count+=1
            n//=10
        return count
    
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        op = list()
        # Digit count : smallest number
        start_from_dict = {2:12, 3:123, 4:1234, 5:12345, 6:123456, 7:1234567, 8:12345678, 9:123456789}
        low_digit_count = self.count_digit(low)
        high_digit_count = min(self.count_digit(high), 9)
        # print(low_digit_count, high_digit_count)
        while low_digit_count<=high_digit_count:
            start_from = start_from_dict.get(low_digit_count)
            q = 10**(low_digit_count-1)
            last_digit = start_from%10
            while last_digit!=10:
                if start_from>high: return op
                if start_from>=low: op.append(start_from)
                last_digit+=1
                start_from = (start_from%q)*10 + (last_digit)
            low_digit_count+=1
        return op