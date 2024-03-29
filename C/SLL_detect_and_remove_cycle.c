// https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list
// https://leetcode.com/problems/linked-list-cycle
// https://leetcode.com/problems/linked-list-cycle-ii
/*
Given the head of a linked list, return the node where the cycle begins. If there is 
 no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached
 again by continuously following the next pointer. Internally, pos is used to denote the
 index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there
 is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:
 The number of the nodes in the list is in the range [0, 104].
 -105 <= Node.val <= 105
 pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
*/

#include <stdio.h>
#include <malloc.h>
 
// Definition for singly-linked list.
  struct ListNode {
      int val;
      struct ListNode *next;
  };
 

typedef struct ListNode list_node;

list_node* get_cycle_node(list_node *head){
    if(!head) return NULL;
    list_node *fast = head;
    list_node *slow = head;
    do{
        fast = fast->next;
        if(fast && fast->next) fast = fast-> next;
        else return NULL;
        slow = slow->next;
    }while(slow!=fast);
    return slow;
}

struct ListNode *detectCycle(struct ListNode *head) {
    list_node *cycle_node = get_cycle_node(head);
    if(!cycle_node) return NULL;
    list_node *t_head = head;
    while(t_head!=cycle_node){
        t_head = t_head->next;
        cycle_node = cycle_node->next;
    }
    return t_head;
}