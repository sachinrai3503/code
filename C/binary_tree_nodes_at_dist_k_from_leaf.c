// https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/?ref=rp
/*
Given a Binary Tree and a positive integer k, 
print all nodes that are distance k from a leaf node.

Here k distance from a leaf means k levels higher than a leaf node. 
For example if k is more than height of Binary Tree, 
then nothing should be printed. 

Expected time complexity is O(n) where n is the number nodes in the 
given Binary Tree.

                        1
                    2        3
                  4   5   6     7
                            8

Nodes at dist 1 from leaf node -> 2,6,3
Nodes at dist 2 from leaf node -> 1,3
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_tree_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_tree_node(data);
    else if(root->data>data) root->left = make_tree(root->left,data);
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

typedef struct{
    int data, visited;
}list_node;

list_node* make_list_node(int data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->visited = 0;
    }
    return node;
}

int is_leaf(tree_node *node){
    if(node->left==NULL && node->right==NULL) return 1;
    return 0;
}

void print_node_at_dist_k_from_leaf(tree_node *root, int k, list_node **list,
            int level){
    if(root==NULL) return;
    list[level] = make_list_node(root->data);
    if(is_leaf(root)){
        if((level-k>=0) && list[level-k]->visited==0){
            printf("%d ",list[level-k]->data);
            list[level-k]->visited = 1;
        }
        return;
    }
    print_node_at_dist_k_from_leaf(root->left,k,list,level+1);
    print_node_at_dist_k_from_leaf(root->right,k,list,level+1);
}

int main(){
    int ip[] = {10,5,1,8,15,13,12,17};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");

    list_node **list = (list_node**)calloc(length,sizeof(list_node*));

    int k = 0;
    for(;k<=length+1;k++){
        printf("k=%d>",k);
        print_node_at_dist_k_from_leaf(root,k,list,0);
        printf("\n");
    }
    return 0;
}