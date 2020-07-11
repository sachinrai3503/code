#include <stdio.h>
#include <limits.h>
#include <malloc.h>

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
    else if(root->data>data) root->left = make_tree(root->left,data);
    else if(root->data<data) root->right = make_tree(root->right,data);
    return root;
}

void in_order(tree_node *root){
    if(root){
        in_order(root->left);
        printf("%d ",root->data);
        in_order(root->right);
    }
}

tree_node* get_in_order_predecessor(tree_node *node){
    if(node==NULL) return NULL;
    tree_node *left_child = node->left;
    for(;left_child && left_child->right && left_child->right!=node;left_child=left_child->right);
    return left_child;
}

tree_node* get_in_order_successor(tree_node *node){
    if(node==NULL) return NULL;
    tree_node *right_child = node->right;
    for(;right_child && right_child->left && right_child->left!=node;right_child=right_child->left);
    return right_child;
}

//https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
/*
Inorder tree traversal using morris traversal
*/
void in_order_morris(tree_node *root){
    while(root){
        tree_node *in_order_predecessor = get_in_order_predecessor(root);
        if(in_order_predecessor==NULL || in_order_predecessor->right==root){
            if(in_order_predecessor) in_order_predecessor->right = NULL;
            printf("%d ",root->data);
            root = root->right;
        }else{
            in_order_predecessor->right = root;
            root = root->left;
        }
    }
}

//https://www.geeksforgeeks.org/reverse-morris-traversal-using-threaded-binary-tree/?ref=rp
/**
 * Given a binary tree, task is to do reverse inorder traversal using Morris Traversal.
 */
void reverse_in_order_morris(tree_node *root){
    while(root){
        tree_node *in_order_successor = get_in_order_successor(root);
        if(in_order_successor==NULL || in_order_successor->left==root){
            if(in_order_successor) in_order_successor->left = NULL;
            printf("%d ",root->data);
            root = root->left;
        }else{
            in_order_successor->left = root;
            root = root->right;
        }
    }
}

int main(){
    int ip[] = {100,75,60,50,65,62,80,83,81,90,125,130,135,133,138};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    in_order(root);
    printf("\n");

    in_order_morris(root);
    printf("\n");
    reverse_in_order_morris(root);
    printf("\n");

    return 0;
}