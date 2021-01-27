// https://leetcode.com/problems/merge-k-sorted-lists/
// https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/
// https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
/*
You are given an array of k linked-lists lists, each linked-list is sorted in
 ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
*/

// Below is heap based sol. with time complexity - O(nkLok(k)) and space O(k)
// Better sol. - SLL_merge_K_sorted_list_in_place.c

#include <stdio.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
 };

typedef struct{
    struct ListNode **data;
    int current_size, max_size;
}heap;

heap* init_heap(int max_size){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = (struct ListNode**)calloc(max_size,sizeof(struct ListNode*));
        _heap->current_size = 0;
        _heap->max_size = max_size;
    }
    return _heap;
}

int is_empty(heap *_heap){
    if(_heap->current_size==0) return 1;
    return 0;
}

int is_full(heap *_heap){
    if(_heap->current_size==_heap->max_size) return 1;
    return 0;
}

void swap(struct ListNode **a, struct ListNode **b){
    struct ListNode *temp = *a;
    *a = *b;
    *b = temp;
}

void min_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<_heap->current_size && _heap->data[left]->val<_heap->data[min_index]->val)  min_index = left;
    if(right<_heap->current_size && _heap->data[right]->val<_heap->data[min_index]->val)  min_index = right;
    if(min_index!=index){
        swap(_heap->data+min_index,_heap->data+index);
        min_heapify(_heap,min_index);
    }
}

void insert_heap(heap *_heap, struct ListNode *data){
    if(is_full(_heap)){
        printf("Full\n");
        return;
    }else if(data){
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

struct ListNode* delete_top(heap *_heap){
    if(is_empty(_heap)){
        printf("Empty\n");
        return NULL;
    }else{
        struct ListNode *temp = _heap->data[0];
        _heap->data[0] = _heap->data[--_heap->current_size];
        min_heapify(_heap,0);
        return temp;
    }
}

struct ListNode* mergeKLists(struct ListNode **arr, int k){
    struct ListNode *head = NULL;
    struct ListNode *prev = NULL;
    heap *_heap = init_heap(k);
    int i = 0;
    for(;i<k;i++){
        if(arr[i])
            printf("i=%d %d\n",i,arr[i]->val);
        else printf("i=%d NULL\n",i);
        insert_heap(_heap,arr[i]);
    }
    while(!is_empty(_heap)){
        struct ListNode *temp = delete_top(_heap);
        if(!head){
            head = temp;
        }else{
            prev->next = temp;
        }
        insert_heap(_heap,temp->next);
        temp->next = NULL;
        prev = temp;
    }
    return head;
}
