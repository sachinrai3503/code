# https://leetcode.com/problems/regular-expression-matching/
"""
Given an input string (s) and a pattern (p), implement regular expression
 matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
 
Constraints:
0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Pat:
    def __init__(self, char, is_astric, is_nullable):
        self.char = char
        self.is_astric = is_astric
        self.is_nullable = is_nullable
    
    def __str__(self):
        return self.char + ' ' + str(self.is_astric) + ' ' + str(self.is_nullable)
    
    def __repr__(self):
        return self.char + ':' + str(self.is_astric) + ':' + str(self.is_nullable)

class Solution(object):
    def compress_pattern(self, pattern):
        pat_len = len(pattern)
        op = list()
        is_nullable = True
        i = pat_len-1
        while i>=0:
            if pattern[i]=='*' and i-1>=0:
                op.insert(0, Pat(pattern[i-1], True, is_nullable))
                i-=2
            else:
                is_nullable = False
                op.insert(0, Pat(pattern[i], False, is_nullable))
                i-=1
        # print(op)
        return op

    def is_matching(self, s, t_p):
        s_len = len(s)
        p_len = len(t_p)
        if s_len==0:
            return True if p_len==0 else t_p[0].is_nullable
        if p_len==0:
            return False
        op = [False for k in range(s_len)]
        for i in range(p_len-1, -1, -1):
            prev = False
            for j in range(s_len-1, -1, -1):
                t_prev = op[j]
                pat = t_p[i].char
                txt = s[j]
                is_match = (pat=='.' or txt==pat)
                if t_p[i].is_astric == False:
                    if not is_match:
                        op[j] = False
                    else:
                        if i==p_len-1 and j==s_len-1: op[j] = True
                        elif j==s_len-1: op[j] = t_p[i+1].is_nullable
                        else: op[j] = prev
                else:
                    skip_pat = False if (i==p_len-1) else op[j]
                    use_txt  = is_match and (op[j+1] if (j<s_len-1) else t_p[i].is_nullable)
                    op[j] = (skip_pat or use_txt)
                prev = t_prev
                # print(op)
        return op[0]
                
    def isMatch(self, text, pattern):
        t_p = self.compress_pattern(pattern)
        return self.is_matching(text, t_p)