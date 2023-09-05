// https://leetcode.com/problems/leaf-similar-trees
/*
Consider all the leaves of a binary tree, from left to right order, the values of
 those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], 
       root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
*/

#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


typedef struct TreeNode tree_node;

typedef struct ListNode1{
    int val;
    struct ListNode1 *next;
}list_node;

list_node* init_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->val = data;
        node->next = NULL;
    }
    return node;
}

void print_list(list_node *head){
    for(;head;head=head->next){
        printf("%d ",head->val);
    }
    printf("\n");
}

list_node* add_to_list(list_node *head, int data){
    list_node *temp = init_list_node(data);
    temp->next = head;
    return temp;
}

bool compare_list(list_node *l1, list_node *l2){
    while(l1 && l2){
        if(l1->val!=l2->val) return false;
        l1=l1->next;
        l2=l2->next;
    }
    if(!l1 && !l2) return true;
    return false;
}

bool is_leaf(tree_node *node){
    if(!node) return false;
    if(!node->left && !node->right) return true;
    return false;
}

void add_leafs_to_list(tree_node *root, list_node **head){
    if(!root) return NULL;
    if(is_leaf(root)){
        *head = add_to_list(*head, root->val);
    }else{
        add_leafs_to_list(root->left, head);
        add_leafs_to_list(root->right, head);
    }
}

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    list_node *t1_leafs = NULL, *t2_leafs = NULL;
    add_leafs_to_list(root1, &t1_leafs);
    add_leafs_to_list(root2, &t2_leafs);
    // print_list(t1_leafs);
    // print_list(t2_leafs);
    return compare_list(t1_leafs, t2_leafs);
}