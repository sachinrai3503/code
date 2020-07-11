// https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/
/*
Given an unsorted array and two numbers x and k, find k closest values to x.

Examples:

Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 
Output : 4 6 7
Three closest values of x are 4, 6 and 7.

Input : arr[] = {-10, -50, 20, 17, 80}, x = 20, k = 2
Output : 17, 20 
*/
#include <stdio.h>
#include <malloc.h>
#include <limits.h>

int get_diff(int a, int b){
    if(a>b) return a-b;
    return b-a;
}

typedef struct{
    int num,diff;
}heap_node;

heap_node* make_node(int num, int diff){
    heap_node *node = (heap_node*)malloc(sizeof(heap_node));
    if(node){
        node->num = num;
        node->diff = diff;
    }
    return node;
}

typedef struct{
    heap_node **data;
    int current_size, max_size;
}heap;

heap* init_heap(int max_size){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = (heap_node**)calloc(max_size,sizeof(heap_node*));
        _heap->current_size = 0;
        _heap->max_size = max_size;
    }
    return _heap;
}

void swap(heap_node **a, heap_node **b){
    heap_node *temp = *a;
    *a = *b;
    *b = temp;
}

void max_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int max_index = index;
    if(left<_heap->current_size && _heap->data[left]->diff>_heap->data[max_index]->diff){
        max_index = left;
    }
    if(right<_heap->current_size && _heap->data[right]->diff>_heap->data[max_index]->diff){
        max_index = right;
    }
    if(max_index!=index){
        swap(_heap->data+max_index,_heap->data+index);
        max_heapify(_heap,max_index);
    }
}

int is_empty(heap *_heap){
    if(_heap->current_size==0) return 1;
    return 0;
}

int is_full(heap *_heap){
    if(_heap->current_size==_heap->max_size) return 1;
    return 0;
}

void insert_heap(heap *_heap, heap_node *data){
    if(is_full(_heap)){
        printf("Full\n");
    }else if(data){
        _heap->data[_heap->current_size++] = data;
        int parent_index = (_heap->current_size-2)/2;
        for(;parent_index>0;parent_index = (parent_index-1)/2){
            max_heapify(_heap,parent_index);
        }
        if(parent_index==0){
            max_heapify(_heap,parent_index);
        }
    }
}

heap_node* delete_top(heap *_heap){
    if(is_empty(_heap)){
        printf("Empty\n");
        return NULL;
    }else{
        heap_node *temp = _heap->data[0];
        _heap->data[0] = _heap->data[--_heap->current_size];
        max_heapify(_heap,0);
        return temp;
    }
}

void print_heap(heap *_heap){
    int i = 0;
    for(;_heap && i<_heap->current_size;i++){
        printf("%d ",_heap->data[i]->num);
    }
    printf("\n");
}

heap* find_k_closest_numbers(int ip[], int length, int num, int k){
    if(length<=0 || k<=0) return NULL;
    heap *_heap = init_heap(k);
    int i = 0;
    for(;i<length;i++){
        if(i<k){
            insert_heap(_heap,make_node(ip[i], get_diff(ip[i],num)));
        }else{
            int diff = get_diff(ip[i],num);
            if(diff<_heap->data[0]->diff){
                delete_top(_heap);
                insert_heap(_heap,make_node(ip[i],get_diff(ip[i],num)));
            }
        }
    }
    return _heap;
}

int main(){
    int ip[] = {-10, -50, 20, 17, 8};
    int length = sizeof(ip)/sizeof(ip[0]);
    int num = 20;
    int k = 2;
    heap *_heap = find_k_closest_numbers(ip,length,num,k);
    print_heap(_heap);
    return 0;
}