// https://www.geeksforgeeks.org/burn-the-binary-tree-starting-from-the-target-node/
/*
Given a binary tree and target node. By giving the fire to the target node 
and fire starts to spread in a complete tree. The task is to print the sequence
 of the burning nodes of a binary tree.

Rules for burning the nodes :

Fire will spread constantly to the connected nodes only.
Every node takes the same time to burn.
A node burns only once.
Examples:

Input : 
                       12
                     /     \
                   13       10
                          /     \
                       14       15
                      /   \     /  \
                     21   24   22   23
target node = 14

Output :
14
21, 24, 10
15, 12
22, 23, 13
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

typedef struct SLL_node{
    tree_node *data;
    struct SLL_node *next;
}list_node;

list_node* make_list_node(tree_node *data){
    list_node *node = (list_node*)malloc(sizeof(list_node));
    if(node){
        node->data = data;
        node->next = node;
    }
    return node;
}

list_node* append(list_node *last, tree_node *data){
    list_node *node = make_list_node(data);
    if(!last) return node;
    node->next = last->next;
    last->next = node;
    return node;
}

void print_list(list_node *last){
    if(last){
        list_node *temp = last->next;
        for(;temp && temp!=last;temp=temp->next) 
            printf("%d ",temp->data->data);
        printf("%d ",temp->data->data);
    }
    printf("\n");
}

void print_burnt_nodes(list_node **data, int length){
    int i = 0;
    for(;i<length && data[i];i++){
        print_list(data[i]);
    }
}

void burn_child_node(tree_node *root, list_node **op, int index){
    if(root==NULL) return;
    op[index] = append(op[index],root);
    burn_child_node(root->left,op,index+1);
    burn_child_node(root->right,op,index+1);
}

int print_burning_node(tree_node *root, int target, list_node **op, int index){
    if(!root) return 0;
    if(root->data==target){
        op[0] = append(op[0],root);
        burn_child_node(root->left,op,1);
        burn_child_node(root->right,op,1);
        return 1;
    }
    int left = print_burning_node(root->left,target,op,index);
    if(left!=0){
        op[left] = append(op[left],root);
        burn_child_node(root->right,op,left+1);
        return left+1;
    }
    int right = print_burning_node(root->right,target,op,index);
    if(right!=0){
        op[right] = append(op[right],root);
        burn_child_node(root->left,op,right+1);
        return right+1;
    }
    return 0;
}

int main(){
    int ip[] = {100,50,25,10,30,32,34,75,50,80,200,150,130,170,160,180,175,190,
                250,225,300,275,350};
    int target = 275;

    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");

    list_node **op = (list_node**)calloc(20,sizeof(list_node*));
    print_burning_node(root,target,op,0);
    print_burnt_nodes(op,20);

    return 0;
}