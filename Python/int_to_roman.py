# https://leetcode.com/problems/integer-to-roman/
# https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
# https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
 12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
 which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
 However, the numeral for four is not IIII. Instead, the number four is written
 as IV. Because the one is before the five we subtract it making four. The same
 principle applies to the number nine, which is written as IX. There are six
 instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Constraints:
1 <= num <= 3999
"""

class Solution:

    def __init__(self):
        self.roman_dict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    
    def to_roman(self, digit, factor):
        num = digit*factor
        if num==0: 
            return None
        if num in self.roman_dict:
            return self.roman_dict[num]
        elif digit==4 or digit==9:
            return self.roman_dict[factor] + self.roman_dict[num+factor]
        op = ''
        if 5<digit<=8:
            op = self.roman_dict[5*factor]
            digit-=5
        op+=self.roman_dict[1*factor]*digit
        return op 
            

    def intToRoman(self, num: int) -> str:
        roman_num = ''
        factor = 1
        while num>0:
            digit = num%10
            if digit!=0:
                roman_num = self.to_roman(digit, factor) + roman_num
            num//=10
            factor*=10
        return roman_num