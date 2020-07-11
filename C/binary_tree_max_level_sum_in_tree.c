// https://www.geeksforgeeks.org/find-level-maximum-sum-binary-tree/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct node{
    int data;
    struct node *left, *right;
}my_node;

my_node* make_node(int data){
    my_node *nw = (my_node*)malloc(sizeof(my_node));
    if(nw){
        nw->data = data;
        nw->left = nw->right = NULL;
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

typedef struct{
    my_node **data;
    int front, rear;
    int max_size;
}que;

que* init_que(int max_size){
    que *q = (que*)malloc(sizeof(que));
    if(q){
        q->data = (my_node**)calloc(max_size,sizeof(my_node*));
        q->front = q->rear = -1;
        q->max_size = max_size;
    }
    return q;
}

int is_empty(que *q){
    if(q->front==-1) return 1;
    return 0;
}

int is_full(que *q){
    if((q->front==0 && q->rear==q->max_size-1) || (q->rear==q->front-1)) return 1;
    return 0;
}

void insert_que(que *q, my_node *data){
    if(is_full(q)){
        printf("Full\n");
    }else if(data){
        if(q->rear==q->max_size-1) q->rear = 0;
        else q->rear++;
        if(q->front==-1) q->front = 0;
        q->data[q->rear] = data;
    }
}

my_node* delete_que(que *q){
    if(is_empty(q)){
        printf("Empty\n");
        return NULL;
    }
    my_node *temp = q->data[q->front];
    if(q->rear==q->front) q->rear = q->front = -1;
    else if(q->front==q->max_size-1) q->front = 0;
    else q->front++;
    return temp;
}

int find_level_with_max_sum(my_node *root){
    int max_sum = INT_MIN;
    int max_sum_level = -1;
    que *q = init_que(20);
    my_node *null_node = make_node(INT_MIN);
    insert_que(q,root);
    insert_que(q,null_node);
    int t_level = 0;
    while(!is_empty(q) && q->data[q->front]!=null_node){
        int t_sum = 0;
        while(!is_empty(q) && q->data[q->front]!=null_node){
            my_node *temp = delete_que(q);
            t_sum+=temp->data;
            insert_que(q,temp->left);
            insert_que(q,temp->right);
        }
        delete_que(q);
        insert_que(q,null_node);
        if(t_sum>max_sum){
            max_sum = t_sum;
            max_sum_level = t_level;
        }
        t_level++;
    }
    printf("Max Sum = %d at level = %d\n",max_sum,max_sum_level);
    return max_sum;
}

int main(){
    int ip[] = {100,50,10,75,70,73,72,74,78,76,77,150,105,140,130,120,145,142,155};
    int length = sizeof(ip)/sizeof(ip[0]);

    // my_node *root = NULL;
    // int i = 0;
    // for(;i<length;i++){
    //     root = make_tree(root,ip[i]);
    // }

    struct node *root = make_node(1); 
    root->left        = make_node(2); 
    root->right       = make_node(3); 
    root->left->left  = make_node(4); 
    root->left->right = make_node(5); 
    root->right->right = make_node(8); 
    root->right->right->left  = make_node(6); 
    root->right->right->right  = make_node(7); 

    pre(root);
    printf("\n");

    find_level_with_max_sum(root);

    return 0;
}