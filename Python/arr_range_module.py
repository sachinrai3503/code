# https://leetcode.com/problems/range-module
"""
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges 
 represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number
 in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any 
 numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right)
 is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 
Example 1:
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
 
Constraints:
1 <= left < right <= 109
At most 104 calls will be made to addRange, queryRange, and removeRange.
"""

from sys import maxsize
import bisect

class RangeModule:

    def __init__(self):
        self.ranges = []
    
    def _bound(self, left, right):
        range_len = len(self.ranges)
        i, j = 0, range_len-1
        for k in (100, 10, 1):
            while i+k-1<range_len and self.ranges[i+k-1][1]<left:
                i+=k
            while j-k+1>=0 and self.ranges[j-k+1][0]>right:
                j-=k
        return i,j

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bound(left, right)
        # print(f'ADD {i=} {j=} {left=} {right=}')
        if i<=j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]
        # print(f'{self.ranges=}')

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_left(self.ranges, (left, maxsize))
        # print(f'Q {i=} {left=} {right=}')
        if i>0:
            i-=1
        return bool(self.ranges) and left>=self.ranges[i][0] and right<=self.ranges[i][1]
        

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bound(left, right)
        # print(f'SUB {i=} {j=} {left=} {right=}')
        intervals = []
        if i<=j:
            if left>self.ranges[i][0]:
                intervals.append((self.ranges[i][0], left))
            if right<self.ranges[j][1]:
                intervals.append((right, self.ranges[j][1]))
        self.ranges[i:j+1] = intervals
        # print(f'{self.ranges=}')

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)