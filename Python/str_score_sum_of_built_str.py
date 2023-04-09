# https://leetcode.com/problems/sum-of-scores-of-built-strings
# https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/
"""
You are building a string s of length n one character at a time, prepending each
 new character to the front of the string. The strings are labeled from 1 to n, 
 where the string with length i is labeled si.

For example, for s = "abaca", s1 == "a", s2 == "ca", s3 == "aca", etc.
The score of si is the length of the longest common prefix between si and sn
 (Note that s == sn).

Given the final string s, return the sum of the score of every si.

Example 1:
Input: s = "babab"
Output: 9
Explanation:
For s1 == "b", the longest common prefix is "b" which has a score of 1.
For s2 == "ab", there is no common prefix so the score is 0.
For s3 == "bab", the longest common prefix is "bab" which has a score of 3.
For s4 == "abab", there is no common prefix so the score is 0.
For s5 == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.

Example 2:
Input: s = "azbazbzaz"
Output: 14
Explanation: 
For s2 == "az", the longest common prefix is "az" which has a score of 2.
For s6 == "azbzaz", the longest common prefix is "azb" which has a score of 3.
For s9 == "azbazbzaz", the longest common prefix is "azbazbzaz" which has a score of 9.
For all other si, the score is 0.
The sum of the scores is 2 + 3 + 9 = 14, so we return 14.
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:

    def count_matching_prefix_len(self, s, s_len, txt, txt_len):
        i, j = 0, 0
        count = 0
        while i<s_len and j<txt_len and s[i]==txt[j]:
            i+=1
            j+=1
            count+=1
        return count

    # Timeout - O(n2)
    def sumScores_1(self, s: str) -> int:
        score = 0
        s_len = len(s)
        t_s = ""
        for i in range(s_len-1,-1,-1):
            t_s = s[i::]
            ts_len = s_len - i
            score+=self.count_matching_prefix_len(s, s_len, t_s, ts_len)
        return score

    # This is kmp + dp.
    def sumScores_dp(self, s: str) -> int:
        s_len = len(s)
        lps = list()
        dp = list()
        for i in range(s_len):
            dp.append(1)
            j = i-1
            while j>=0 and s[lps[j]]!=s[i]:
                j = lps[j]-1
            if j<0:
                lps.append(0)
            else:
                lps.append(lps[j]+1)
                dp[-1]+=dp[lps[j]]
        # print(f'{lps=}')
        # print(f'{dp=}')
        return sum(dp)
    
    # z_algo
    def sumScores(self, s: str) -> int:
        s_len = len(s)
        z = [s_len]
        l, r = 0, 0
        for i in range(1, s_len):
            if i>r:
                l, r = i, i
                while r<s_len and s[r-l]==s[r]:
                    r+=1
                z.append(r-l)
                r-=1
            else:
                k = i-l
                if z[k]<(r-i+1):
                    z.append(z[k])
                else:
                    l = i
                    while r<s_len and s[r-l]==s[r]:
                        r+=1
                    z.append(r-l)
                    r-=1
        # print(f'{z=}')
        return sum(z)