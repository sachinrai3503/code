// https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
/*
The diameter of a tree (sometimes called the width) is the number of nodes
 on the longest path between two end nodes.
*/

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

void pre_order(tree_node *root){
    if(root){
        printf("%d ",root->data);
        pre_order(root->left);
        pre_order(root->right);
    }
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int get_diameter(tree_node *root, int *max_diameter){
    if(root==NULL) return 0;
    int left = get_diameter(root->left,max_diameter);
    int right = get_diameter(root->right,max_diameter);
    if(left!=0 && right!=0){
        if(left+right+1>*max_diameter){
            *max_diameter = left+right+1;
        }
    }
    return 1 + get_max(left,right);
}

int main(){
    int ip[] = {5,4,3,2,1,6};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    // int i=0;
    // for(;i<length;i++){
    //     root = make_tree(root,ip[i]);
    // }
    root = make_node(1); 
    root->left        = make_node(2); 
    root->right       = make_node(3); 
    root->left->left  = make_node(4); 
    root->left->right = make_node(5);

    pre_order(root);
    printf("\n");

    int diameter = 0;
    get_diameter(root,&diameter);
    printf("diameter = %d\n",diameter);
    return 0;
}