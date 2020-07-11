// https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
/*
Given an array and an integer K, find the maximum for each and every contiguous 
    subarray of size k.

Examples :

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_int_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct  
{
    int *data;
    int front, rear;
    int max_size;
}queue;

queue* init_queue(int max_size){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->data = (int*)calloc(max_size,sizeof(int));
        que->front = que->rear = -1;
        que->max_size = max_size;
    }
    return que;
}

int is_empty(queue *que){
    if(que->front==-1) return 1;
    return 0;
}

int is_full(queue *que){
    if((que->front==0 && que->rear==que->max_size-1) || (que->rear==que->front-1)) return 1;
    return 0;
}

void insert_queue(queue *que, int data){
    if(is_full(que)){
        printf("Full\n");
    }else{
        if(que->rear==que->max_size-1) que->rear = 0;
        else que->rear++;
        if(que->front==-1) que->front = 0;
        que->data[que->rear] = data;
    }
}

int delete_rear(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = que->data[que->rear];
        if(que->rear==que->front) que->rear = que->front = -1;
        else if(que->rear==0) que->rear = que->max_size-1;
        else que->rear--;
        return temp;
    }
}

int delete_front(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = que->data[que->front];
        if(que->rear==que->front) que->rear = que->front = -1;
        else if(que->front==que->max_size-1) que->front = 0;
        else que->front++;
        return temp;
    }
}

int* get_max_of_all_subarr_of_size_k(int ip[], int length, int k){
    if(k<=0){
        printf("Invalid\n");
        return NULL;
    }
    int *op = (int*)calloc(length-k+1,sizeof(int));
    int j = 0;
    queue *que = init_queue(length);
    int i = 0;
    for(;i<length;i++){
        while(!is_empty(que) && ip[que->data[que->rear]]<=ip[i]){
            delete_rear(que);
        }
        insert_queue(que,i);
        if(i>=k-1){
            op[j++] = ip[que->data[que->front]];
            if(que->data[que->front]<=i+1-k)
                delete_front(que);
        }
    }
    return op;
}

int main(){
    int ip[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_int_arr(ip,length);
    int k = 1;
    for(;k<=length+1;k++){
        printf("k = %d =>",k);
        print_int_arr(get_max_of_all_subarr_of_size_k(ip,length,k),length-k+1);
    }

    return 0;
}