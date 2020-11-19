# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# https://www.geeksforgeeks.org/reduce-the-string-by-removing-k-consecutive-identical-characters/
"""
Given a string s, a k duplicate removal consists of choosing k adjacent and
 equal letters from s and removing them causing the left and the right side 
 of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck = list()
        for char in s:
            if len(stck)==0 or stck[-1][0]!=char:
                stck.append((char, 1))
            elif stck[-1][0]==char:
                stck.append((char, stck[-1][1]+1))
            if stck[-1][1]==k:
                j = 0
                while j<k:
                    stck.pop()
                    j+=1
        return ''.join(item[0] for item in stck)