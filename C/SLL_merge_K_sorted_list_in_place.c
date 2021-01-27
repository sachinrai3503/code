// https://leetcode.com/problems/merge-k-sorted-lists/
// https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/
// https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
/*
You are given an array of k linked-lists lists, each linked-list is sorted in
 ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
*/

// NOTE - Below logic is O(nkLog(k)) and is better than the min_heap based sol.
// because that uses O(k) extra space with same time complexity.

#include <stdio.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
 };

typedef struct ListNode list_node;

list_node* get_last_smaller_greater_node(list_node *head, int data){
    list_node *prev = NULL;
    for(;head && head->val<=data;head=head->next) prev = head;
    return prev;
}

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    if(!l1) return l2;
    if(!l2) return l1;
    list_node *new_head = NULL;
    list_node *prev = NULL;
    while(l1 && l2){
        list_node *last_small_eq_node = get_last_smaller_greater_node(l2, l1->val);
        if(new_head==NULL){
            if(last_small_eq_node) new_head = l2;
            else new_head = l1;
        }else{
            if(last_small_eq_node) prev->next = l2;
            else prev->next = l1;
        }
        if(last_small_eq_node){
            l2 = last_small_eq_node->next;
            last_small_eq_node->next = l1;
        }
        prev = l1;
        l1 = l1->next;
    }
    if(!l1) prev->next = l2;
    return new_head;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    if(listsSize==0) return NULL;
    int count = listsSize;
    while(count>1){
        int k = 0;
        int i = 0;
        for(;i<count;i+=2){
            list_node *l1 = lists[i];
            list_node *l2 = NULL;
            if(i+1<count) l2 = lists[i+1];
            lists[k++] = mergeTwoLists(l1, l2);
        }
        count = k;
    }
    return lists[0];
}