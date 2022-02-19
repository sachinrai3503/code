// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
// https://www.geeksforgeeks.org/flatten-a-multi-level-linked-list-set-2-depth-wise
/*
You are given a doubly linked list which in addition to the next and previous
 pointers, it could have a child pointer, which may or may not point to a 
 separate doubly linked list. These child lists may have one or more children 
 of their own, and so on, to produce a multilevel data structure, as shown in 
 the example below.

Flatten the list so that all the nodes appear in a single-level, DLL. 
You are given the head of the first level of the list.

NOTE - 
How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:
    [1,2,3,4,5,6,null]
    [7,8,9,10,null]
    [11,12,null]

To serialize all levels together we will add nulls in each level to signify no 
node connects to the upper node of the previous level.

The serialization becomes:

    [1,2,3,4,5,6,null]
    [null,null,7,8,9,10,null]
    [null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:
    [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:
Input: head = []
Output: []

Constraints:
 - Number of Nodes will not exceed 1000.
 - 1 <= Node.val <= 10^5
*/
#include <stdio.h>

// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
    
public:
    Node* flatten_node(Node* head) {
        if(head==NULL) return NULL;
        Node *next = flatten_node(head->next);
        Node *child = flatten_node(head->child);
        Node *last = NULL;
        if(next){
            last = next->prev;
            next->prev->next = head;
            if(child) next->prev = child->prev;
            else next->prev = head;
        }
        if(child){
            if(!last) last = child->prev;
            if(next) child->prev->next = next;
            else child->prev->next = head;
            child->prev = head;
        }
        if(child){
            head->next = child;
        }else if(next){
            head->next = next;
        }else{
            head->next = head;
        }
        if(last) head->prev = last;
        else head->prev = head;
        head->child = NULL;
        return head;
    }

    public:
    Node* flatten(Node* head) {
        if(head==NULL) return NULL;
        head = flatten_node(head);
        head->prev->next = NULL;
        head->prev = NULL;
        return head;
    }
};