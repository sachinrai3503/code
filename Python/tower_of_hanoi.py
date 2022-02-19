# https://www.lintcode.com/problem/169/
"""
Tower of Hanoi is a well-known problem.There are n plates of different sizes (radius 1-n)
 stacked on three pillars A, B and C.They are all stacked on A at first, your goal is
 moving all the plates from A to C in minimum legal steps.

The rules of moving are as follows:
You are allowed to move one plate once (from top of one pillar to top of another pillar)
Ensure that the smaller plates are on the top of the bigger one,and there is nothing under
 the biggest plate.


Example
Example 1:
Input:n = 2
Output: ["from A to B","from A to C","from B to C"]

Example 2:
Input:n = 3
Output:["from A to C","from A to B","from C to B","from A to C","from B to A","from B to C","from A to C"]
"""

class Solution:

    def move(self, n, fr, to, spare):
        if n==1:
            self.op.append("from " +fr + " to " + to)
        elif n>1:
            self.move(n-1, fr, spare, to)
            self.move(1,fr,to,spare)
            self.move(n-1,spare,to,fr)

    """
    @param n: the number of disks
    @return: the order of moves
    """
    def towerOfHanoi(self, n):
        self.op = list()
        self.move(n, 'A', 'C', 'B')
        return self.op
