// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
// https://www.geeksforgeeks.org/maximum-difference-between-node-and-its-ancestor-in-binary-tree/
/*
Given the root of a binary tree, find the maximum value V for which there exist
 different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any
 child of A is an ancestor of B.

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are  :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3
 
Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
*/

//  Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
 
#include <limits.h>
#include <stdio.h>

typedef struct TreeNode tree_node;

int get_abs_diff(int a, int b){
    if(a>b) return a-b;
    return b-a;
}

void get_max_diff(tree_node *root, int max, int min, int *max_diff){
    if(root==NULL) return;
    if(root->val>max) max = root->val;
    if(root->val<min) min = root->val;
    int cur_diff = get_abs_diff(max, min);
    if(cur_diff>*max_diff){
        *max_diff = cur_diff;
    }
    get_max_diff(root->left, max, min, max_diff);
    get_max_diff(root->right, max, min, max_diff);
}

int maxAncestorDiff(struct TreeNode* root){
    int max_diff = 0;
    get_max_diff(root, INT_MIN, INT_MAX, &max_diff);
    return max_diff;
}