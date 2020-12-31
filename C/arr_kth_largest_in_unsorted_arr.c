// https://leetcode.com/problems/kth-largest-element-in-an-array/
// https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
/*
Find the kth largest element in an unsorted array. Note that it is the kth
 largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void printArr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct{
    int *data;
    int curSize, maxSize;
}heap;

heap* initHeap(int *data, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = data;
        _heap->curSize = length;
        _heap->maxSize = length;
    }
    return _heap;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void minHeapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int minIndex = index;
    if(left<_heap->curSize && _heap->data[left]<_heap->data[minIndex]) minIndex = left;
    if(right<_heap->curSize && _heap->data[right]<_heap->data[minIndex]) minIndex = right;
    if(minIndex!=index){
        swap(_heap->data+minIndex, _heap->data+index);
        minHeapify(_heap, minIndex);
    }
}

heap* buildHeap(int *ip, int length){
    heap *_heap = initHeap(ip, length);
    int parentIndex = (_heap->curSize-2)/2;
    for(;parentIndex>=0;parentIndex--){
        minHeapify(_heap, parentIndex);
    }
    return _heap;
}

int findKthLargest(int* nums, int numsSize, int k){
    heap *_heap = buildHeap(nums, k);
    // printArr(_heap->data, _heap->curSize);
    int i = k;
    for(;i<numsSize;i++){
        if(nums[i]>_heap->data[0]){
            _heap->data[0] = nums[i];
            minHeapify(_heap, 0);
        }
    }
    return _heap->data[0];
}