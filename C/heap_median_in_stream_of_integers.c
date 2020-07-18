// https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
/*
Median in a stream of integers (running integers)

Given that integers are read from a data stream. Find median of elements 
read so for in efficient way. For simplicity assume there are no duplicates.

For example, let us consider the stream 5, 15, 1, 3 …

After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

When the input size is odd, we take the middle element of sorted data.
If even, we pick average of middle two elements in sorted stream.
*/

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

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void min_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<_heap->current_size && _heap->data[min_index]>_heap->data[left]){
        min_index = left;
    }
    if(right<_heap->current_size && _heap->data[min_index]>_heap->data[right]){
        min_index = right;
    }
    if(min_index!=index){
        swap(_heap->data+min_index,_heap->data+index);
        min_heapify(_heap,min_index);
    }
}

void max_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int max_index = index;
    if(left<_heap->current_size && _heap->data[max_index]<_heap->data[left]){
        max_index = left;
    }
    if(right<_heap->current_size && _heap->data[max_index]<_heap->data[right]){
        max_index = right;
    }
    if(max_index!=index){
        swap(_heap->data+max_index,_heap->data+index);
        min_heapify(_heap,max_index);
    }
}

void insert_min_heap(heap *_heap, int data){
    if(_heap->current_size==_heap->max_size){
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

void insert_max_heap(heap *_heap, int data){
    if(_heap->current_size==_heap->max_size){
        printf("Full\n");
    }else{
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

int delete_top_min_heap(heap *_heap){
    if(_heap->current_size==0){
        printf("Empty heap\n");
        return INT_MIN;
    }else{
        int temp = _heap->data[0];
        _heap->data[0] = _heap->data[--_heap->current_size];
        min_heapify(_heap,0);
        return temp;
    }
}

int delete_top_max_heap(heap *_heap){
    if(_heap->current_size==0){
        printf("Empty heap\n");
        return INT_MIN;
    }else{
        int temp = _heap->data[0];
        _heap->data[0] = _heap->data[--_heap->current_size];
        max_heapify(_heap,0);
        return temp;
    }
}

int evaluate_median(heap *min_heap, heap *max_heap){
    if(min_heap->current_size==max_heap->current_size){
        return (min_heap->data[0]+max_heap->data[0])/2;
    }else if(min_heap->current_size>max_heap->current_size){
        return min_heap->data[0];
    }else{
        return max_heap->data[0];
    }
}

void check_and_insert(heap *max_heap, heap *min_heap, int data, int heap_flag){
    if(heap_flag==0){
        if(min_heap->current_size>max_heap->current_size){
            insert_max_heap(max_heap,delete_top_min_heap(min_heap));
        }
        insert_min_heap(min_heap,data);
    }else{
        if(max_heap->current_size>min_heap->current_size){
            insert_min_heap(min_heap,delete_top_max_heap(max_heap));
        }
        insert_max_heap(max_heap,data);
    }
}

void print_median(int ip[], int length){
    heap *max_heap = init_heap((length/2)+1);
    heap *min_heap = init_heap((length/2)+1);
    int median = INT_MIN;
    int i = 0;
    for(;i<length;i++){
        if(ip[i]>median){
            check_and_insert(max_heap,min_heap,ip[i],0);
        }else{
            check_and_insert(max_heap,min_heap,ip[i],1);
        }
        median = evaluate_median(min_heap,max_heap);
        // print_arr(max_heap->data,max_heap->current_size);
        // print_arr(min_heap->data,min_heap->current_size);
        printf("%d ",median);
    }
}

int main(){
    int ip[] = {5,15,1,3,2,8,7,9,10,6,11,4};
    int length = sizeof(ip)/sizeof(ip[0]);
    print_arr(ip,length);
    print_median(ip,length);
}