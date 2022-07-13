# https://leetcode.com/problems/add-two-numbers/
"""
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit. 
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        prev = None
        a, b, carry = 0, 0, 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            t_sum = a + b + carry
            op = ListNode(t_sum%10)
            carry = t_sum//10
            if head is None:
                head = op
            else:
                prev.next = op
            prev = op
            l1 = None if l1==None else l1.next
            l2 = None if l2==None else l2.next
        if carry==1:
            prev.next = ListNode(1)
        return head