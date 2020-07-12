// https://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
/*
Given a Singly Linked List which has data members sorted in ascending order. 
Construct a Balanced BST which has same data members as the given Linked List.

Expected time complextity = O(n)

Examples:
Input:  Linked List 1->2->3
Output: A Balanced BST 
     2   
   /  \  
  1    3 
Input: Linked List 1->2->3->4->5->6->7
Output: A Balanced BST
        4
      /   \
     2     6
   /  \   / \
  1   3  5   7  
Input: Linked List 1->2->3->4
Output: A Balanced BST
      3   
    /  \  
   2    4 
 / 
1
Input:  Linked List 1->2->3->4->5->6
Output: A Balanced BST
      4   
    /   \  
   2     6 
 /  \   / 
1   3  5   
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct list_node{
    int data;
    struct list_node *next;
}list;

typedef struct tree_node{
    int data;
    struct tree_node *left, *right;
}tree;

list* init_list_node(int data){
    list *node = (list*)malloc(sizeof(list));
    if(node){
        node->data = data;
        node->next = NULL;
    }
    return node;
}

list* insert_in_list(list *head, int data){
    list *node = init_list_node(data);
    node->next = head;
    return node;
}

tree* init_tree_node(int data){
    tree *node = (tree*)malloc(sizeof(tree));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

void pre(tree *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

void print_list(list *head){
    for(;head;head=head->next){
        printf("%d ",head->data);
    }
    printf("\n");
}

int get_list_len(list *head){
    int len = 0;
    for(;head;len++,head=head->next);
    return len;
}

tree* to_balanced_BST(list **node, int s, int e){
    if(s>e){
        return NULL;
    }
    int mid = (s+e)/2;
    tree *left = to_balanced_BST(node,s,mid-1);
    tree *root = init_tree_node((*node)->data);
    (*node) = (*node)->next;
    tree* right = to_balanced_BST(node,mid+1,e);
    root->left = left;
    root->right = right;
    return root;
}

int main(){
    int ip[] = {1,2,3,4,5,6};
    int length = sizeof(ip)/sizeof(ip[0]);
    list *head = NULL;
    int i = length-1;
    for(;i>=0;i--){
        head = insert_in_list(head,ip[i]);
    }
    printf("List =>");
    print_list(head);
    int list_len = get_list_len(head);
    tree *root = to_balanced_BST(&head,0,list_len-1);
    printf("tree =>");
    pre(root);

    return 0;
}
    