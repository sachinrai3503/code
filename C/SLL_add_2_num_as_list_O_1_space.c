// https://leetcode.com/problems/add-two-numbers-ii/
// https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists-set-3/

/*
You are given two non-empty linked lists representing two non-negative integers.
 The most significant digit comes first and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 
Follow up: Could you solve it without reversing the input lists?
*/

// Below sol. is without reversing the list and iterative.

#include <stdio.h>
#include <malloc.h>

// Definition for singly-linked list.
 struct ListNode {
     int val;
     struct ListNode *next;
 };


typedef struct ListNode list_node;

list_node* make_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->val = data;
        node->next = NULL;
    }
    return node;
}

int get_len(list_node *l1){
    int len = 0;
    for(;l1;l1=l1->next) len++;
    return len;
}

int get_next_sum(list_node *l1, int len1, list_node *l2, int len2){
    int a = 0, b = 0;
    if(len1==len2){
        a = (l1->next)?l1->next->val:0;
        b = (l2->next)?l2->next->val:0;
    }else if(len1>len2){
        a = (l1->next)?l1->next->val:0;
        if(len1-len2==1) b = (l2)?l2->val:0;
    }else{
        b = (l2->next)?l2->next->val:0;
        if(len2-len1==1) a = (l1)?l1->val:0;
    }
    return a+b;
}

list_node* add_carry(list_node *head, list_node *from, list_node *to, int carry){
    while(1){
        if(from->val<9) from->val++;
        else{
            from->val = 0;
            if(from==head){
                list_node *temp = make_list_node(1);
                temp->next = head;
                head = temp;
            }
        }
        if(from==to) break;
        else from = from->next;
    }
    return head;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int len1 = get_len(l1);
    int len2 = get_len(l2);
    int a = 0, b = 0;
    list_node *head = NULL;
    list_node *prev = NULL;
    list_node *carry_from = NULL;
    while(len1 || len2){
        int next_sum = 0;
        int carry = 0;
        if(len1==len2){
            a = l1->val;
            b = l2->val;
            next_sum = get_next_sum(l1, len1, l2, len2);
            l1 = l1->next;
            l2 = l2->next;
            len1--;
            len2--;
        }else if(len1>len2){
            a = l1->val;
            next_sum = get_next_sum(l1, len1, l2, len2);
            l1 = l1->next;
            len1--;
        }else{
            b = l2->val;
            next_sum = get_next_sum(l1, len1, l2, len2);
            l2 = l2->next;
            len2--;
        }
        int sum = a+b;
        list_node *temp = make_list_node(sum%10);
        carry = sum/10;
        if(head==NULL){
            if(carry==1){
                list_node *carry_node = make_list_node(1);
                carry_node->next = temp;
                head = carry_node;
            }
            else head = temp;
        }else prev->next = temp;
        if(next_sum<9){
            carry_from = NULL;
        }else if(next_sum>9){
            if(!carry_from) carry_from = temp;
            head = add_carry(head, carry_from, temp, 1);
            carry_from = NULL;
        }else if(!carry_from){
            carry_from = temp;
        }
        prev = temp;
    }
    return head;
}