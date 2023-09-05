// https://leetcode.com/problems/remove-linked-list-elements
/**
Given the head of a linked list and an integer val, remove all the nodes of the 
 linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
 
Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
*/

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
     int val;
     struct ListNode *next;
 };

typedef struct ListNode list_node;

struct ListNode* removeElements(struct ListNode* head, int val){
    if(head==NULL) return NULL;
    list_node *new_head = NULL;
    list_node *prev = NULL, *cur = head, *next = cur->next;
    while(cur){
        if(cur->val!=val){
            if(!new_head) new_head = cur;
            prev = cur;
        }else{
            if(prev) prev->next = next;
        }
        cur = next;
        if(cur) next = cur->next;
    }
    return new_head;
}