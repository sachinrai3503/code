# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal
# https://www.geeksforgeeks.org/check-if-two-strings-can-be-made-equal-by-swapping-one-character-among-each-other
"""
You are given two strings s1 and s2 of equal length. A string swap is an operation
 where you choose two indices in a string (not necessarily different) and swap the
 characters at these indices.

Return true if it is possible to make both strings equal by performing at most one
 string swap on exactly one of the strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 
Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s_len = len(s1)
        indexs = list()
        for i in range(s_len):
            if s1[i]!=s2[i]:
                indexs.append(i)
        indexs_len = len(indexs)
        if indexs_len==0: return True
        if indexs_len!=2: return False
        return (s1[indexs[0]]==s2[indexs[1]] and s1[indexs[1]]==s2[indexs[0]])

# https://leetcode.com/problems/buddy-strings
"""
Given two strings s and goal, return true if you can swap two letters in s so the
 result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j
 and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
"""

class Solution2:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_len = len(s)
        g_len = len(goal)
        if s_len!=g_len: return False
        index = list()
        freq = [0 for i in range(26)]
        has_dup_char = False
        for i in range(s_len):
            freq[ord(s[i])-97]+=1
            if freq[ord(s[i])-97]==2: has_dup_char = True
            if s[i]!=goal[i]:
                index.append(i)
        index_len = len(index)
        if index_len==0:
            return has_dup_char
        if index_len!=2: return False
        return (s[index[0]]==goal[index[1]] and s[index[1]]==goal[index[0]])