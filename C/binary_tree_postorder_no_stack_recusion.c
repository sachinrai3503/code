// https://www.geeksforgeeks.org/postorder-traversal-binary-tree-without-recursion-without-stack/
/*
Will use an extra parent attribute in tree node
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    struct node *left, *right, *parent;
    int data;
}tree_node;

tree_node* make_node(int data){
    tree_node *nw = (tree_node*)malloc(sizeof(tree_node));
    if(nw){
        nw->data = data;
        nw->left = nw->right = NULL;
        nw->parent = NULL;
    }
    return nw;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_node(data);
    if(root->data>data) root->left = make_tree(root->left,data);
    else if(root->data<data) root->right = make_tree(root->right,data);
    return root;
}

void post_order(tree_node *root){
    if(root){
        post_order(root->left);
        post_order(root->right);
        printf("%d ",root->data);
    }
}

void postorder_no_stack_rec(tree_node *root){
    while(root){
        if(root->left && root->left->parent==NULL){
            root->left->parent = root;
            root = root->left;
        }else if(root->right && root->right->parent==NULL){
            root->right->parent = root;
            root = root->right;
        }else{
            printf("%d ",root->data);
            root = root->parent;
        }
    }
}

int main(){
    int ip[] = {100,75,60,50,65,62,80,83,81,90,125,130,135,133,138};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    // int i = 0;
    // for(;i<length;i++){
    //     root = make_tree(root,ip[i]);
    // }
    root = make_node(8);
    root->left = make_node(3); 
    root->right = make_node(10); 
    root->left->left = make_node(1); 
    root->left->right = make_node(6); 
    root->left->right->left = make_node(4); 
    root->left->right->right = make_node(7); 
    root->right->right = make_node(14); 
    root->right->right->left = make_node(13); 

    post_order(root);
    printf("\n");

    postorder_no_stack_rec(root);
    printf("\n");

    return 0;
}