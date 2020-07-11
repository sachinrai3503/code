// https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

/**
* Given a binary tree in which each node element contains a number.
* Find the maximum possible sum from one leaf node to another.
* The maximum sum path may or may not go through root.
*/
 
#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_node(int data){
    tree_node *nw = (tree_node*)malloc(sizeof(tree_node));
    if(nw){
        nw->data = data;
        nw->left = nw->right = NULL;
    }
    return nw;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_node(data);
    if(root->data>data) root->left = make_tree(root->left,data);
    else if(root->data<data) root->right = make_tree(root->right,data);
    return root;
}

void pre_order(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre_order(root->left);
        pre_order(root->right);
    }
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int max_leaf_to_leaf_path_sum(tree_node *root, int *max_sum){
    if(root==NULL) return INT_MAX;
    int left = max_leaf_to_leaf_path_sum(root->left,max_sum);
    int right = max_leaf_to_leaf_path_sum(root->right,max_sum);
    if(left!=INT_MAX && right!=INT_MAX){
        if(root->data+left+right>*max_sum) *max_sum = root->data+left+right;
        return root->data + get_max(left,right);
    }else if(left!=INT_MAX){
        return root->data + left;
    }else if(right!=INT_MAX){
        return root->data + right;
    }
    return root->data;
}

int main(){
    int ip[] = {};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre_order(root);
    printf("\n");

    int max_sum = INT_MIN;
    max_leaf_to_leaf_path_sum(root,&max_sum);
    printf("max_sum = %d ",max_sum);

    return 0;
}