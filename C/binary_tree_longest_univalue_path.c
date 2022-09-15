// https://leetcode.com/problems/longest-univalue-path/
// https://www.geeksforgeeks.org/longest-path-values-binary-tree/
/*
Given the root of a binary tree, return the length of the longest path, where each node in
 the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
*/

#include <stdio.h>

//   Definition for a binary tree node.
  struct TreeNode {
      int val;
      struct TreeNode *left;
      struct TreeNode *right;
  };
 
typedef struct TreeNode tree_node;

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int get_longest_path(tree_node *root, int *max_len_path){
    if(root==NULL) return 0;
    int left_len = get_longest_path(root->left, max_len_path);
    int right_len = get_longest_path(root->right, max_len_path);
    if(root->left && root->right && root->val==root->left->val && root->val==root->right->val){
        *max_len_path = get_max(*max_len_path, 2 + left_len + right_len);
        return 1 + get_max(left_len, right_len);
    }else if(root->left && root->left->val==root->val){
        *max_len_path = get_max(*max_len_path, 1 + left_len);
        return 1+left_len;
    }else if(root->right && root->right->val==root->val){
        *max_len_path = get_max(*max_len_path, 1 + right_len);
        return 1+right_len;
    }else{
        return 0;
    }
}

int longestUnivaluePath(struct TreeNode* root){
    int max_len_path = 0;
    get_longest_path(root, &max_len_path);
    return max_len_path;
}