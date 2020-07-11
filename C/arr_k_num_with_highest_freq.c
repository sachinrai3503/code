// https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/
// https://www.geeksforgeeks.org/find-k-most-frequent-in-linear-time/
/*
Given an array of n numbers and a positive integer k. 
The problem is to find k numbers with most occurrences, i.e.,
 the top k numbers having the maximum frequency. 

If two numbers have the same frequency then the larger
 number should be given preference. 

The numbers should be displayed in decreasing order of their frequencies.
It is assumed that the array consists of k numbers with most occurrences.

Examples:
Input: 
arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, 
k = 2
Output: 4 1
Input : 
arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
k = 4
Output: 5 11 7 10
*/

// Below is heap based solution
// For linear time see python <>

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

typedef struct{
    int data;
    int freq;
    int index; // index of element in heap
}heap_data;

typedef struct{
    heap_data **data;
    int current_size, max_size;
}heap;

heap_data* init_heap_data(int data, int freq){
    heap_data *_heap_data = (heap_data*)malloc(sizeof(heap_data));
    if(_heap_data){
        _heap_data->data = data;
        _heap_data->freq = freq;
        _heap_data->index = -1;
    }
    return _heap_data;
}

heap* init_heap(int max_size){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = (heap_data**)calloc(max_size,sizeof(heap_data*));
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

void swap(heap_data **a, heap_data **b){
    heap_data *temp = *b;
    *b = *a;
    *a = temp;
    int t_index = (*b)->index;
    (*b)->index = (*a)->index;
    (*a)->index = t_index;
}

void print_heap(heap *_heap){
    int i = 0;
    for(;i<_heap->current_size;i++){
        printf("%d %d %d <>",_heap->data[i]->data,_heap->data[i]->freq,
                _heap->data[i]->index);
    }
    printf("\n");
}

/*
    Returns 0 if both are equal.
    Returns -1 if data1 is greater else 1;
*/
int compare(heap_data *data1, heap_data *data2){
    if(data1->freq>data2->freq) return -1;
    if(data1->freq<data2->freq) return 1;
    if(data1->data>data2->data) return -1;
    if(data1->data<data2->data) return 1;
    return 0;
}

void max_heapify(heap *_heap, int index){
    int left_index = index*2+1;
    int right_index = index*2+2;
    int max_index = index;
    if(left_index<_heap->current_size && 
        compare(_heap->data[max_index],_heap->data[left_index])==1){
            max_index = left_index;
    }
    if(right_index<_heap->current_size && 
        compare(_heap->data[max_index],_heap->data[right_index])==1){
        max_index = right_index;
    }
    if(max_index!=index){
        swap(_heap->data+max_index,_heap->data+index);
        max_heapify(_heap,max_index);
    }
}

void insert_heap(heap *_heap, heap_data *data){
    if(is_full(_heap)){
        printf("Full\n");
        return;
    }else if(data){
        data->index = _heap->current_size;
        _heap->data[_heap->current_size++] = data;
        int parent_index = (_heap->current_size-2)/2;
        for(;parent_index>0;parent_index=(parent_index-1)/2){
            max_heapify(_heap,parent_index);
        }
        if(parent_index==0){
            max_heapify(_heap,parent_index);
        }
    }
}

heap_data* delete_top(heap *_heap){
    if(is_empty(_heap)){
        printf("Empty\n");
        return NULL;
    }else{
        heap_data *temp = _heap->data[0];
        swap(_heap->data,_heap->data+(--_heap->current_size));
        max_heapify(_heap,0);
        return temp;
    }
}

void rearrange_node(heap *_heap, int index){
    if(is_empty(_heap)){
        printf("Empty\n");
        return;
    }else if(index>0 && index<_heap->current_size){
        while(index>0){
            int parent_index = (index-1)/2;
            if(compare(_heap->data[index],_heap->data[parent_index])==-1){
                swap(_heap->data+index,_heap->data+parent_index);
            }else{
                return;
            }
            index = parent_index;
        }
    }
}

void print_k_most_frequent_element(int ip[], int length, int k){
    heap *_heap = init_heap(length);
    heap_data **hash = (heap_data**)calloc(1000,sizeof(heap_data*));
    int i = 0;
    for(;i<length;i++){
        if(hash[ip[i]]==NULL){
            hash[ip[i]] = init_heap_data(ip[i],1);
            insert_heap(_heap,hash[ip[i]]);
        }else{
            hash[ip[i]]->freq++;
            rearrange_node(_heap,hash[ip[i]]->index);
        }
        // print_heap(_heap);
    }
    for(i=0;i<k && is_empty(_heap)==0;i++){
        heap_data *temp = delete_top(_heap);
        printf("(%d-%d) ",temp->data,temp->freq);
    }
}

int main(){
    int ip[] = {3, 1, 4, 4, 5, 2, 6, 1};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    int k = 0;
    for(;k<=length+1;k++){
        printf("K=%d ",k);
        print_k_most_frequent_element(ip,length,k);
        printf("\n");
    }

    return 0;
}