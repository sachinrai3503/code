// https://leetcode.com/problems/binary-tree-maximum-path-sum/
// https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
/*
A path in a binary tree is a sequence of nodes where each pair of adjacent
 nodes in the sequence has an edge connecting them. A node can only appear
 in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode treeNode;

int getMax(int a, int b){
    if(a>b) return a;
    return b;
}

int getMaxPathSum(treeNode *root, int *max){
    if(root==NULL) return 0;
    int left = getMaxPathSum(root->left, max);
    int right = getMaxPathSum(root->right, max);

    int left_sub_tree = left + root->val;
    int right_sub_tree = right + root->val;
    int via_root = left + right + root->val;

    *max = getMax(*max, getMax(getMax(left_sub_tree, right_sub_tree), getMax(root->val, via_root)));
    return getMax(root->val, getMax(left_sub_tree,right_sub_tree));   
}

int maxPathSum(struct TreeNode* root){
    int max = INT_MIN;
    getMaxPathSum(root, &max);
    return max;
}