// https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/
/*
Given a binary tree. Modify it in such a way that 
after modification you can have a preorder traversal 
of it using only the right pointers. 
During modification, you can use right as well as left pointers.

Examples:
Input :    10
          /   \
        8      2
      /  \    
    3     5  
Output :    10
              \
               8
                \ 
                 3
                  \
                   5
                    \
                     2
Explanation : The preorder traversal
of given binary tree is 10 8 3 5 2.
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

void pre(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

tree_node* get_preorder_predecessor(tree_node *root, tree_node *r_child){
    if(r_child==NULL) return NULL;
    if(root==NULL) return NULL;
    if(root->left==NULL) return root;
    tree_node *temp = root->left;
    while(temp){
        if(temp->right) temp = temp->right;
        else if(temp->left) temp = temp->left;
        else return temp;
    }
    return NULL;
}

tree_node* get_preorder_successor(tree_node *node){
    if(!node) return NULL;
    if(node->left) return node->left;
    return node->right;
}

tree_node* modify_tree(tree_node *root){
    if(root==NULL) return NULL;
    tree_node *r_child_preorder_pred = get_preorder_predecessor(root,root->right);
    tree_node *preorder_successor = get_preorder_successor(root);
    modify_tree(root->left);
    modify_tree(root->right);
    if(root->right){
        r_child_preorder_pred->right = root->right;
    }
    root->right = preorder_successor;
    root->left = NULL;
    return root;
}

int main(){

    int ip[] = {100,50,25,40,35,45,42,55,80,75,105,130,125,120,130,128};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }

    // root = make_node(10);
    // root->left = make_node(8);
    // root->right = make_node(2);
    // root->left->left = make_node(3);
    // root->left->right = make_node(5);  

    pre(root);
    printf("\n");

    tree_node *modified_tree = modify_tree(root);
    pre(modified_tree);

    return 0;
}