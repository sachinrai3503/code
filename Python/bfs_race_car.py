# https://leetcode.com/problems/race-car
"""
Your car starts at position 0 and speed +1 on an infinite number line. 
 Your car can go into negative positions. Your car drives automatically 
 according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
    position += speed
    speed *= 2
When you get an instruction 'R', your car does the following:
    If your speed is positive then speed = -1
    otherwise speed = 1
    Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3,
 and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of 
 instructions to get there.

Example 1:
Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:
Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

Constraints:
1 <= target <= 104
"""

from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        steps = 0
        que = deque()
        que.append((0,1))
        que.append(None)
        visited = set()
        visited.add((0,1))
        while que[0]!=None:
            while que[0]!=None:
                pos, speed = que.popleft()
                if pos==target: return steps
                A_info = (pos+speed, speed*2)
                R_info = (pos, -1 if speed>=0 else 1)
                if A_info not in visited:
                    que.append(A_info)
                    visited.add(A_info)
                if R_info not in visited:
                    que.append(R_info)
                    visited.add(R_info)
            que.popleft()
            # print(que)
            steps+=1
            que.append(None)
        return -1