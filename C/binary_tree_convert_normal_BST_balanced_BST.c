// https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/?ref=rp
// https://leetcode.com/problems/balance-a-binary-search-tree/
/*
Given a BST (Binary Search Tree) that may be unbalanced, convert it into a 
balanced BST that has minimum possible height.

Examples :

Input:
       30
      /
     20
    /
   10
Output:
     20
   /   \
 10     30


Input:
         4
        /
       3
      /
     2
    /
   1
Output:
      3            3           2
    /  \         /  \        /  \
   1    4   OR  2    4  OR  1    3   OR ..
    \          /                   \
     2        1                     4 


NOTE - Using the tree balancing logic in bottom up fashion won't work for below
tree.
                          100
                        /     \
                      50       150
                    /   \      /  \
                   40   55   120   160
                 /       \
                30       60
               /          \
             20            65
            /               \
           10               70

    Here assume that 20,30,40,65,60,55 all have children till depth of 10.
    So, all the subtrees under 50 is balanced. Same for subtrees under 150. 
    But 100 is unbalanced and doing a right rotation on 100 won't balance it.
*/

#include <stdio.h>
//  Definition for a binary tree node.
 struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
 };
 
typedef struct TreeNode tree_node;

tree_node* make_tree_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->val = data;
        node->left = node->right = NULL;
    }
    return node;
}

tree_node* to_height_bal_BST(int *ip, int s, int e){
    if(s>e) return NULL;
    int mid = s + (e-s)/2;
    tree_node *root = make_tree_node(ip[mid]);
    root->left = to_height_bal_BST(ip,s,mid-1);
    root->right = to_height_bal_BST(ip,mid+1,e);
    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize){
    return to_height_bal_BST(nums, 0, numsSize-1);
}

void to_sorted_arr(tree_node *root, int *op, int *index){
    if(root){
        to_sorted_arr(root->left,op,index);
        op[(*index)++] = root->val;
        to_sorted_arr(root->right,op,index);
    }
}

struct TreeNode* balanceBST(struct TreeNode* root){
    int *op = (int*)calloc(10000,sizeof(int));
    int index = 0;
    to_sorted_arr(root, op, &index);
    return sortedArrayToBST(op,index);
}