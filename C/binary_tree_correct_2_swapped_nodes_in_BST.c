// https://leetcode.com/problems/recover-binary-search-tree/
// https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/
/*
You are given the root of a binary search tree (BST), where exactly two nodes
 of the tree were swapped by mistake. 
 
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

Example 1:

        1             3
      3        ==>  1
        2             2

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. 
Swapping 1 and 3 makes the BST valid.
*/

#include <stdio.h>

// Definition for a binary tree node.
typedef struct node {
    int val;
    struct node *left;
    struct node *right;
}treeNode;

void recoverBST(treeNode *root, treeNode **a, treeNode **b, treeNode **prev){
    if(root==NULL) return;
    recoverBST(root->left,a,b,prev);
    if(*prev && root->val<(*prev)->val){
        if(*a==NULL) *a = *prev;
        *b = root;
    }
    *prev = root;
    recoverBST(root->right,a,b,prev);
}

void recoverTree(treeNode* root){
    treeNode *a = NULL;
    treeNode *b = NULL;
    treeNode *prev = NULL;
    recoverBST(root,&a,&b,&prev);
    int temp = a->val;
    a->val = b->val;
    b->val = temp;
}