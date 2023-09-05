# https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t
  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2. 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:
Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""
 
Constraints:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
#  C version in string_gcd_of_2_string.c

class Solution:

    def match_substr(self, s1, s1_len, s2, s2_len): # len(s2)<=len(s1)
        if s1_len<s2_len: return False
        if (s1_len%s2_len)!=0: return False
        i = 0
        while i<s1_len:
            j = 0
            while i<s1_len and j<s2_len:
                if s1[i]!=s2[j]: return False
                i+=1
                j+=1
            if i==s1_len and j!=s2_len: return False
        return True

    # O(m*n) time complexity
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)
        small_str, small_str_len = None, 0
        if str1_len<=str2_len:
            small_str, small_str_len = str1, str1_len
        else:
            small_str, small_str_len = str2, str2_len
        i = 1 # substr repeat count
        while (small_str_len//i)>0:
            if (small_str_len%i)==0:
                t_len=small_str_len//i
                # print(f'{t_len=}')
                t_str = small_str[:t_len]
                if self.match_substr(str1, str1_len, t_str, t_len) and self.match_substr(str2, str2_len, t_str, t_len):
                    return t_str
            i+=1
        return ""

    def get_lps(self, s, s_len):
        lps = list()
        i = 0
        for i in range(s_len):
            j = i-1
            while j>=0 and s[lps[j]]!=s[i]:
                j = lps[j]-1
            if j<0:
                lps.append(0)
            else:
                lps.append(lps[j]+1)
        return lps[-1]

    def compare(self, s1, s2, s_len):
        for i in range(s_len):
            if s1[i]!=s2[i]: return False
        return True

    def is_valid(self, s_len, s_lps, s_rep_chars_count):
        if s_lps==0: return True
        if s_lps<((s_len+1)//2): return False
        if (s_len%s_rep_chars_count)!=0: return False
        return True

    def gcd(self, a, b):
        if b==0: return a
        return self.gcd(b,a%b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)
        str1_lps = self.get_lps(str1, str1_len)
        str2_lps = self.get_lps(str2, str2_len)
        str1_rep_chars_count = str1_len - str1_lps
        str2_rep_chars_count = str2_len - str2_lps
        # print(f'{str1_len=} {str1_lps=} {str1_rep_chars_count=}')
        # print(f'{str2_len=} {str2_lps=} {str2_rep_chars_count=}')
        if not self.is_valid(str1_len, str1_lps, str1_rep_chars_count) or \
            not self.is_valid(str2_len, str2_lps, str2_rep_chars_count):
            # print('Here')
            return ""
        if str1_rep_chars_count!=str2_rep_chars_count: return ""
        if not self.compare(str1, str2, str1_rep_chars_count): return ""
        return str1[:self.gcd(str1_len, str2_len)]