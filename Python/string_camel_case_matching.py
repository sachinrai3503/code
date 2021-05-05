# https://leetcode.com/problems/camelcase-matching/
"""
A query word matches a given pattern if we can insert lowercase letters to the
 pattern word so that it equals the query. (We may insert each character at any
 position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans,
 where answer[i] is true if and only if queries[i] matches the pattern.

Example 1:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:
1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
"""

class Solution:
    
    def check_query(self, query, pattern):
        i, j = 0, 0
        l1, l2 = len(query), len(pattern)
        while i<l1 and j<l2:
            if pattern[j]==query[i]:
                j+=1
            elif 'A'<=query[i]<='Z':
                return False
            i+=1
        while i<l1:
            if 'A'<=query[i]<='Z': return False
            i+=1
        if j<l2: return False
        return True
    
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        op_list = list()
        for query in queries:
            op_list.append(self.check_query(query, pattern))
        return op_list