// https://www.geeksforgeeks.org/print-all-nodes-at-distance-k-from-given-node-iterative-approach/
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

// For iterative sol- binary_tree_print_node_at_dist_k_from_given_node.c

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

typedef struct{
    tree_node **data;
    int front, rear;
    int max_size;
}que;

que* init_que(int max_size){
    que *q = (que*)malloc(sizeof(que));
    if(q){
        q->data = (tree_node**)calloc(max_size,sizeof(tree_node*));
        q->front = q->rear = -1;
        q->max_size = max_size;
    }
    return q;
}

int is_full_que(que *q){
    if((q->front==0 && q->rear==q->max_size-1) || (q->rear==q->front-1))
        return 1;
    return 0;
}

int is_empty_que(que *q){
    if(q->front==-1) return 1;
    return 0;
}

void insert_que(que *q, tree_node *data){
    if(is_full_que(q)){
        printf("Full\n");
        return;
    }else if(data){
        if(q->rear==q->max_size-1) q->rear = 0;
        else q->rear++;
        if(q->front==-1) q->front=0;
        q->data[q->rear] = data;
    }
}

tree_node* delete_que(que *q){
    if(is_empty_que(q)){
        printf("Empty\n");
        return NULL;
    }else{
        tree_node *temp = q->data[q->front];
        if(q->front==q->rear) q->front = q->rear = -1;
        else if(q->front==q->max_size-1) q->front = 0;
        else q->front++;
        return temp;
    }
}

void print_que(que *q){
    int i = q->front;
    if(i>q->rear){
        while(i<q->max_size){
            if(q->data[i]->data!=INT_MAX)
                printf("%d ",q->data[i]->data);
            i++;
        }
        i = 0;
    }
    while(i<=q->rear){
        if(q->data[i]->data!=INT_MAX)
            printf("%d ",q->data[i]->data);
        i++;
    }
}

typedef struct{
    tree_node **data;
    int top,max_size;
}stck;

stck* init_stck(int max_size){
    stck *stk = (stck*)malloc(sizeof(stck));
    if(stk){
        stk->data = (tree_node**)calloc(max_size,sizeof(tree_node*));
        stk->top = -1;
        stk->max_size = max_size;
    }
    return stk;
}

int is_full_stck(stck *stk){
    if(stk->top==stk->max_size-1) return 1;
    return 0;
}

int is_empty_stck(stck *stck){
    if(stck->top==-1) return 1;
    return 0;
}

void push(stck *stk, tree_node *data){
    if(is_full_stck(stk)){
        printf("Full\n");
        return;
    }else if(data){
        stk->data[++stk->top] = data;
    }
}

tree_node* pop(stck *stk){
    if(is_empty_stck(stk)){
        printf("Empty\n");
        return NULL;
    }else{
        return stk->data[stk->top--];
    }
}

tree_node* stack_top(stck *stk){
    if(is_empty_stck(stk)){
        printf("Empty\n");
        return NULL;
    }
    return stk->data[stk->top];
}

void print_node_at_dist_k(tree_node *data, int k){
    que *q = init_que(20);
    tree_node *null_node = make_node(INT_MAX);
    insert_que(q,data);
    insert_que(q,null_node);
    int dist = 0;
    while(!is_empty_que(q) && q->data[q->front]!=null_node){
        int flag = 0;
        while(!is_empty_que(q) && q->data[q->front]!=null_node && dist<k){
            tree_node *temp = delete_que(q);
            insert_que(q,temp->left);
            insert_que(q,temp->right);
            flag = 1;
        }
        if(flag)    delete_que(q);
        if(dist==k){
            print_que(q);
            return;
        }else   dist++;
        insert_que(q,null_node);
    }
}

void print_parent_at_dist_k(stck *stk, int k){
    if(!is_empty_stck(stk)){
        int cur_dist = 1;
        tree_node *temp = pop(stk);
        while(!is_empty_stck(stk)){
            if(cur_dist>k){
                break;
            }else if(cur_dist==k){
                printf("%d ",stack_top(stk)->data);
                break;
            }else if(temp==stack_top(stk)->left){
                print_node_at_dist_k(stack_top(stk)->right,k-(cur_dist+1));
            }else{
                print_node_at_dist_k(stack_top(stk)->left,k-(cur_dist+1));
            }
            cur_dist++;
            temp = pop(stk);
        }
    }
}

int is_reqired_node(tree_node *node, int k, stck *stk){
    if(stack_top(stk)==node){
        print_node_at_dist_k(node,k);
        print_parent_at_dist_k(stk,k);
        return 1;
    }
    return 0;
}

void print_node_at_dist_k_from_given_node(tree_node *root, tree_node *node, 
                int k){
    if(root==NULL) return;
    stck *stk = init_stck(20);
    push(stk,root);
    if(is_reqired_node(node,k,stk)) return;
    while(!is_empty_stck(stk)){
        while(stack_top(stk)->left){
            push(stk,stack_top(stk)->left);
            if(is_reqired_node(node,k,stk)) return;
        }
        if(stack_top(stk)->right){
            push(stk,stack_top(stk)->right);
            if(is_reqired_node(node,k,stk)) return;
        }else{
            tree_node *temp = pop(stk);
            while(!is_empty_stck(stk) && (!stack_top(stk)->right ||
                       stack_top(stk)->right==temp)){
                temp = pop(stk);
            }
            if(!is_empty_stck(stk) && temp==stack_top(stk)->left){
                push(stk,stack_top(stk)->right);
                if(is_reqired_node(node,k,stk)) return;
            }
        }
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
        print_node_at_dist_k_from_given_node(root,node,k);
        printf("\n");
    }

    return 0;
}