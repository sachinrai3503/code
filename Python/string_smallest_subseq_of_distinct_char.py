# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
Given a string s, return the lexicographically smallest subsequence of s that contains
 all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    
    def smallestSubsequence(self, s: str) -> str:
        s_len = len(s)
        last_occ = [-1 for i in range(26)]
        visited = set()
        stck = list()
        for i in range(s_len):
            last_occ[ord(s[i])-97] = i
        for i in range(s_len):
            char = s[i]
            if char in visited: continue
            while len(stck)>0 and (stck[-1]>char and last_occ[ord(stck[-1])-97]>i):
                visited.remove(stck.pop())
            stck.append(char)
            visited.add(char)
        return ''.join(stck)
        
    
    # Assuming both seq have same length
    def compare(self, seq1, seq2, len1):
        if seq1 is None: return 1
        if seq2 is None: return -1
        for i in range(len1):
            if seq1[i]>seq2[i]: return 1
            elif seq1[i]<seq2[i]: return -1
        return 0
    
    # This would timeout
    def smallestSubsequence1(self, s: str) -> str:
        seq = ''
        seq_len = 0
        s_len = len(s)
        mask_count = 1<<s_len
        for i in range(mask_count):
            t_seq = ''
            t_len = 0
            seen = set()
            valid_seq = True
            for j in range(s_len):
                if i&(1<<j):
                    if s[j] not in seen:
                        t_seq+=s[j]
                        t_len+=1
                        seen.add(s[j])
                    else:
                        valid_seq = False
                        break
            # print(t_seq, seen, valid_seq)
            if valid_seq:
                if t_len>seq_len:
                    seq, seq_len = t_seq, t_len
                elif t_len==seq_len and self.compare(seq, t_seq, t_len)==1:
                    seq = t_seq
        return seq