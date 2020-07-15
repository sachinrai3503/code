// https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

/*
A program to check if a binary tree is BST or notA program to check if 
a binary tree is BST or not
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* init_node(int data){
    tree_node *nw = (tree_node*)malloc(sizeof(tree_node));
    if(nw){
        nw->data = data;
        nw->left = nw->right = NULL;
    }
    return nw;
}

void pre(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

int is_valid_BST(tree_node *root, int min, int max){
    if(root==NULL) return 1;
    if(root->data<min || root->data>max) return 0;
    return is_valid_BST(root->left,min,root->data) &&
        is_valid_BST(root->right,root->data,max);
}

int is_BST(tree_node *root){
    return is_valid_BST(root,INT_MIN,INT_MAX);
}

int main(){

    /*
        Valid BST
                        20
                15               25
        10          17      22          27
            13   16   18

        invalid BST
                        20
                15               25
         10         17      22          27
            13  '14'   18
    */

    tree_node *root = init_node(20);
    root->left = init_node(15);
    root->left->left = init_node(10);
    root->left->left->right = init_node(13);
    root->left->right = init_node(17);
    root->left->right->left = init_node(14); // Wrong node
    root->left->right->right = init_node(18);
    root->right = init_node(25);
    root->right->left = init_node(22);
    root->right->right = init_node(27);

    pre(root);
    printf("\n");
    printf("Is Valid BST = %d\n",is_BST(root));

    return 0;
}