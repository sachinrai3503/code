// https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/?ref=rp
/*
Given a binary tree, a target node in the binary tree,
 and an integer value k, print all the nodes that are at distance k 
 from the given target node. No parent pointers are available.

BinaryTree
                    20
                8        22
            4     12
                10   14

Input: target = pointer to node with data 8.
root = pointer to node with data 20.
k = 2.
Output : 10 14 22
If target is 14 and k is 3, then output
should be “4 20”
*/

// For iterative sol- binary_tree_print_node_at_dist_k_from_given_node_iter.c

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

tree_node* search_node(tree_node *root, int data){
    while(root){
        if(root->data==data) return root;
        else if(root->data>data) root = root->left;
        else if(root->data<data) root = root->right;
    }
    return NULL;
}

void print_node_at_dist_k(tree_node *node, int cur_dist, int k){
    if(node==NULL)  return;
    if(cur_dist==k){
        printf("%d ",node->data);
        return;
    }else if(cur_dist>k) return;
    print_node_at_dist_k(node->left,cur_dist+1,k);
    print_node_at_dist_k(node->right,cur_dist+1,k);
}

int print_node_at_dist_k_from_given_node(tree_node *root, tree_node *data, 
            int k, int *found_flag){
    if(root==NULL) return 0;
    if(root==data){
        *found_flag = 1;
        print_node_at_dist_k(root,0,k);
        return 1;
    }
    int left = print_node_at_dist_k_from_given_node(root->left,data,k,
            found_flag);
    if(*found_flag==1){
        if(left==k) printf("%d ",root->data);
        else    print_node_at_dist_k(root->right,left+1,k);
        return  left+1;
    }else{
        int right = print_node_at_dist_k_from_given_node(root->right,data,k,
                    found_flag);
        if(*found_flag==1){
            if(right==k)    printf("%d ",root->data);
            else    print_node_at_dist_k(root->left,right+1,k);
            return  right+1;
        }else return 0;
    }
}

int main(){
    int ip[] = {20,5,4,7,6,8,15,14,13,12,11,10,16,17,18,25,24,23,27,26,128,100
                        ,90,80};
    int length = sizeof(ip)/sizeof(ip[0]);
    int data = 80;

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");
    printf("Data = %d\n",data);
    tree_node *node = search_node(root,data);

    int k = 0;
    for(;k<=length+1;k++){
        printf("K=%d ->",k);
        int found_flag = 0;
        print_node_at_dist_k_from_given_node(root,node,k,&found_flag);
        printf("\n");
    }

    return 0;
}