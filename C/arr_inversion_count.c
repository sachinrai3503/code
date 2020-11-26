// https://leetcode.com/problems/count-of-smaller-numbers-after-self/
/*
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller 
elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Constraints:
0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
*/

#include <stdio.h>
#include <malloc.h>

void print_arr(int *ip, int length){
    int i =0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* init_seq_arr(int length){
    int *op = (int*)calloc(length,sizeof(int));
    int k = 1;
    int i = length-1;
    for(;i>=0;i--){
        op[i] = k++;
    }
    return op;
}

typedef struct {
    int *ip;
    int *index;
    int current_size, max_size;
}heap;

heap* init_heap(int *ip, int *index, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->ip = ip;
        _heap->index = index;
        _heap->current_size = length;
        _heap->max_size = length;
    }
    return _heap;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int compare(int ip1, int ip2, int index1, int index2){
    if(ip1<ip2) return -1;
    else if(ip1>ip2) return 1;
    else if(ip1==ip2 && index1>index2) return -1;
    else if(ip1==ip2 && index1<index2) return 1;
    else return 0;
    
}

void min_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<_heap->current_size && 
       compare(_heap->ip[min_index], _heap->ip[left], 
               _heap->index[min_index], _heap->index[left])==1){
        min_index = left;
    }
    if(right<_heap->current_size &&
       compare(_heap->ip[min_index], _heap->ip[right],
               _heap->index[min_index], _heap->index[right])==1){
        min_index = right;
    }
    if(min_index!=index){
        swap(_heap->ip+min_index, _heap->ip+index);
        swap(_heap->index+min_index, _heap->index+index);
        min_heapify(_heap, min_index);
    }
}

heap* build_heap(int *ip, int *index, int length){
    heap *_heap = init_heap(ip, index, length);
    int parent_index = (_heap->current_size-2)/2;
    for(;parent_index>0;parent_index--){
        min_heapify(_heap, parent_index);
    }
    if(parent_index==0){
        min_heapify(_heap, parent_index);
    }
    return _heap;
}

void heap_sort(int *ip, int *index, int length){
    heap *_heap = build_heap(ip, index, length);
    while(_heap->current_size>1){
        swap(_heap->ip,_heap->ip+(--_heap->current_size));
        swap(_heap->index,_heap->index+(_heap->current_size));
        min_heapify(_heap, 0);
    }
}

void bit_update(int *bit, int length, int index, int value){
    int i = index;
    for(;i<length;i=i+(i&-i)){
        bit[i]+=value;
    }
}

int bit_query(int *bit, int length, int index){
    int count = 0;
    for(;index>0;index = index - (index&-index))
        count+=bit[index];
    return count;
}

int* count_inversion(int *ip, int length){
    int *op_index = init_seq_arr(length);
    heap_sort(ip,op_index,length);
    // print_arr(ip,length);
    // print_arr(op_index,length);
    int *bit = (int*)calloc(length+1, sizeof(int));
    int bit_len = length+1;
    int *count = (int*)calloc(length, sizeof(int));
    int i = length-1;
    for(;i>=0;i--){
        count[length-op_index[i]] = bit_query(bit, bit_len, op_index[i]-1);
        bit_update(bit, bit_len, op_index[i], 1);
        // print_arr(bit, bit_len);
    }
    // print_arr(count, length);
    return count;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSmaller(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    return count_inversion(nums, numsSize);
}