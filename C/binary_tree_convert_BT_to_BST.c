// https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/
/*
Given a Binary Tree, convert it to a Binary Search Tree.
The conversion should keep the original structure of Binary Tree.
Examples.

Example 1
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7


Example 2
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30
*/

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

void print_pre_order(tree_node *root){
    if(root){
        printf("%d ",root->data);
        print_pre_order(root->left);
        print_pre_order(root->right);
    }
}

void print_in_order(tree_node *root){
    if(root){
        print_in_order(root->left);
        printf("%d ",root->data);
        print_in_order(root->right);
    }
}

void set_inorder(tree_node *root, tree_node **inorder_arr, int *k){
    if(root==NULL) return;
    set_inorder(root->left,inorder_arr,k);
    inorder_arr[(*k)++] = root;
    set_inorder(root->right,inorder_arr,k);
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int *inorder_arr, int length){
    int i = 0;
    for(;i<length;i++){
        int min = i;
        int j = i+1;
        for(;j<length;j++){
            if(inorder_arr[j]<inorder_arr[min]){
                min = j;
            }
        }
        swap(inorder_arr+i,inorder_arr+min);
    }
}

int binary_search(int *ip, int s, int e, int data){
    while(s<=e){
        int mid = (s+e)/2;
        if(ip[mid]==data) return mid;
        if(ip[mid]>data) e = mid-1;
        else s = mid+1;
    }
    return -1;
}

int* copy(tree_node **ip, int length){
    int *op = (int*)calloc(length,sizeof(int*));
    if(op){
        int i = 0;
        for(;i<length;i++){
            op[i] = ip[i]->data;
        }
    }
    return op;
}

void convert_to_BST(tree_node *root){
    tree_node **actual_in_order = (tree_node**)calloc(30,sizeof(tree_node*));
    int k = 0;
    set_inorder(root,actual_in_order,&k);
    int *expected_in_order = copy(actual_in_order,k);
    sort(expected_in_order,k);
    int i = 0;
    while(i<k){
        int temp = actual_in_order[i]->data;
        int expected_index = binary_search(expected_in_order,0,k-1,temp);
        if(expected_index!=i){
            actual_in_order[i]->data = actual_in_order[expected_index]->data;
            actual_in_order[expected_index]->data = temp;
        }else{
            i++;
        }
    }
}

int main(){

    tree_node *root = NULL;
    root = make_node(10);
    root->left = make_node(30);
    root->right = make_node(15);
    root->left->left = make_node(20);
    root->right->right = make_node(5);

    print_pre_order(root);
    printf("\n");
    convert_to_BST(root);
    print_pre_order(root);
    printf("\n");
    print_in_order(root);

    return 0;
}