// https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/
// https://leetcode.com/problems/relative-sort-array/

/*
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order 
among the elements will be same as those are in A2. For the elements not 
present in A2, append them at last in sorted order. 
Example: 

Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
       A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

The code should handle all cases like the number of elements in A2[] may
be more or less compared to A1[]. A2[] may have some elements which may not
 be there in A1[] and vice versa is also possible.
*/

// Here the approch uses custom compare using hash and heap sort for sorting.
// So, time complexity = O(nlog(n)) + O(m) where n, m size of arr1, arr2.

// We can also reduce it to O(n+m) + O(plog(p)) by moving all arr1 element as key 
// in map with count as value. Then, traverse each element in arr2 &
//  delete the element from map & copy the element to result count times. 
// Sort remaining 'p' element in map & add to result.

#include <limits.h>
#include <stdio.h>
#include <malloc.h>

#define true 1
#define false 0
typedef int bool;

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void init_arr(int *ip, int length, int value){
    int i = 0;
    for(;i<length;i++){
        ip[i] = value;
    }
}

typedef struct{
    int *data;
}hash_map;

hash_map* init_map(){
    hash_map *map = (hash_map*)malloc(sizeof(hash_map));
    if(map){
        map->data = (int*)calloc(1001,sizeof(int));
        init_arr(map->data,1001,INT_MAX);
    }
    return map;
}

void insert_in_map(hash_map *map, int key, int value){
    if(map){
        map->data[key] = value;
    }
}

bool is_present(hash_map *map, int num){
    if(map && map->data[num]!=INT_MAX){
        return true;
    }
    return false;
}

int get_value(hash_map *map, int key){
    if(is_present(map, key)){
        return map->data[key];
    }
    return INT_MAX;
}

//  If(a>b) returns -1, if(a<b) returns 1, if(a==b) return 0
int compare(hash_map *map, int a, int b){
    int ai = get_value(map, a);
    int bi = get_value(map, b);
    if(ai!=INT_MAX && bi!=INT_MAX){
        if(ai<bi) return 1;
        else if(ai>bi) return -1;
        return 0;
    }else if(ai!=INT_MAX) return 1;
    else if(bi!=INT_MAX) return -1;
    else if(a>b) return -1;
    else if(a<b) return 1;
    return 0;
}

typedef struct {
    int *data;
    int current_size, max_size;
}heap;

heap* init_heap(int *data, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = data;
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

void max_heapify(hash_map *map, heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int max_index = index;
    if(left<_heap->current_size && 
        compare(map, _heap->data[max_index], _heap->data[left])==1){
        max_index = left;
    }
    if(right<_heap->current_size && 
        compare(map, _heap->data[max_index], _heap->data[right])==1){
        max_index = right;
    }
    if(max_index!=index){
        swap(_heap->data+index, _heap->data+max_index);
        max_heapify(map, _heap, max_index);
    }
}

void build_heap(hash_map *map, heap *_heap){
    int parent_index = (_heap->current_size-2)/2;
    for(;parent_index>=0;parent_index--){
        max_heapify(map, _heap, parent_index);
    }
}

void heap_sort(hash_map *map, int ip[], int length){
    heap *_heap = init_heap(ip,length);
    build_heap(map, _heap);
    // print_arr(_heap->data, _heap->current_size);
    while(_heap->current_size>1){
        swap(_heap->data,_heap->data + (--_heap->current_size));
        max_heapify(map, _heap, 0);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* relativeSortArray(int* arr1, int arr1Size, 
                       int* arr2, int arr2Size, int* returnSize){
    hash_map *map = init_map();
    int i = 0;
    for(;i<arr2Size;i++){
        insert_in_map(map, arr2[i], i);
    }
    heap_sort(map, arr1, arr1Size);
    *returnSize = arr1Size;
    return arr1;
}

int main(){
    int arr1[] = { 2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5};
    int arr2[] = {2, 1, 8, 3, 4};
    int arr1_len = sizeof(arr1)/sizeof(arr1[0]);
    int arr2_len = sizeof(arr2)/sizeof(arr2[0]);

    printf("arr1>");print_arr(arr1, arr1_len);
    printf("arr2>");print_arr(arr2, arr2_len);

    int op_len = 0;
    int *op = relativeSortArray(arr1, arr1_len, arr2, arr2_len, &op_len);
    printf("op>");print_arr(op, op_len);

    return 0;
}