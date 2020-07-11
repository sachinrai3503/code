// https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
/*
Given an infinite stream of integers, find the k’th largest element at any point of time.
Example:

Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output:    {_,   _, 10, 11, 20, 40, 50,  50, ...}
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

typedef struct{
    int *data;
    int current_size, max_size;
}heap;

heap* init_heap(int max_size){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = (int*)calloc(max_size,sizeof(int));
        _heap->current_size = 0;
        _heap->max_size = max_size;
    }
    return _heap;
}

int is_full(heap *_heap){
    if(_heap->current_size==_heap->max_size) return 1;
    return 0;
}

int is_empty(heap *_heap){
    if(_heap->current_size==0) return 1;
    return 0;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void min_heapify(heap *_heap, int index){
    int left_child = index*2+1;
    int right_child = index*2+2;
    int min_index = index;
    if(left_child<_heap->current_size && _heap->data[left_child]<_heap->data[min_index]){
        min_index = left_child;
    }
    if(right_child<_heap->current_size && _heap->data[right_child]<_heap->data[min_index]){
        min_index = right_child;
    }
    if(min_index!=index){
        swap(_heap->data+index,_heap->data+min_index);
        min_heapify(_heap,min_index);
    }
}

void insert_heap(heap *_heap, int data){
    if(is_full(_heap)){
        printf("Full\n");
    }else{
        _heap->data[_heap->current_size++] = data;
        int parent_index = (_heap->current_size-2)/2;
        for(;parent_index>0;parent_index=(parent_index-1)/2){
            min_heapify(_heap,parent_index);
        }
        if(parent_index==0){
            min_heapify(_heap,parent_index);
        }
    }
}

int delete_heaptop(heap *_heap){
    if(is_empty(_heap)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = _heap->data[0];
        _heap->data[0] = _heap->data[--_heap->current_size];
        min_heapify(_heap,0);
        return temp;
    }
}

void print_k_largest_in_stream(int ip[], int length, int k){
    if(k<=0){
        printf("Invalid K\n");
        return;
    }
    heap *_heap = init_heap(k);
    int i = 0;
    for(;i<length;i++){
        if(is_full(_heap)){
            if(ip[i]>_heap->data[0]){
                delete_heaptop(_heap);
                insert_heap(_heap,ip[i]);
            }
        }else{
            insert_heap(_heap,ip[i]);
        }
        if(i>=k-1){
            printf("%d ",_heap->data[0]);
        }
    }
    printf("\n");
}

int main(){
    int ip[] = {10, 20, 11, 70, 50, 40, 100, 5};
    int length = sizeof(ip)/sizeof(ip[0]);
    
    print_int_arr(ip,length);
    int k = 1;
    for(;k<=length+1;k++){
        printf("k=%d >",k);
        print_k_largest_in_stream(ip,length,k);
    }

    return 0;
}