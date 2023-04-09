# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
"""
Given a string s and an integer k, return the length of the longest substring of
 s such that the frequency of each character in this substring is greater than or
 equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b'
 is repeated 3 times.

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""

class Solution:
    
    def get_freq(self, string, s, e):
        freq = {}
        for i in range(s,e+1):
            char = string[i]
            char_freq = freq.get(char, 0)
            freq[char] = char_freq+1
        # print(f'{freq=}')
        return freq
    
    def find_longest_substr(self, string, s, e, cur_freq, k):
        if s>e: return 0
        max_len_str = 0
        t_freq = {}
        t_s = s
        for i in range(s, e+1):
            char = string[i]
            char_freq = t_freq.get(char, 0)
            t_freq[char] = char_freq+1
            if cur_freq.get(char, None)<k:
                max_len_str = max(max_len_str, self.find_longest_substr(string, t_s, i-1, t_freq, k))
                t_s = i+1
                t_freq.clear()
        if t_s==(e+1): return max_len_str
        if t_s==s: return e-s+1
        max_len_str = max(max_len_str, self.find_longest_substr(string, t_s, e, t_freq, k))
        return max_len_str
    
    def longestSubstring(self, s: str, k: int) -> int:
        s_len = len(s)
        freq = self.get_freq(s, 0, s_len-1)
        return self.find_longest_substr(s, 0, s_len-1, freq, k)