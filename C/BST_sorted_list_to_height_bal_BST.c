// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
/*
Given the head of a singly linked list where elements are sorted in ascending order, convert 
 it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
 of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown 
 height balanced BST.

Example 2:
Input: head = []
Output: []

Constraints:
The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
*/

#include <stdio.h>
#include <malloc.h>

//  Definition for singly-linked list.
 struct ListNode {
     int val;
     struct ListNode *next;
 };

//  Definition for a binary tree node.
 struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
 };

typedef struct ListNode list_node;
typedef struct TreeNode tree_node;

tree_node* init_tree_node(int val){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->val = val;
        node->left = node->right = NULL;
    }
    return node;
}

int get_len(list_node *head){
    int len = 0;
    while(head){
        len++;
        head = head->next;
    }
    return len;
}

tree_node* get_BST(list_node **head, int s, int e){
    if(s>e) return NULL;
    int mid = s + (e-s)/2;
    tree_node *left = get_BST(head, s, mid-1);
    tree_node *node = init_tree_node((*head)->val);
    *head = (*head)->next;
    tree_node *right = get_BST(head, mid+1, e);
    node->left = left;
    node->right = right;
    return node;
}

struct TreeNode* sortedListToBST(struct ListNode* head){
    int list_len = get_len(head);
    tree_node *root = get_BST(&head, 0, list_len-1);
    return root;
}