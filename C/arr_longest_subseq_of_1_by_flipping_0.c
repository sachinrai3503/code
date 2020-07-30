// https://www.geeksforgeeks.org/longest-subsegment-1s-formed-changing-k-0s/
// https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/

/*
Given a binary array and an integer m, find the position of zeroes flipping
 which creates maximum number of consecutive 1’s in array.

Examples :

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 2
Output:  5 7

Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
         m = 1
Output:  7

Input:   arr[] = {0, 0, 0, 1}
         m = 4
Output:  0 1 2
*/

// Python version of code - list_longest_subseq_of_1_by_flipping_0.py

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct {
    int *data;
    int front, rear;
    int max_size;
}que;

que* init_que(int max_size){
    que *q = (que*)malloc(sizeof(que));
    if(q){
        q->data = (int*)calloc(max_size,sizeof(int));
        q->front = q->rear = -1;
        q->max_size = max_size;
    }
    return q;
}

int is_full(que *q){
    if((q->front==0 && q->rear==q->max_size-1) || (q->rear==q->front-1)) 
        return 1;
    return 0;
}

int is_empty(que *q){
    if(q->front==-1) return 1;
    return 0;
}

void insert_que(que *q, int data){
    if(is_full(q)){
        printf("Full\n");
    }else{
        if(q->rear==q->max_size-1) q->rear = 0;
        else q->rear++;
        if(q->front==-1) q->front = 0;
        q->data[q->rear] = data;
    }
}

int delete_que(que *q){
    if(is_empty(q)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = q->data[q->front];
        if(q->front==q->rear) q->rear = q->front = -1;
        else if(q->front==q->max_size-1) q->front = 0;
        else q->front++;
        return temp;
    }
}

int copy_que_to_arr(que *q, int *op, int m){
    int k = 0;
    int i = q->front;
    if(i>q->rear){
        while(i<q->max_size && k<m){
            op[k++] = q->data[i++];
        }
        i = 0;
    }
    while(i!=-1 && i<=q->rear && k<m){
        op[k++] = q->data[i++];
    }
    return k-1;
}


int* get_0_to_flip(int *ip, int length, int m, int *index){
    que *q = init_que(m+1);
    int s = 0, e = -1;
    int *op = (int*)calloc(m,sizeof(int));
    int zero_count = 0;
    int ts = 0;
    int i = 0;
    for(;i<length;i++){
        if(ip[i]==0){
            insert_que(q,i);
            zero_count++;
        }
        if(zero_count>m){
            if((i-ts)>(e-s+1)){
                e = i-1;
                s = ts;
                *index = copy_que_to_arr(q,op,m);
            }
            ts = delete_que(q) + 1;
            zero_count--;
        }
    }
    if((i-ts)>(e-s+1)){
        e = i-1;
        s = ts;
        *index = copy_que_to_arr(q,op,m);
    }
    printf("Start=%d end=%d count=%d >>",s,e,(e-s+1));
    return op;
}

int main(){
    int ip[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);

    int m = 0;
    for(;m<=length+1;m++){
        int index = -1;
        printf("M=%d>>",m);
        int *op = get_0_to_flip(ip,length,m,&index);
        print_arr(op,index+1);
    }

    return 0;   
}