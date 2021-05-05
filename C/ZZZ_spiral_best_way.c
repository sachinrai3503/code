// https://www.geeksforgeeks.org/anti-clockwise-spiral-traversal-of-a-binary-tree/
#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct treenode{
    int data;
    struct treenode *left, *right;
}tree_node;

tree_node* init_tree_node(int data){
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

tree_node* make_tree(tree_node *root, int data){
    if(root==NULL) return init_tree_node(data);
    if(root->data>data) root->left = make_tree(root->left, data);
    else if(root->data<data) root->right = make_tree(root->right, data);
}

void print_tree(tree_node *root){
    if(root){
        printf("%d ",root->data);
        print_tree(root->left);
        print_tree(root->right);
    }
}

typedef struct DCLL{
    tree_node *data;
    struct DCLL *next, *prev;
}dcll;

dcll* init_dcll_node(tree_node *data){
    dcll *node = (dcll*)malloc(sizeof(dcll));
    if(node){
        node->data = data;
        node->next = node->prev = node;
    }
    return node;
}

dcll* insert_dcll_node(dcll* head, tree_node *data){
    if(!data) return head;
    dcll *node = init_dcll_node(data);
    if(!head) return node;
    node->prev = head->prev;
    head->prev->next = node;
    node->next = head;
    head->prev = node;
    return head;
}

void print_dll_forward(dcll *head){
    if(!head) return;
    dcll *last = head->prev;
    while(head!=last){
        printf("%d ",head->data->data);
        head = head->next;
    }
    printf("%d ",head->data->data);
    printf("\n");
}

void print_dll_back(dcll *head){
    if(!head) return;
    dcll *first = head;
    head = head->prev;
    while(head!=first){
        printf("%d ",head->data->data);
        head = head->prev;
    }
    printf("%d ",head->data->data);
    printf("\n");
}

typedef struct queuenode{
    dcll *head;
    struct  queuenode *next, *prev;
}queue_node;

queue_node* init_queue_node(dcll *data){
    queue_node *node = (queue_node*)malloc(sizeof(queue_node));
    if(node){
        node->head = data;
        node->next = node->prev = NULL;
    }
    return node;
}

typedef struct{
    queue_node *front, *rear;
}queue;

queue* init_queue(){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->front = que->rear = NULL;
    }
    return que;
}

void insert_queue(queue *que, dcll *data){
    if(data==NULL) return;
    queue_node *node = init_queue_node(data);
    if(que->front==que->rear && que->front==NULL){
        que->front = que->rear = node;
    }else{
        node->prev = que->rear;
        que->rear->next = node;
        que->rear = node;
    }
}

void delete_rear(queue *que){
    if(que->rear!=NULL){
        que->rear = que->rear->prev;
        if(que->rear) que->rear->next = NULL;
        else que->rear = que->front = NULL;
    }
}

void delete_front(queue *que){
    if(que->front!=NULL){
        que->front = que->front->next;
        if(que->front) que->front->prev = NULL;
        else que->front = que->rear = NULL;
    }
}

void print_queue(queue *que){
    if(que){
        queue_node *cur = que->front;
        while(cur){
            print_dll_forward(cur->head);
            cur = cur->next;
        }
    }
    printf("\n");
}

void print_tree_alternate(queue *que){
    while(que->front!=NULL){
        print_dll_back(que->front->head);
        delete_front(que);
        if(que->rear){
            print_dll_forward(que->rear->head);
            delete_rear(que);
        }
    }
    printf("\n");
}

void print_spiral(tree_node *root){
    queue *que = init_queue();
    insert_queue(que, insert_dcll_node(NULL, root));
    queue_node *cur = que->front;
    while(cur){
        dcll *newL = NULL;
        dcll *temp = cur->head;
        dcll *last = temp->prev;
        while(temp!=last){
            newL = insert_dcll_node(newL, temp->data->left);
            newL = insert_dcll_node(newL, temp->data->right);
            temp = temp->next;
        }
        newL = insert_dcll_node(newL, temp->data->left);
        newL = insert_dcll_node(newL, temp->data->right);
        insert_queue(que, newL);
        cur = cur->next;
    }
    print_queue(que);
    print_tree_alternate(que);
}

int main(){
    int ip[] = {100,50,170,25,60,150,190,20,30,55,65,130,160,185,200};
    int length = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root, ip[i]);
    }
    print_tree(root);
    printf("\n");
    print_spiral(root);

    return 0;
}