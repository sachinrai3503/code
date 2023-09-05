// https://leetcode.com/problems/remove-nodes-from-linked-list
/**
You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the 
 right side of it.

Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.

Constraints:
The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105 
*/

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode list_node;

list_node* reverse(list_node *head){
    list_node *p = head;
    list_node *q = NULL, *r = NULL;
    while(p){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
    }
    return q;
}

struct ListNode* removeNodes(struct ListNode* head){
    list_node *p = head;
    list_node *q = NULL, *r = NULL;
    while(p){
        q = p;
        p = p->next;
        while(r && r->val<q->val){
            r=r->next;
        }
        q->next = r;
        r = q;
    }
    return reverse(q);
}