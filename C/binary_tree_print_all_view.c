// Code for printing Top/Bottom/Left/Right view of Binary tree.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}tree_node;

tree_node* make_tree_node(int data){
    tree_node *nw = (tree_node*)malloc(sizeof(tree_node));
    if(nw){
        nw->data = data;
        nw->left = nw->right = NULL;
    }
    return nw;
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

typedef struct SCLL_node{
    tree_node *data;
    struct SCLL_node *next;
}list_node;

list_node* make_list_node(tree_node *data){
    list_node *nw = (list_node*)malloc(sizeof(list_node));
    if(nw){
        nw->data = data;
        nw->next = nw;
    }
    return nw;
}

list_node* insert_in_list(list_node *last, list_node *data){
    if(last){
        data->next = last->next;
        last->next = data;
    }
    return data;
}

void print_SCLL(list_node *last){
    if(last){
        list_node *first = last->next;
        for(;first!=last;first=first->next)
            printf("%d ",first->data->data);
        printf("%d ",first->data->data);
    }
    printf("\n");
}

// For bottom view
typedef struct DLL_node_bottom{
    int max_level;
    list_node *last;
    struct DLL_node_bottom *left, *right;
}dll_node_botttom;

dll_node_botttom* make_dll_bottom_node(){
    dll_node_botttom *nw = (dll_node_botttom*)malloc(sizeof(dll_node_botttom));
    if(nw){
        nw->last = NULL;
        nw->max_level = -1;
        nw->left = nw->right = NULL;
    }
    return nw;
}

dll_node_botttom* get_left_most_node_bottom(dll_node_botttom *node){
    for(;node && node->left;node=node->left);
    return node;
}

void print_DLL_bottom(dll_node_botttom *node){
    dll_node_botttom *first_node = get_left_most_node_bottom(node);
    for(;first_node;first_node=first_node->right){
        print_SCLL(first_node->last);
    }
}

// For top view
typedef struct DLL_node_top{
    int min_level;
    int data;
    struct DLL_node_top *left, *right;
}dll_node_top;

dll_node_top* make_dll_top_node(){
    dll_node_top *nw = (dll_node_top*)malloc(sizeof(dll_node_top));
    if(nw){
        nw->data = INT_MIN;
        nw->min_level = INT_MAX;
        nw->left = nw->right = NULL;
    }
    return nw;
}

dll_node_top* get_left_most_node_top(dll_node_top *node){
    for(;node && node->left;node=node->left);
    return node;
}

void print_DLL_top(dll_node_top *node){
    dll_node_top *first_node = get_left_most_node_top(node);
    for(;first_node;first_node=first_node->right){
        printf("%d ",first_node->data);
    }
    printf("\n");
}

// https://www.geeksforgeeks.org/bottom-view-binary-tree/
dll_node_botttom* get_bottom_view(tree_node *root, int cur_level,
     dll_node_botttom *left, dll_node_botttom *center, dll_node_botttom *right){
    if(root==NULL) return center;
    if(center==NULL){
        center = make_dll_bottom_node();
        center->left = left;
        center->right = right;
        if(right) right->left = center;
        if(left) left->right = center;
    }
    if(cur_level>=center->max_level){
        if(cur_level>center->max_level && center->last){
            free(center->last->next);
            center->last = NULL;
        }
        center->last = insert_in_list(center->last,make_list_node(root));
        center->max_level = cur_level;
    }
    dll_node_botttom *left_left = NULL;
    if(center->left)
        left_left = center->left->left;
    get_bottom_view(root->left,cur_level+1,left_left,center->left,center);
    dll_node_botttom *right_right = NULL;
    if(center->right)
        right_right = center->right->right;
    get_bottom_view(root->right,cur_level+1,center,center->right,right_right);
    return center;
}

// https://www.geeksforgeeks.org/print-nodes-in-top-view-of-binary-tree-set-2/?ref=rp
dll_node_top* get_top_view(tree_node *root, int cur_level, dll_node_top *left,
            dll_node_top *center, dll_node_top *right){
    if(root==NULL){
        return center;
    }
    if(center==NULL){
        center = make_dll_top_node();
        center->left = left;
        center->right = right;
        if(left) left->right = center;
        if(right) right->left = center;
    }
    if(cur_level<center->min_level){
        center->data = root->data;
        center->min_level = cur_level;
    }
    dll_node_top *left_left = NULL;
    if(center->left)
        left_left = center->left->left;
    get_top_view(root->left,cur_level+1,left_left,center->left,center);
    dll_node_top *right_right = NULL;
    if(center->right)
        right_right = center->right->right;
    get_top_view(root->right,cur_level+1,center,center->right,right_right);
    return center;
}

void print_left_view(tree_node *root, int cur_level, int *max_level){
    if(root==NULL) return;
    if(cur_level>*max_level){
        printf("%d ",root->data);
        *max_level = cur_level;
    }
    print_left_view(root->left,cur_level+1,max_level);
    print_left_view(root->right,cur_level+1,max_level);
}

void print_right_view(tree_node *root, int cur_level, int *max_level){
    if(root==NULL) return;
    if(cur_level>*max_level){
        printf("%d ",root->data);
        *max_level = cur_level;
    }
    print_right_view(root->right,cur_level+1,max_level);
    print_right_view(root->left,cur_level+1,max_level);
}

int main(){
    int ip[] = {20,5,4,7,6,8,25,24,23,27,26,128,100,90,80};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    // tree_node* root = make_tree_node(1); 
    // root->right = make_tree_node(2); 
    // root->right->right = make_tree_node(4); 
    // root->right->right->left = make_tree_node(3); 
    // root->right->right->right = make_tree_node(5);

    pre(root);
    printf("\n");

    dll_node_botttom *bottom_view = get_bottom_view(root,0,NULL,NULL,NULL);
    printf("Bottom View = ");
    print_DLL_bottom(bottom_view);

    int max_level = -1;
    printf("Left view = ");
    print_left_view(root,0,&max_level);
    printf("\n");

    max_level = -1;
    printf("Right view = ");
    print_right_view(root,0,&max_level);
    printf("\n");

    dll_node_top *top_view = get_top_view(root,0,NULL,NULL,NULL);
    printf("Top view = ");
    print_DLL_top(top_view);

    return 0;
}