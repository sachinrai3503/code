// https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/?ref=rp
/*
Iterative Postorder Traversal Using One Stack
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    struct node *left, *right;
    int data;
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

void post_order(tree_node *root){
    if(root){
        post_order(root->left);
        post_order(root->right);
        printf("%d ",root->data);
    }
}

typedef struct {
    tree_node **data;
    int top, max_size;
}stack;

stack* init_stack(int max_size){
    stack *stck = (stack*)malloc(sizeof(stack));
    if(stck){
        stck->top = -1;
        stck->data = (tree_node**)calloc(max_size,sizeof(tree_node*));
        stck->max_size = max_size;
    }
    return stck;
}

int is_empty(stack *stck){
    if(stck->top==-1) return 1;
    return 0;
}

int is_full(stack *stck){
    if(stck->top==stck->max_size-1) return 1;
    return 0;
}

void push(stack *stck, tree_node *data){
    if(is_full(stck)){
        printf("Full\n");
    }else if(data){
        stck->data[++stck->top] = data;
    }
}

tree_node* pop(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return NULL;
    }else{
        return stck->data[stck->top--];
    }
}

tree_node* stack_top(stack *stck){
    if(is_empty(stck)){
        printf("Empty\n");
        return NULL;
    }
    return stck->data[stck->top];
}

void postorder_1_stack(tree_node *root){
    stack *stck = init_stack(20);
    push(stck,root);
    while(!is_empty(stck)){
        while(stack_top(stck)->left){
            push(stck,stack_top(stck)->left);
        }
        if(stack_top(stck)->right){
            push(stck,stack_top(stck)->right);
        }else{
            tree_node *prev = NULL;
            while(!is_empty(stck) && (stack_top(stck)->right==NULL || stack_top(stck)->right==prev)){
                tree_node *temp = pop(stck);
                printf("%d ",temp->data);
                prev = temp;
            }
            if(!is_empty(stck) && stack_top(stck)->right!=prev){
                push(stck,stack_top(stck)->right);
            }
        }
    }
}

int main(){
    int ip[] = {100,75,60,50,65,62,80,83,81,90,125,130,135,133,138};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    // int i = 0;
    // for(;i<length;i++){
    //     root = make_tree(root,ip[i]);
    // }
    root = make_node(8);
    root->left = make_node(3); 
    root->right = make_node(10); 
    root->left->left = make_node(1); 
    root->left->right = make_node(6); 
    root->left->right->left = make_node(4); 
    root->left->right->right = make_node(7); 
    root->right->right = make_node(14); 
    root->right->right->left = make_node(13); 

    post_order(root);
    printf("\n");

    postorder_1_stack(root);
    printf("\n");

    return 0;
}