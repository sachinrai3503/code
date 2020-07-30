// https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
/*
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). 
The left and right pointers in nodes are to be used as previous and next
 pointers respectively in converted DLL. 
 
The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
The first node of Inorder traversal (left most node in BT) must be
 head node of the DLL.
*/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }   
    return node;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return make_node(data);
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

void print_list(tree_node *head){
    for(;head;head=head->right){
        printf("%d ",head->data);
    }
    printf("\n");
}

tree_node* join(tree_node *list1_last, tree_node *list2_last){
     if(list1_last==NULL) return list2_last;
     if(list2_last==NULL) return list1_last;
     tree_node *head2 = list2_last->right;
     list2_last->right = list1_last->right;
     list1_last->right = head2;
     head2->left = list1_last;
     return list2_last;
}

tree_node* to_DLL(tree_node *root){
    if(root==NULL) return NULL;
    tree_node *left_last = to_DLL(root->left);
    tree_node *right_last = to_DLL(root->right);
    root->left = root->right = NULL;
    root->right = root;
    return (join(join(left_last,root),right_last));
}

tree_node* convert_tree_to_DLL(tree_node *root){
    tree_node *last = to_DLL(root);
    if(!last) return last;
    tree_node *first = last->right;
    last->right = NULL;
    return first;
}

int main(){
    int ip[] = {100,80,50,10,70,60,75,72,82,90,85,150,200,202,175,170};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int  i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");

    tree_node *head = convert_tree_to_DLL(root);
    print_list(head);

    return 0;
}