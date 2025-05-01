# https://leetcode.com/problems/linked-list-random-node
"""
Given a singly linked list, return a random node's value from the linked list. 
 Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. 
All the nodes of the list should be equally likely to be chosen.
 
Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

Constraints:
The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""

import random
from random import randint
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution1:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = None

    def getRandom(self) -> int:
        if self.length:
            index = randint(0, self.length)
        else:
            index = int(random.random() * (10**randint(1,16)))
        return self.find_element_at(index)
    
    def find_element_at(self, index):
        i = 0
        t_head = self.head
        while i<index and t_head:
            i+=1
            t_head = t_head.next
        if t_head:
            return t_head.val
        else:
            self.length = i
            return self.getRandom()

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    # https://leetcode.ca/2016-12-16-382-Linked-List-Random-Node
    # This is slow
    def getRandom(self) -> int:
        n = ans = 0
        t_head = self.head
        while t_head:
            n+=1
            x = randint(1, n)
            if n==x:
                ans = t_head.val
            t_head = t_head.next
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()