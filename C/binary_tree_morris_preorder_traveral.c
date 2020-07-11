// https://www.geeksforgeeks.org/morris-traversal-for-preorder/?ref=rp

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    struct node *left, *right;
    int data;
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

tree_node* get_inorder_predecessor(tree_node *node){
    if(node==NULL) return NULL;
    tree_node *left_child = node->left;
    for(;left_child && left_child->right && left_child->right!=node;left_child=left_child->right);
    return left_child;
}

tree_node* morris_preorder(tree_node *root){
    while(root){
        tree_node *in_order_predecessor = get_inorder_predecessor(root);
        if(in_order_predecessor==NULL){
            printf("%d ",root->data);
            root = root->right;
        }else if(in_order_predecessor->right==root){
            in_order_predecessor->right = NULL;
            root = root->right;
        }else{
            in_order_predecessor->right = root;
            printf("%d ",root->data);
            root = root->left;
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

    root = make_node(1);  
    root->left = make_node(2);  
    root->right = make_node(3);  
  
    root->left->left = make_node(4);  
    root->left->right = make_node(5);  
  
    root->right->left = make_node(6);  
    root->right->right = make_node(7);  
  
    root->left->left->left = make_node(8);  
    root->left->left->right = make_node(9);  
  
    root->left->right->left = make_node(10);  
    root->left->right->right = make_node(11);  


    pre_order(root);
    printf("\n");

    morris_preorder(root);
    printf("\n");

    pre_order(root);
    printf("\n");

    return 0;
}