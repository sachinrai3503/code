// https://www.geeksforgeeks.org/lru-cache-implementation/
// LRU Cache Implementation - Counting the page faults.

#include <stdio.h>
#include <limits.h>
#include <malloc.h>

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct node{
    int data;
    struct node *left, *right;
}que_node;

typedef struct{
    que_node *front, *rear;
    int size, max_size;
}que;

que_node* init_node(int data){
    que_node *node = (que_node*)malloc(sizeof(que_node));
    if(node){
        node->data = data;
        node->left = node->right = NULL;
    }
    return node;
}

que* init_que(int max_size){
    que *_que = (que*)malloc(sizeof(que));
    if(_que){
        _que->front = _que->rear = NULL;
        _que->size = 0;
        _que->max_size = max_size;
    }
    return _que;
}

int is_empty(que *_que){
    if(_que->front==NULL) return 1;
    return 0;
}

int is_full(que *_que){
    if(_que->size == _que->max_size) return 1;
    return 0;
}

void insert_at_rear(que *_que, que_node *data){
    if(is_full(_que)){
        printf("Full\n");
        return;
    }else if(data){
        if(is_empty(_que)){
            _que->front = _que->rear = data;
        }else{
            _que->rear->right = data;
            data->left = _que->rear;
            _que->rear = data;
        }
        _que->size++;
    }
}

que_node* delete_front(que *_que){
    if(is_empty(_que)){
        printf("Empty\n");
        return NULL;
    }else{
        que_node *temp = _que->front;
        if(_que->rear==_que->front){
            _que->rear = _que->front = NULL;
        }else{
            _que->front = _que->front->right;
            _que->front->left = NULL;
        }
        _que->size--;
        temp->left = temp->right = NULL;
        return temp;
    }
}

que_node* delete_node(que *_que, que_node *node){
    if(is_empty(_que)){
        printf("Empty\n");
        return NULL;
    }else{
        que_node *temp = node;
        que_node *left = node->left;
        que_node *right = node->right;
        if(left){
            left->right = right;
        }else{
            _que->front = right;
        }
        if(right){
            right->left = left;
        }else{
            _que->rear = left;
        }
        _que->size--;
        temp->left = temp->right = NULL;
        return temp;
    }
}

void print_que(que *_que){
    que_node *temp = _que->front;
    for(;temp;temp=temp->right){
        printf("%d ",temp->data);
    }
    printf("\n");
}

int count_page_fault(int page_arr[], int length, int cache_size){
    que *_que = init_que(cache_size);
    que_node **hash = (que_node**)calloc(1000,sizeof(que_node*));
    int page_fault_count = 0;
    int i = 0;
    for(;i<length;i++){
        if(hash[page_arr[i]]){
            que_node *temp = delete_node(_que,hash[page_arr[i]]);
            insert_at_rear(_que,temp);
        }else{
            if(is_full(_que)){
                que_node *temp = delete_front(_que);
                hash[temp->data] = NULL;
                page_fault_count++;
            }
            que_node *node = init_node(page_arr[i]);
            insert_at_rear(_que,node);
            hash[node->data]  = node;
        }
    }
    return page_fault_count;
}

int main(){
    int ip[] = {1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    int cache_size = 1;
    for(;cache_size<=length+1;cache_size++)
        printf("cache size = %d Count =>%d\n",cache_size,count_page_fault(ip,length,cache_size));

    return 0;
}