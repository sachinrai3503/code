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

typedef struct {
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

int is_empty(que *q){
    if(q->front==-1) return 1;
    return 0;
}

int is_full(que *q){
    if((q->front==0 && q->rear==q->max_size-1) || (q->front==q->rear+1)) return 1;
    return 0;
}

void insert_que(que *q, tree_node *data){
    if(is_full(q)){
        printf("Full\n");
    }else if(data){
        if(q->rear==q->max_size-1) q->rear=0;
        else q->rear++;
        if(q->front==-1) q->front = 0;
        q->data[q->rear] = data;
    }
}

tree_node* delete_front(que *q){
    if(is_empty(q)){
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

tree_node* delete_rear(que *q){
    if(is_empty(q)){
        printf("Empty\n");
        return NULL;
    }else{
        tree_node *temp = q->data[q->rear];
        if(q->front==q->rear) q->front = q->rear = -1;
        else if(q->rear==0) q->rear = q->max_size-1;
        else q->rear--;
        return temp;
    }
}

void print_que_left_to_right(que *q){
    int i = q->front;
    while(i>q->rear){
        printf("%d ",q->data[i]->data);
        i++;
        if(i==q->max_size){
            i=0;
            break;
        }
    }
    while(i<=q->rear){
        printf("%d ",q->data[i]->data);
        i++;
    }
    printf("\n");
}

void print_que_right_to_left(que *q){
    int i = q->rear;
    while(i<q->front){
        printf("%d ",q->data[i]->data);
        i--;
        if(i==-1){
            i=q->max_size-1;
            break;
        }
    }
    while(i>=q->front){
        printf("%d ",q->data[i]->data);
        i--;
    }
    printf("\n");
}

void print_que_arr(que **arr, int length){
    int i = 0;
    for(;i<length;i++){
        print_que_left_to_right(arr[i]);
    }
}

que** get_level_as_arr_element(tree_node *root, int *level){
    que **arr = (que**)calloc(20,sizeof(que*));
    que *q = init_que(15);
    tree_node *null_node = make_node(INT_MIN);
    insert_que(q,root);
    insert_que(q,null_node);
    while(!is_empty(q) && q->data[q->front]!=null_node){
        que *t_q = init_que(15);
        while(!is_empty(q) && q->data[q->front]!=null_node){
            tree_node *temp = delete_front(q);
            insert_que(q,temp->left);
            insert_que(q,temp->right);
            insert_que(t_q,temp);
        }
        arr[(*level)++] = t_q;
        delete_front(q);
        insert_que(q,null_node);
    }
    return arr;
}

//https://www.geeksforgeeks.org/zigzag-tree-traversal/
/*
Write a function to print ZigZag order traversal of a binary tree.
For the below binary tree the zigzag order traversal will be 1 3 2 7 6 5 4

                1
        2               3
    7       6       5       4

*/
void print_spiral_V1(que **arr, int length){
    int i = 0;
    for(;i<length;i++){
        if(i%2==0) print_que_left_to_right(arr[i]);
        else print_que_right_to_left(arr[i]);
    }
}

//https://www.geeksforgeeks.org/reverse-zigzag-traversal-of-a-binary-tree/?ref=rp
/*
Input:
      5
     / \
    9   3
   /     \
  6       4
 / \
8   7
Output: 7 8 6 4 3 9 5
*/
void print_spiral_V2(que **arr, int length){
    int flag = 0;
    int i = length-1;
    for(;i>=0;i--){
        if(flag==0) print_que_right_to_left(arr[i]);
        else print_que_left_to_right(arr[i]);
        flag = !flag;
    }
}

//https://www.geeksforgeeks.org/reverse-clockwise-spiral-traversal-of-a-binary-tree/?ref=rp
/*
Input :
           20
         /   \
        8     22
      /   \  /   \
     5     3 4    25
          / \
         10  14
Output : 14 10 20 25 4 3 5 8 22
*/
void print_spiral_V3(que **arr, int length){
    int i = 0, j = length-1;
    while(i<j){
        print_que_right_to_left(arr[j]);
        print_que_left_to_right(arr[i]);
        i++;
        j--;
    }
    if(i==j){
        print_que_right_to_left(arr[j]);
    }
}

//https://www.geeksforgeeks.org/reverse-anti-clockwise-spiral-traversal-of-a-binary-tree/?ref=rp
/*
Input :
           20
         /   \
        8     22
      /   \  /   \
     5     3 4    25
          / \
         10  14
Output : 10 14 20 5 3 4 25 22 8
*/
void print_spiral_V4(que **arr, int length){
    int i = 0, j = length-1;
    while(i<j){
        print_que_left_to_right(arr[j]);
        print_que_right_to_left(arr[i]);
        i++;
        j--;
    }
    if(i==j){
        print_que_left_to_right(arr[j]);
    }
}

//https://www.geeksforgeeks.org/vertical-zig-zag-traversal-of-a-tree/?ref=rp
/*
Vertical Zig-Zag traversal of a tree is defined as:

Print the elements of the first level in the order from right to left, 
    if there are no elements left then skip to the next level.
Print the elements of the last level in the order from left to right, 
    if there are no elements left then skip to the previous level.
Repeat the above steps while there are nodes left to traverse.

Input: 
     1
  /     \
 2       3
  \     /  \
  4    5    6
  /          \
 7            8
Output: 1, 7, 3, 8, 2, 4, 6, 5
*/
void print_vertical_zig_zag(que **arr, int length){
    int i = 0, j = length-1;
    int flag = 0;
    while(i<=j){
        if(flag==0){
            tree_node *temp = delete_rear(arr[i]);
            printf("%d ",temp->data);
            if(is_empty(arr[i])) i++;
        }else{
            tree_node *temp = delete_front(arr[j]);
            printf("%d ",temp->data);
            if(is_empty(arr[j])) j--;
        }
        flag=!flag;
    }
    printf("\n");
}

int main(){
    // int ip[] = {100,75,60,50,65,62,80,83,81,90,125,130,135,133,138};
    int ip[] = {100,75,60,50,65,80,83,125,130,135};
    int length  = sizeof(ip)/sizeof(ip[0]);

    tree_node *root = NULL;
    int i = 0;
    for(;i<length;i++){
        root = make_tree(root,ip[i]);
    }
    pre_order(root);
    printf("\n");

    int level = 0;
    que **arr = get_level_as_arr_element(root, &level);
    printf("each level as arr\n");
    print_que_arr(arr,level);
    
    printf("===============V1=====================\n");
    print_spiral_V1(arr,level);
    printf("===============V2=====================\n");
    print_spiral_V2(arr,level);
    printf("============V3========================\n");
    print_spiral_V3(arr,level);
    printf("============V4========================\n");
    print_spiral_V4(arr,level);
    printf("=============Vertical Zig Zag=======================\n");
    print_vertical_zig_zag(arr,level);
    printf("====================================\n");
    return 0;
}