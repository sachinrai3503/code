// https://www.geeksforgeeks.org/find-value-k-in-given-complete-binary-tree-with-values-indexed-from-1-to-n
/*
Given a complete binary tree with values indexed from 1 to N and a key K. 
The task is to check whether a key exists in the tree or not. Print “true” if the
 key exists, otherwise print “false”. 

Examples: 
 Input: K = 2 
 
         1
       /   \  
     2      3  
    /  \   / \
   4    5 6   7
 /  \   /
8    9 10
Output: true 

Input: K = 11 
         1
       /   \  
     2      3  
    /  \   / \
   4    5 6   7
 /  \   /
8    9 10
Output: false 
*/

#include <stdio.h>
#include <malloc.h>
#include <math.h>

typedef struct node{
    int data;
    struct node *left, *right;
}treeNode;

treeNode* init_tree_node(int data){
    treeNode *node = (treeNode*)malloc(sizeof(treeNode));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

void pre(treeNode *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

int searchInCBT(treeNode *root, int k){
    int level = log2(k);
    int s = 1<<level;
    int e = (1<<(level+1)) - 1;
    while(root){
        if(root->data==k) return 1;
        int mid = s + (e-s)/2;
        if(k<=mid){
            e = mid;
            root = root->left;
        }else{
            s = mid+1;
            root = root->right;
        }
    }
    return 0;
}

int main(){
    treeNode *root = init_tree_node(1);
    root->left = init_tree_node(2);
    root->right = init_tree_node(3);
    root->left->left = init_tree_node(4);
    root->left->right = init_tree_node(5);
    root->right->left = init_tree_node(6);
    root->right->right = init_tree_node(7);
    root->left->left->left = init_tree_node(8);
    root->left->left->right = init_tree_node(9);
    root->left->right->left = init_tree_node(10);

    int k = 1;
    for(;k<=100;k++)
        printf("k = %d Is present =%d\n",k, searchInCBT(root, k));
}