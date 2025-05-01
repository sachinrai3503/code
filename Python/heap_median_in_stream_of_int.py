# https://leetcode.com/problems/find-median-from-data-stream
# https://github.com/RodneyShag/LeetCode_solutions/blob/master/Solutions/Find%20Median%20from%20Data%20Stream.md
"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
 and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.count_left = 0
        self.count_right = 0
        self.median = 0

    def addNum(self, num: int) -> None:
        if num<=self.median:
            if self.count_left>self.count_right:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                self.count_right+=1
                self.count_left-=1
            heapq.heappush(self.max_heap, -num)
            self.count_left+=1
        else:
            if self.count_left<self.count_right:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                self.count_left+=1
                self.count_right-=1
            heapq.heappush(self.min_heap, num)
            self.count_right+=1
        self.median = self._get_median()

    def _get_median(self):
        if self.count_left==self.count_right:
            self.median = (-self.max_heap[0] + self.min_heap[0])/2
        elif self.count_left<self.count_right:
            self.median = self.min_heap[0]
        else:
            self.median = -self.max_heap[0]
        return self.median

    def findMedian(self) -> float:
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()