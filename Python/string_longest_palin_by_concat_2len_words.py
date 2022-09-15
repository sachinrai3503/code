# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words
"""
You are given an array of strings words. Each element of words consists of two lowercase
 English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating
 them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible 
 to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 
Constraints:
1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        max_len = 0
        freq_dict = dict()
        for word in words:
            count = freq_dict.get(word, 0)
            count+=1
            freq_dict[word] = count
        # print(freq_dict)
        included_odd_len = False
        for key in freq_dict:
            if freq_dict[key]==0: continue
            if key[0]!=key[1]: # word not palin
                rev_key = key[::-1]
                if rev_key not in freq_dict: continue
                max_len+=(min(freq_dict[key], freq_dict[rev_key])*4)
                freq_dict[key] = 0
                freq_dict[rev_key] = 0
            else:
                t_count = freq_dict[key]
                freq_dict[key] = 0
                if not t_count&1: # count is even
                    max_len+=(t_count*2)
                else:
                    if not included_odd_len:
                        included_odd_len = True
                        max_len+=(t_count*2)
                    else:
                        max_len+=((t_count-1)*2)
        return max_len