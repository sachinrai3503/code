# https://leetcode.com/problems/minimum-interval-to-include-each-query
"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting
 at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains,
 or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such
 that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Example 2:
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:
1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""

from typing import List
import heapq

class Solution:

    def floor(self, queries, queries_index, queries_len, k):
        _floor = -1
        s, e = 0, queries_len-1
        while s<=e:
            mid = s + (e-s)//2
            if queries[queries_index[mid]]<=k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor
    
    def ceil(self, queries, queries_index, queries_len, k):
        _ceil = queries_len
        s, e = 0, queries_len-1
        while s<=e:
            mid = s + (e-s)//2
            if queries[queries_index[mid]]<k:
                s = mid+1
            else:
                _ceil = mid
                e = mid-1
        return _ceil

    # This will timeout
    def minInterval1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals_len = len(intervals)
        queries_len = len(queries)
        op = [-1 for i in range(queries_len)]
        intervals.sort(key = lambda interval: interval[1]-interval[0]+1)
        queries_index = [i for i in range(queries_len)]
        queries_index.sort(key = lambda i: queries[i])
        # print(f'{intervals=}')
        # print(f'{queries=}')
        # print(f'{queries_index=}')
        for i in range(intervals_len):
            s, e = intervals[i]
            interval_len = e-s+1
            # queries[p:q] = queries impacted by this interval 
            p = self.ceil(queries, queries_index, queries_len, s)
            q = self.floor(queries, queries_index, queries_len, e)
            # print(f'{p=} {q=}')
            while p<=q:
                if op[queries_index[p]]==-1:
                    op[queries_index[p]] = interval_len
                p+=1
        return op

    # This too will timeout
    def minInterval2(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals_len = len(intervals)
        queries_len = len(queries)
        op = [-1 for i in range(queries_len)]
        queries_index = [i for i in range(queries_len)]
        queries_index.sort(key = lambda i: queries[i])
        intervals_heap = [[interval[0], interval[1], interval[1]-interval[0]+1] for interval in intervals]
        heapq.heapify(intervals_heap)
        print(f'{intervals=}')
        print(f'{intervals_heap=}')
        print(f'{queries=}')
        print(f'{queries_index=}')
        i = 0
        while i<queries_len and intervals_heap:
            top = intervals_heap[0]
            query = queries[queries_index[i]]
            if query<top[0]:
                op[queries_index[i]] = -1
                i+=1
            elif query==top[0]:
                interval = heapq.heappop(intervals_heap)
                op[queries_index[i]] = interval[2]
                interval[0] = query
                if interval[0]<=interval[1]:
                    heapq.heappush(intervals_heap, interval)
                i+=1
            else:
                interval = heapq.heappop(intervals_heap)
                interval[0] = query
                if interval[0]<=interval[1]:
                    heapq.heappush(intervals_heap, interval)
        return op
    
    def minInterval_old(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_len = len(queries)
        intervals_len = len(intervals)
        op = [-1 for i in range(queries_len)]
        queries_index = [i for i in range(queries_len)]
        intervals.sort()
        queries_index.sort(key = lambda i : queries[i])
        min_heap = list()
        i, j = 0, 0
        while i<queries_len:
            query = queries[queries_index[i]]
            while j<intervals_len and query>=intervals[j][0]:
                s, e = intervals[j]
                heapq.heappush(min_heap, (e-s+1, e))
                j+=1
            while min_heap and min_heap[0][1]<query:
                heapq.heappop(min_heap)
            op[queries_index[i]] = min_heap[0][0] if min_heap else -1
            i+=1
        return op

    # Same as above. Just 1 minor enhancement
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_len = len(queries)
        intervals_len = len(intervals)
        intervals.sort(key = lambda x: x[0])
        queries_index = [i for i in range(queries_len)]
        op = [-1 for _ in range(queries_len)]
        queries_index.sort(key = lambda x : queries[x])
        # print(f'{queries_index=}')
        interval_heap = [] # [(size, e), (...), ...]
        i = 0
        for query_index in queries_index:
            query = queries[query_index]
            while i<intervals_len: # add new relevant intervals to the heap
                s, e = intervals[i]
                if query>e: # past interval
                    i+=1
                elif query<s: # future interval
                    break
                else:
                    heapq.heappush(interval_heap, (e-s+1, e))
                    i+=1
            while interval_heap and interval_heap[0][1]<query: # pop past intervals in the heap
                heapq.heappop(interval_heap)
            if interval_heap:
                op[query_index] = interval_heap[0][0]
        return op