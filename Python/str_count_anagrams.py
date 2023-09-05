# https://leetcode.com/problems/count-anagrams
"""
You are given a string s containing one or more words. Every consecutive pair
 of words is separated by a single space ' '.

A string t is an anagram of string s if the ith word of t is a permutation of 
 the ith word of s.

For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
Return the number of distinct anagrams of s. Since the answer may be very large,
 return it modulo 109 + 7.

Example 1:
Input: s = "too hot"
Output: 18
Explanation: Some of the anagrams of the given string are "too hot", 
 "oot hot", "oto toh", "too toh", and "too oht".

Example 2:
Input: s = "aa"
Output: 1
Explanation: There is only one anagram possible for the given string.
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters and spaces ' '.
There is single space between consecutive words.
"""

from math import factorial

class Solution:

    def __init__(self):
        self.q = 1000000007
        self.factorial_map = dict()

    def get_factorial(self, n:int) -> int:
        fact = self.factorial_map.get(n, None)
        if fact is not None: return fact
        fact = factorial(n)
        self.factorial_map[n] = fact
        return fact

    def get_unique_anagram_count(self, word_len, char_count_map):
        numerator = self.get_factorial(word_len)
        denominator = 1
        for _, count in char_count_map.items():
            if count>1:
                denominator = denominator*self.get_factorial(count)
        return (numerator//denominator)%self.q

    def process_word(self, word_len, char_list, char_count, word_anagram_count_map):
        word = ''.join(char_list)
        anagram_count = word_anagram_count_map.get(word, None)
        if anagram_count is None:
            anagram_count = self.get_unique_anagram_count(word_len, char_count)
            word_anagram_count_map[word] = anagram_count
        return anagram_count

    def countAnagrams(self, s: str) -> int:
        op = 1
        s_len = len(s)
        word_anagram_count_map = dict()
        char_count = dict()
        word_len = 0
        char_list = list()
        for char in s:
            if char is ' ':
                anagram_count = self.process_word(word_len, char_list, char_count, word_anagram_count_map)
                op = (op*anagram_count)%self.q
                word_len = 0
                char_list.clear()
                char_count.clear()
            else:
                word_len+=1
                char_list.append(char)
                count = char_count.get(char, 0)
                char_count[char] = count+1
        anagram_count = self.process_word(word_len, char_list, char_count, word_anagram_count_map)
        op = (op*anagram_count)%self.q
        return op