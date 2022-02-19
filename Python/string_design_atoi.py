# https://leetcode.com/problems/string-to-integer-atoi/
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit 
 signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
 Read in and ignore any leading whitespace.
 Check if the next character (if not already at the end of the string) is '-' or '+'.
     Read this character in if it is either. This determines if the final result is negative
     or positive respectively. Assume the result is positive if neither is present.
 Read in next the characters until the next non-digit character or the end of the
  input is reached. The rest of the string is ignored.
 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits
  were read, then the integer is 0. Change the sign as necessary (from step 2).
 If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then
  clamp the integer so that it remains in the range. Specifically, integers less
  than -231 should be clamped to -231, and integers greater than 231 - 1 should be
  clamped to 231 - 1.
 
Return the integer as the final result.
Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the
 string after the digits. 

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42

Example 3:
Input: s = "4193 with words"
Output: 4193

Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+',
 '-', and '.'.
"""
class Solution:
    
    # This is using finite automata
    def myAtoi(self, s:str) -> int:
        TA = [[0,1,1,2],[2,2,1,2]] # ' ', +-, [0-9], .[A-Z][a-z]
        max_num = 1<<31
        s_len = len(s)
        state = 0
        num = 0
        sign = 1
        for i in range(s_len):
            char = s[i]
            col = None
            if char==' ': col = 0
            elif char in '+-': col = 1
            elif '0'<=char<='9': col = 2
            else: col = 3
            state = TA[state][col]
            if state==2: break
            if state==1:
                if col==1:
                    if char=='-': sign = -1
                else:
                    num = num*10 + (ord(char)-48)
                    if num>=max_num:
                        break
        if sign==-1: return sign*min(num, max_num)
        return min(num, max_num-1)
    
    def myAtoi_str(self, s: str) -> int:
        num = 0
        sign = 1
        max_num = 1<<31
        num_flag = False
        s_len = len(s)
        for i in range(s_len):
            char = s[i]
            if char=='.' or 'a'<=char<='z' or 'A'<=char<='Z':
                break
            elif char==' ':
                if num_flag: break
            elif char=='+' or char=='-':
                if num_flag: break
                if char=='-': sign = -1
                num_flag = True
            else:
                num = num*10 + (ord(char)-48)
                if num>=max_num:
                    break
                num_flag = True
        if sign==-1: return sign*min(num, max_num)
        return min(num, max_num-1)