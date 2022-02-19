# https://leetcode.com/problems/longest-duplicate-substring/
"""
Given a string s, consider all duplicated substrings: (contiguous) substrings of s
 that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not
 have a duplicated substring, the answer is "".

Example 1:
Input: s = "banana"
Output: "ana"

Example 2:
Input: s = "abcd"
Output: ""

Constraints:
2 <= s.length <= 3 * 104
s consists of lowercase English letters.
"""

class Solution:
    
    def compare(self, s, s_len, i, j, com_len):
        # print(s, s_len, i, j, com_len)
        for k in range(com_len):
            if s[i+k]!=s[j+k]: return False
        return True
    
    # It can add O(n^2) to the overall complexity if q is not choosen properly.
    def check_substr_with_len_k(self, s, s_len, k):
        d = 26 # no of char
        # prime number. Small q will cause more collision in hash_index_map.
        # Too big q will cause many unique keys & key lookup time will increase. 
        q = 10**6+7
        h = (d**(k-1))%q
        hash_index_map = dict() # hash:index_list
        t_hash = 0
        for i in range(s_len):
            t_hash = (t_hash*d + (ord(s[i])-97))%q
            if i>=(k-1):
                index_list = hash_index_map.get(t_hash, list())
                for index in index_list:
                    if self.compare(s, s_len, index, i-k+1, k): return index
                index_list.append(i-k+1)
                hash_index_map[t_hash] = index_list
                t_hash = t_hash - (ord(s[i-k+1])-97)*h
        return -1
    
    # This doesn't do mod and adds only O(n) to the overall complexity.
    # But since no mod, too many values in set. So, lookup time in set increases.
    def check_substr_with_len_k_1(self, s, s_len, k):
        d = 26 # no of char
        q = 17 # prime number
        h = d**(k-1)
        hash_set = set()
        t_hash = 0
        for i in range(s_len):
            t_hash = t_hash*d + (ord(s[i])-97) # Not doing mod here
            if i>=(k-1):
                if t_hash in hash_set:  return i-k+1
                hash_set.add(t_hash)
                t_hash = t_hash - (ord(s[i-k+1])-97)*h
        return -1
    
    # This is using binary search + rolling hash(Rabin Karp)
    def longestDupSubstring(self, s_str: str) -> str:
        op_len = 0
        op_index = -1
        s_len = len(s_str)
        s, e = 1, s_len-1
        while s<=e:
            mid = s + (e-s)//2
            t_index = self.check_substr_with_len_k(s_str, s_len, mid)
            if t_index!=-1:
                op_index = t_index
                op_len = mid
                s = mid+1
            else:
                e = mid-1
        return s_str[op_index:op_index+op_len]
                
        
    def get_lps(self, s):
        max_lps = 0
        s_len = len(s)
        lps = [0 for i in range(s_len)]
        for i in range(s_len):
            j = i-1
            while j>-1 and s[lps[j]]!=s[i]:
                j = lps[j]-1
            if j==-1:
                lps[i] = 0
            else:
                lps[i] = lps[j]+1
            max_lps = max(max_lps, lps[i])
        # print(s, lps, max_lps)
        return max_lps
        
    # This is based on LPS from KMP. O(n^2) time complexity.
    def longestDupSubstring_lps(self, s: str) -> str:
        op_len = 0
        op = None
        s_len = len(s)
        for i in range(s_len):
            max_lps = self.get_lps(s[i:])
            if max_lps>op_len:
                op_len = max_lps
                op = s[i:i+op_len]
            if op_len==(s_len-i-1): break
        return op if op is not None else ""