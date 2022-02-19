# https://www.geeksforgeeks.org/the-celebrity-problem/
# https://www.lintcode.com/problem/645/
"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,
 there may exist one celebrity. The definition of a celebrity is that all the other
 n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
 The only thing you are allowed to do is to ask questions like:
 "Hi, A. Do you know B?" to get information of whether A knows B.
  You need to find out the celebrity (or verify there is not one) by asking as
  few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B.
 Implement a function int findCelebrity(n), your function should minimize the number
 of calls to knows.

There will be exactly one celebrity if he/she is in the party. 
 Return the celebrity's label if there is a celebrity in the party.
 If there is no celebrity, return -1.

Example1
Input:
2 // next n * (n - 1) lines 
0 knows 1
1 does not know 0
Output: 1
Explanation:
Everyone knows 1,and 1 knows no one.

Example2
Input:
3 // next n * (n - 1) lines 
0 does not know 1
0 does not know 2
1 knows 0
1 does not know 2
2 knows 0
2 knows 1
Output: 0
Explanation:
Everyone knows 0,and 0 knows no one.
0 does not know 1,and 1 knows 0.
2 knows everyone,but 1 does not know 2.
"""

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Celebrity:
    def knows(self, a, b):
        pass

class Solution:

    def __init__(self):
        self.celebrity = Celebrity()

    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        cel = 0
        i = 1
        while i<n:
            if not self.celebrity.knows(i, cel):
                cel = i
                i+=1
            elif self.celebrity.knows(cel, i):
                cel = i+1
                i+=2
            else: i+=1
        # print(cel)
        if cel>=n: return -1
        i = 0
        while i<cel:
            if not self.celebrity.knows(i, cel):
                # print(i, cel)
                return -1
            if self.celebrity.knows(cel, i): 
                # print('dfd', i, cel)
                return -1
            i+=1
        return cel