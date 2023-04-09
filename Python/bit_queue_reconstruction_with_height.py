# https://leetcode.com/problems/queue-reconstruction-by-height/description/
"""
You are given an array of people, people, which are the attributes of some people
 in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the
 ith person of height hi with exactly ki other people in front who have a height
 greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people.
 The returned queue should be formatted as an array queue, where queue[j] = [hj, kj]
 is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:
1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
"""
from typing import List

class BIT:
    def __init__(self, size):
        self.data = [0 for i in range(size+1)]
        self.size = size+1

    def update(self, index, value=1):
        index+=1
        while index<self.size:
            self.data[index]+=value
            index+=(index&-index)

    def query(self, index):
        _sum = 0
        index+=1
        while index>0:
            _sum+=self.data[index]
            index-=(index&-index)
        return _sum

class Solution:

    def find_next_cell(self, bit:BIT, op, n, s, k):
        while s<n:
            if op[s] is not None: # already occupied
                s+=1
                continue
            empty_cell_count = s - bit.query(s-1) # total_cells - occupied ones
            if empty_cell_count==k: return s
            s+=1
        return -1

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_length = len(people)
        op = [None for i in range(people_length)]
        bit = BIT(people_length)
        people.sort(key = lambda x : (x[0], -x[1]))
        # print(people)
        for i in range(people_length):
            taller_req = people[i][1]
            index = self.find_next_cell(bit, op, people_length, taller_req, taller_req)
            bit.update(index)
            op[index] = people[i]
        return op