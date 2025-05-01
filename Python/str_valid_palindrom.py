# https://leetcode.com/problems/valid-palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
 all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome. 

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        allowed_char = ascii_letters + digits
        i, j = 0, s_len-1
        while i<j:
            while i<j and s[i] not in allowed_char:
                i+=1
            while j>i and s[j] not in allowed_char:
                j-=1
            if i==j: return True
            elif s[i].lower()!=s[j].lower(): return False
            i+=1
            j-=1
        return True