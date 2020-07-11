#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    struct node *left, *right;
    int data;
}my_node;

my_node* make_node(int data){
    my_node *nw = (my_node*)malloc(sizeof(my_node));
    if(nw){
        nw->left = nw->right = NULL;
        nw->data = data;
    }
    return nw;
}

my_node* make_tree(my_node *root, int data){
    if(root==NULL) return make_node(data);
    if(root->data>data) root->left = make_tree(root->left,data);
    else if(root->data<data) root->right = make_tree(root->right,data);
    return root;
}

void pre(my_node *root){
    if(root){
        printf("%d ",root->data);
        pre(root->left);
        pre(root->right);
    }
}

void in(my_node *root){
    if(root){
        in(root->left);
        printf("%d ",root->data);
        in(root->right);
    }
}

void print_left_side(my_node *root){
    if(root==NULL) return;
    if(root->left){
        printf("%d ",root->data);
        print_left_side(root->left);
    }else if(root->right){
        printf("%d ",root->data);
        print_left_side(root->right);
    }
}

void print_leaf_node(my_node *root){
    if(root==NULL) return;
    if(root->left==NULL && root->right==NULL) printf("%d ",root->data);
    print_leaf_node(root->left);
    print_leaf_node(root->right);
}

void print_right_side(my_node *root){
    if(root==NULL) return;
    if(root->right){
        print_right_side(root->right);
        printf("%d ",root->data);
    }else if(root->left){
        print_right_side(root->left);
        printf("%d ",root->data);
    }
}

void print_right(my_node *root){
    while(root && root->right==NULL){
        root = root->left;
    }
    while(root && root->left==NULL){
        root = root->right;
    }
    if(root){
        print_right_side(root->right);
    }
}

int main(){
    int ip[] = {200,180,150,160,170,165,175,174,176,177};
    int length = sizeof(ip)/sizeof(ip[0]);

    my_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre(root);
    printf("\n");
    in(root);
    printf("\n");

    print_left_side(root);
    print_leaf_node(root);
    print_right(root);

    return 0;
}