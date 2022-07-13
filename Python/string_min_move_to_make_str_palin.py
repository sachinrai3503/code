# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
"""
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:
Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.

Example 2:
Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 
Constraints:
1 <= s.length <= 2000
s consists only of lowercase English letters.
s can be converted to a palindrome using a finite number of moves.
"""

from collections import deque

class Solution:
    
    def is_palindrom(self, s, s_len):
        i, j = 0, s_len-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1
            j-=1
        return True
    
    # This times out
    def minMovesToMakePalindrome1(self, s: str) -> int:
        que = deque()
        visited = set()
        s_len = len(s)
        count = 0
        if self.is_palindrom(s, s_len): return 0
        que.append(s)
        visited.add(s)
        que.append(None)
        while que[0]!=None:
            # print(que, visited)
            while que[0]!=None:
                temp = que.popleft()
                for i in range(s_len-1):
                    t_s = temp[:i] + temp[i+1] + temp[i] + temp[i+2:]
                    if t_s not in visited:
                        if self.is_palindrom(t_s, s_len): return count+1
                        que.append(t_s)
                        visited.add(t_s)
            que.popleft()
            count+=1
            que.append(None)
        return -1
                    
    def minMovesToMakePalindrome2(self, s: str) -> int:
        count=0
        s_len = len(s)
        s_list = list(s)
        i, j = 0, s_len-1
        while i<j:
            p = j
            while s_list[i]!=s_list[p]:
                p-=1
            if p==i:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                count+=1
            else:
                while p<j:
                    s_list[p], s_list[p+1] = s_list[p+1], s_list[p]
                    p+=1
                    count+=1
                i+=1
                j-=1
        return count
    
    # Same logic as above but without swapping.
    def minMovesToMakePalindrome(self, s: str) -> int:
        count=0
        s_len = len(s)
        while s_len>2:
            hi = s.rfind(s[0])
            # print(s, s_len, hi)
            if hi==0: # means single occurance of this char
                lo = s.find(s[-1])
                count+=lo
                s = s[:lo] + s[lo+1:-1]
                s_len-=2
            else:
                count+=(s_len - hi - 1)
                s = s[1:hi] + s[hi+1:]
                s_len-=2
        return count