#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

// https://www.geeksforgeeks.org/merge-two-sorted-arrays/
/*
Given two sorted arrays, the task is to merge them in a sorted manner.

Examples:

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8}
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
Output: arr3[] = {4, 5, 7, 8, 8, 9}
*/
// Time complexity - O(n+m), Space complexity - O(m+n)
int* merge_2_sorted_arr1(int *ip1, int len1, int *ip2, int len2){
    int *op = (int*)calloc(len1+len2, sizeof(int));
    int k = 0;
    int i = 0, j = 0;
    while(i<len1 && j<len2){
        if(ip1[i]<ip2[j]){
            op[k++] = ip1[i++];
        }else{
            op[k++] = ip2[j++];
        }
    }
    while(i<len1){
        op[k++] = ip1[i++];
    }
    while(j<len2){
        op[k++] = ip2[j++];
    }
    return op;
}

// https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/
/*
We are given two sorted array. We need to merge these two arrays such that the 
initial numbers (after complete sorting) are in the first array and the 
remaining numbers are in the second array. Extra space allowed in O(1).

Example:

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20} 
*/
// Note - Here no extra splace is allowed.
// Time - O(m*n)
void merge_2_sorted_arr_no_extra_space(int *ip1, int len1, int *ip2, int len2){
    if(len1<=0 || len2<=0) return;
    int i = len2-1;
    for(;i>=0;i--){
        int last = ip1[len1-1];
        int j = len1-2;
        while(j>=0 && ip1[j]>ip2[i]){
            ip1[j+1] = ip1[j];
            j--;
        }
        if(j!=len1-2 || last>ip2[i]){
            ip1[j+1] = ip2[i];
            ip2[i] = last;
        }
    }
}

typedef struct{
    int *data;
    int current_size, max_size;
}heap;

heap* init_heap(int *ip, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = ip;
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
        swap(_heap->data+min_index, _heap->data+index);
        min_heapify(_heap, min_index);
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
        swap(_heap->data+max_index, _heap->data+index);
        max_heapify(_heap, max_index);
    }
}

heap* build_max_heap(int *ip, int length){
    heap *_heap = init_heap(ip,length);
    int parent_index = (_heap->current_size-2)/2;
    for(;parent_index>=0;parent_index-=1){
        max_heapify(_heap, parent_index);
    }
    return _heap;
}

void heap_sort(int *ip, int length){
    heap *_heap = build_max_heap(ip,length);
    while(_heap->current_size>1){
        swap(_heap->data,_heap->data+(--_heap->current_size));
        max_heapify(_heap, 0);
    }
}

// https://www.geeksforgeeks.org/merge-two-sorted-arrays-in-o1-extra-space-using-heap/
// Below code uses heap to sort the arr in constant space.
// Time - (n+m)O(log(m))
void merge_2_sorted_arr_no_extra_space_heap(int *ip1, int len1, 
                                                 int *ip2, int len2){
    if(len1<=0 || len2<=0) return;
    heap *min_heap = init_heap(ip2, len2);
    int i = 0;
    for(;i<len1;i++){
        if(ip1[i]>ip2[0]){
            swap(ip1+i, ip2);
            min_heapify(min_heap, 0);
        }
    }
    heap_sort(ip2, len2);
}

// https://www.geeksforgeeks.org/merge-two-sorted-arrays-in-o1-extra-space-using-quicksort-partition/
// Merge two sorted arrays in O(1) extra space using QuickSort partition
void merge_2_sorted_arr_no_extra_space_quick_sort_partition(int *ip1, int len1, 
                                                            int *ip2, int len2){
    if(len1<=0 || len2<=0) return;
    int N = len1;
    int i = 0, j = 0;
    int count = 0;
    while(count<N){
        if(j==len2 || ip1[i]<ip2[j]) i++;
        else j++;
        count++;
    }
    int _n_plus_1_ele = INT_MIN;
    if(i==len1) _n_plus_1_ele = ip2[j];
    else if(j==len2) _n_plus_1_ele = ip1[i];
    else _n_plus_1_ele = (ip1[i]<ip2[j])?ip1[i]:ip2[j];
    printf("N+1 element=%d, i=%d j=%d len1=%d len2=%d\n",_n_plus_1_ele,i,j,len1, len2);
    int k = 0;
    for(;k<j;k++){
        swap(ip1+i,ip2+k);
        i++;
    }
    heap_sort(ip1,len1);
    heap_sort(ip2,len2);
}

int main(){
    int ip1[] = {1, 5, 9 };
    int ip2[] = {2,4,7,10};
    int len1 = sizeof(ip1)/sizeof(ip1[0]);
    int len2 = sizeof(ip2)/sizeof(ip2[0]);

    printf("ip1>");
    print_arr(ip1,len1);
    printf("ip2>");
    print_arr(ip2,len2);

    // int *op = merge_2_sorted_arr1(ip1,len1,ip2,len2);
    // printf("op>");
    // print_arr(op,len1+len2);
    
    // merge_2_sorted_arr_no_extra_space(ip1, len1, ip2, len2);
    // merge_2_sorted_arr_no_extra_space_heap(ip1, len1, ip2, len2);
    merge_2_sorted_arr_no_extra_space_quick_sort_partition(ip1,len1,ip2,len2);
    printf("op>>");
    print_arr(ip1,len1);
    print_arr(ip2,len2);
    

    return 0;
}