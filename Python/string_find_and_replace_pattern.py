# https://leetcode.com/problems/find-and-replace-pattern/
"""
Given a list of strings words and a string pattern, return a list of words[i]
 that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that
 after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters:
 every letter maps to another letter, and no two letters map to the same letter.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 
Constraints:
1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""

class Solution:
        
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        op = list()
        pat_len = len(pattern)
        for word in words:
            pat_link = [None for i in range(26)]
            word_link = [None for i in range(26)]
            result = True
            # print(word, pattern)
            for i in range(pat_len):
                p_index = ord(pattern[i])-97
                w_index = ord(word[i])-97
                p_link = pat_link[p_index]
                w_link = word_link[w_index]
                if p_link is None and w_link is None:
                    pat_link[p_index] = word[i]
                    word_link[w_index] = pattern[i]
                elif p_link is not None and w_link is not None:
                    if p_link==word[i] and w_link==pattern[i]: continue
                    else:
                        result = False
                        break
                else:
                    result = False
                    break
            # print(i, pat_link, word_link)
            if result:
                op.append(word)
        return op