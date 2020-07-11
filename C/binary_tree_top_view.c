// https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
// https://www.geeksforgeeks.org/print-nodes-in-top-view-of-binary-tree-set-2/

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

typedef struct binary_tree_node{
    struct binary_tree_node *left, *right;
    int data;
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

void print_tree_pre_order(tree_node *root){
    if(root){
        printf("%d ",root->data);
        print_tree_pre_order(root->left);
        print_tree_pre_order(root->right);
    }
}

typedef struct dll_node{
    struct dll_node *left,*right;
    int level, data;
}list_node;

list_node* make_list_node(int level, int data){
    list_node *nw = (list_node*)malloc(sizeof(list_node));
    if(nw){
        nw->left = nw->right = NULL;
        nw->level = level;
        nw->data = data;
    }
    return nw;
}

list_node* get_left_node(list_node *node){
    for(;node && node->left;node = node->left);
    return node;
}

void print_list(list_node *node){
    for(;node;node=node->right)
        printf("%d ",node->data);
    printf("\n");
}

list_node* top_view_of_binary_tree(tree_node *root, list_node *left, list_node *center, list_node *right, int level){
    if(root==NULL) return NULL;
    if(center==NULL){
        center = make_list_node(level,root->data);
        center->right = right;
        center->left = left;
        if(right) right->left = center;
        if(left) left->right = center;
    }
    if(center->level>level){
        center->level = level;
        center->data = root->data;
    }
    list_node *left_left = NULL, *right_right = NULL;
    if(center->left) left_left = center->left->left;
    top_view_of_binary_tree(root->left,left_left,left,center,level+1);
    if(center->right) right_right = center->right->right;
    top_view_of_binary_tree(root->right,center,right,right_right,level+1);
    return center;
}

int main(){
    int ip[] = {10,20,30,9,2,3,4,5,6,7};
    int length = sizeof(ip)/sizeof(ip[0]);

    // tree_node *root = NULL;
    // int i = 0;
    // for(;i<length;i++){
    //     root = make_tree(root,ip[i]);
    // }

    tree_node* root = make_tree_node(1); 
    root->left = make_tree_node(2); 
    root->right = make_tree_node(3); 
    root->left->right = make_tree_node(4); 
    root->left->right->right = make_tree_node(5); 
    root->left->right->right->right = make_tree_node(6); 

    print_tree_pre_order(root);
    printf("\n");

    list_node *center = top_view_of_binary_tree(root,NULL,NULL,NULL,0);
    print_list(get_left_node(center));

    return 0;
}