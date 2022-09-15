// https://leetcode.com/problems/palindrome-linked-list/
/*
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
*/

#include <stdio.h>
#include <malloc.h>
#define true 1
#define false 1

typedef int bool;

//  Definition for singly-linked list.
struct ListNode {
      int val;
      struct ListNode *next;
  };

typedef struct ListNode list_node;

list_node* get_middle(list_node *head){
    list_node *p = head;
    list_node *q = head;
    while(p && p->next){
        p = p->next;
        if(p->next){
            q = q->next;
            p = p->next;
        }
    }
    return q;
}

list_node* reverse(list_node *head){
    list_node *p = head;
    list_node *q = NULL;
    list_node *r = NULL;
    while(p){
        q = p;
        p = p->next;
        q->next = r;
        r = q;
    }
    return q;
}

bool isPalindrome(struct ListNode* head){
    list_node *middle_node = get_middle(head);
    list_node *h2 = NULL;
    if(middle_node){
        h2 = middle_node->next;
        middle_node->next = NULL;
    }
    h2 = reverse(h2);
    while(h2){
        if(head->val!=h2->val) return false;
        head = head->next;
        h2 = h2->next;
    }
    return true;
}