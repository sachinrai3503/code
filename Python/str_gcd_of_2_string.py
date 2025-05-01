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

    def gcd(self, a, b):
        if b==0:
            return a
        return self.gcd(b, a%b)

    def getLPS(self, s, s_len):
        lps = list()
        for i in range(s_len):
            j = i-1
            while j>-1 and s[i]!=s[lps[j]]:
                j = lps[j]-1
            if j==-1:
                lps.append(0)
            else:
                lps.append(lps[j]+1)
        # print(f'{lps=}')
        return lps[-1]
    
    def getRepeatingString(self, s, s_len):
        lps = self.getLPS(s, s_len)
        if lps==0: return (s, 1) # s is repeating 1s
        if lps<(s_len//2 + (1 if s_len&1==1 else 0)):
            return ('', 0)
        rep_len = s_len - lps
        if (s_len%rep_len)!=0:
            return ('', 0)
        return (s[:rep_len], s_len//rep_len)

    def gcdOfStrings_1(self, str1: str, str2: str) -> str:
        s1_rep, s1_rep_len = self.getRepeatingString(str1, len(str1))
        s2_rep, s2_rep_len = self.getRepeatingString(str2, len(str2))
        if s1_rep=='' or s2_rep=='': return ''
        if s1_rep!=s2_rep: return ''
        return s1_rep*(self.gcd(s1_rep_len, s2_rep_len))

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2)!=(str2+str1): return ''
        return str1[:self.gcd(len(str1), len(str2))]