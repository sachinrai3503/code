# https://leetcode.com/problems/implement-queue-using-stacks
# https://www.geeksforgeeks.org/queue-using-stacks
"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue
 (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top,
 peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may
 simulate a stack using a list or deque (double-ended queue) as long as you use
 only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 
Follow-up: Can you implement the queue such that each operation is amortized
 O(1) time complexity? In other words, performing n operations will take overall
 O(n) time even if one of those operations may take longer.
"""

from sys import maxsize

class MyQueue:

    def __init__(self):
        self.stck1 = list()
        self.stck2 = list()

    def push(self, x: int) -> None:
        self.stck1.append(x)

    def pop(self) -> int:
        if self.empty(): return maxsize
        if len(self.stck2)==0:
            while len(self.stck1)>0:
                self.stck2.append(self.stck1.pop())
        temp = self.stck2.pop()
        return temp

    def peek(self) -> int:
        if self.empty(): return maxsize
        if len(self.stck2)==0:
            while len(self.stck1)>0:
                self.stck2.append(self.stck1.pop())
        return self.stck2[-1]

    def empty(self) -> bool:
        if len(self.stck1)==0 and len(self.stck2)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()