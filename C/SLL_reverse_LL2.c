// https://leetcode.com/problems/reverse-linked-list-ii
/**
Given the head of a singly linked list and two integers left and right where 
 left <= right, reverse the nodes of the list from position left to position 
 right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n 
Follow up: Could you do it in one pass?
*/

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode list_node;

list_node* reverse_count_nodes(list_node *head, int count){
    if(!head) return NULL;
    list_node *p = head;
    list_node *q = NULL, *r = NULL;
    int i = 0;
    while(p && i<count){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
        i++;
    }
    if(count>0){
        head->next = p;
    }
    return q;
}

struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    list_node *prev = NULL;
    int i = 0;
    list_node *p = head;
    while(p){
        i++;
        if(i==left){
            list_node *next = reverse_count_nodes(p, right-left+1);
            if(prev) prev->next = next;
            else head = next;
            break;
        }
        prev = p;
        p = p->next;
    }
    return head;
}