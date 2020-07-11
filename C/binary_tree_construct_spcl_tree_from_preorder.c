// https://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
/*
Given an array ‘pre[]’ that represents Preorder traversal 
of a spacial binary tree where every node has either 0 or 2 children.

One more array ‘preLN[]’ is given which has only two possible
 values ‘L’ and ‘N’. The value ‘L’ in ‘preLN[]’ indicates that 
 the corresponding node in Binary Tree is a leaf node and value ‘N’
  indicates that the corresponding node is non-leaf node. 
  
Write a function to construct the tree from the given two arrays.

Example:

Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
Output: Root of following tree
          10
         /  \
        30   15
       /  \
      20   5
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

void print_int_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

void pre_order(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre_order(root->left);
        pre_order(root->right);
    }
}

tree_node* construct_tree(int pre[], char preLN[], int length, int *index){
    if(*index==length){
        return NULL;
    }
    tree_node *node = make_node(pre[(*index)++]);
    if(preLN[(*index)-1]=='L') return node;
    node->left = construct_tree(pre,preLN,length,index);
    node->right = construct_tree(pre,preLN,length,index);
    return node;
}

int main(){

    int pre[] = {1,2,3,4,5,6,3,4,5,7,8,6,5};
    char preLN[] = {'N','N','L','N','L','L','N','N','N','L','L','L','L'};
    int length = sizeof(pre)/sizeof(pre[0]);

    print_int_arr(pre,length);
    int index = 0;
    tree_node *root = construct_tree(pre,preLN,length,&index);
    pre_order(root);

    return 0;
}