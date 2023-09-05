// https://leetcode.com/problems/reverse-nodes-in-k-group
/**
Given the head of a linked list, reverse the nodes of the list k at a time, and 
 return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes, in the end, should
 remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
*/

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode list_node;

int count_nodes(list_node *head){
    int i = 0;
    for(;head;head=head->next){
        i+=1;
    }
    return i;
}

list_node* reverse_k_nodes(list_node *head, int k){
    list_node *p = head;
    list_node *q = NULL, *r = NULL;
    int i = 0;
    while(p && i<k){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
        i++;
    }
    if(k!=0)
        head->next=p;
    return q;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k){
    list_node *new_head = NULL;
    list_node *prev = NULL;
    int list_len = count_nodes(head);
    int reverse_count = list_len/k;
    while(head && reverse_count>0){
        list_node *reversed_node = reverse_k_nodes(head, k);
        if(prev) prev->next = reversed_node;
        else new_head = reversed_node;
        prev = head;
        head = head->next;
        reverse_count--;
    }
    return new_head;
}