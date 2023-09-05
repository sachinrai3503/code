// https://leetcode.com/problems/odd-even-linked-list
/**
Given the head of a singly linked list, group all the nodes with odd indices
 together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain 
 as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
*/

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};


typedef struct ListNode list_node;

struct ListNode* oddEvenList(struct ListNode* head){
    if(!head) return NULL;
    list_node *odd_head = NULL, *odd_last = NULL;
    list_node *even_head = NULL, *even_last = NULL;
    int i = 1;
    while(head){
        list_node *next = head->next;
        if(i%2==1){
            if(odd_head==NULL) odd_head = head;
            else odd_last->next = head;
            odd_last = head;
        }else{
            if(even_head==NULL) even_head = head;
            else even_last->next = head;
            even_last = head;
        }
        i++;
        head = next;
    }
    odd_last->next=even_head;
    if(even_last) even_last->next = NULL;
    return odd_head;
}