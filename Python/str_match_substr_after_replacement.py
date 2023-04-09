# https://leetcode.com/problems/match-substring-after-replacement
"""
You are given two strings s and sub. You are also given a 2D character array mappings
 where mappings[i] = [oldi, newi] indicates that you may perform the following operation
 any number of times:

Replace a character oldi of sub with newi.
Each character in sub cannot be replaced more than once.

Return true if it is possible to make sub a substring of s by replacing zero or more
 characters according to mappings. Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
Output: true
Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'.
Now sub = "l3e7" is a substring of s, so we return true.

Example 2:
Input: s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]
Output: false
Explanation: The string "f00l" is not a substring of s and no replacements can be made.
Note that we cannot replace '0' with 'o'.

Example 3:
Input: s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
Output: true
Explanation: Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'.
Now sub = "l33tb" is a substring of s, so we return true.

Constraints:
1 <= sub.length <= s.length <= 5000
0 <= mappings.length <= 1000
mappings[i].length == 2
oldi != newi
s and sub consist of uppercase and lowercase English letters and digits.
oldi and newi are either uppercase or lowercase English letters or digits.
"""

from typing import List

class Solution:

    def is_match(self, pat_char, txt_char, words_map):
        if txt_char==pat_char: return True
        if pat_char not in words_map: return False
        if txt_char not in words_map[pat_char]: return False
        return True

    def z_function(self, s, s_len, words_map):
        z_arr = [None]
        l, r = 0, 0
        for i in range(1, s_len):
            if i>r:
                l, r = i, i
                while r<s_len and self.is_match(s[r-l], s[r], words_map):
                    r+=1
                z_arr.append(r-l)
                r-=1
            else:
                k = i-l
                if z_arr[k]<(r-i+1):
                    z_arr.append(z_arr[k])
                else:
                    l = i
                    while r<s_len and self.is_match(s[r-l], s[r], words_map):
                        r+=1
                    z_arr.append(r-l)
                    r-=1
        print(f'{z_arr=}')
        return z_arr

    # Z Won't work
    # TC - s = "llllllf", sub = "i1tILf",
    # mapping = [["i", "l"], ["1", "l"], ["t", "l"], ["I", "l"], ["L", "l"]]
    # z_arr=[None, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0]
    # z_str='i1tILf$llllllf' z_len=14
    # The z_arr for 'sub' in sub$s is not factoring in the mapping
    def matchReplacement_Z(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        s_len = len(s)
        sub_len = len(sub)
        words_map = dict()
        for c1, c2 in mappings:
            if c1 in words_map:
                words_map[c1].add(c2)
            else:
                words_map[c1] = {c2}
        print(f'{words_map=}')
        z_str = sub + '$' + s
        z_len = len(z_str)
        z_arr = self.z_function(z_str, z_len, words_map)
        print(f'{z_str=} {z_len=}')
        for i in range(z_len):
            if z_arr[i] and z_arr[i]==sub_len:
                # print(f'{(i-sub_len-1)=}')
                return True
        return False

    def get_lps(self, pat, pat_len):
        lps = list()
        for i in range(pat_len):
            j = i-1
            while j>=0 and pat[lps[j]]!=pat[i]:
                j = lps[j]-1
            if j<0:
                lps.append(0)
            else:
                lps.append(lps[j]+1)
        # print(f'{lps=}')
        return lps
    
    def kmp(self, txt, txt_len, pat, pat_len, pat_lps, words_map):
        i, j = 0, 0
        while i<txt_len and j<pat_len:
            # print(f'before {i=} {j=}')
            if self.is_match(pat[j], txt[i], words_map):
                i+=1
                j+=1
            elif j==0:
                i+=1
            else:
                j = pat_lps[j-1]
            # print(f'after {i=} {j=}')
            if j==pat_len:
                # print(f'found at {i-pat_len}')
                j = pat_lps[j-1]
                return True
        return False

    # KMP Won't work
    # TC - s = "llllllf", sub = "i1tILf",
    # mapping = [["i", "l"], ["1", "l"], ["t", "l"], ["I", "l"], ["L", "l"]]
    # LPS doesn't takes into account the mapping. Getting LPS to consider mapping is difficult
    #  - Same char is mapped to > 1 chars in input mapping list
    #  - while comparing same char can be mapped to 2 different char in s. So, falling 
    #     back(j=lps[j-1]) can get wrong.
    def matchReplacement_KMP(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        s_len = len(s)
        sub_len = len(sub)
        words_map = dict()
        for c1, c2 in mappings:
            if c1 in words_map:
                words_map[c1].add(c2)
            else:
                words_map[c1] = {c2}
        # print(f'{words_map=}')
        sub_lps = self.get_lps(sub, sub_len)
        return self.kmp(s, s_len, sub, sub_len, sub_lps, words_map)

    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        s_len = len(s)
        sub_len = len(sub)
        words_map = dict()
        for c1, c2 in mappings:
            if c1 in words_map:
                words_map[c1].add(c2)
            else:
                words_map[c1] = {c2}
        # print(f'{words_map=}')
        for i in range(s_len-sub_len+1):
            for j in range(sub_len):
                char_s = s[i+j]
                if char_s==sub[j] or char_s in words_map.get(sub[j],{}): continue
                else: break
            else:
                return True
        return False