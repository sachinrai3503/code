// https://www.geeksforgeeks.org/least-frequently-used-lfu-cache-implementation
// https://leetcode.com/problems/lfu-cache/
/*
Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

- LFUCache(int capacity) Initializes the object with the capacity of the DS.
- int get(int key) Gets the value of the key if the key exists in the cache.
   Otherwise, returns -1.
- void put(int key, int value) Sets or inserts the value if the key is not
   already present. When the cache reaches its capacity, it should invalidate
   the least frequently used item before inserting a new item. For this problem,
   when there is a tie (i.e., two or more keys with the same frequency),
   the least recently used key would be evicted.
  
Notice that the number of times an item is used is the number of calls to the
 get and put functions for that item since it was inserted. This number is set
 to zero when the item is removed.

Example 1:
Input - 
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output - [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);
lfu.put(2, 2);
lfu.get(1);      // return 1
lfu.put(3, 3);   // evicts key 2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.put(4, 4);   // evicts key 1.
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.get(4);      // return 4
 
Constraints:
- 0 <= capacity, key, value <= 104
- At most 105 calls will be made to get and put.
*/

#include <stdio.h>
#include <malloc.h>

typedef struct heap_node {
    int data;
    int key;
    int freq_used;
    int last_used;
    int heap_index;
}node;

typedef struct {
    node **data;
    node **key_map;
    int cur_size;
    int max_size;
    int oper_ser_no;
} LFUCache;

node* init_heap_node(int key, int data){
    node *_node = (node*)malloc(sizeof(node));
    if(_node){
        _node->key = key;
        _node->data = data;
        _node->freq_used = 0;
        _node->last_used = -1;
        _node->heap_index = -1;
    }
    return _node;
}

int compare(node *a, node *b){
    if(a->freq_used>b->freq_used) return 1;
    if(a->freq_used<b->freq_used) return -1;
    if(a->last_used>b->last_used) return 1;
    if(a->last_used<b->last_used) return -1;
    return 0;
}

int is_full(LFUCache *LFU){
    if(LFU->cur_size==LFU->max_size) return 1;
    return 0;
}

int is_empty(LFUCache *LFU){
    if(LFU->cur_size==0) return 1;
    return 0;
}

void swap(node **a, node **b){
    node *temp = *a;
    *a = *b;
    *b = temp;
    int index = (*a)->heap_index;
    (*a)->heap_index = (*b)->heap_index;
    (*b)->heap_index = index;
}

void min_heapify(LFUCache *LFU, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<LFU->cur_size && compare(LFU->data[left], LFU->data[min_index])==-1) min_index = left;
    if(right<LFU->cur_size && compare(LFU->data[right], LFU->data[min_index])==-1) min_index = right;
    if(min_index!=index){
        swap(LFU->data+index, LFU->data+min_index);
        min_heapify(LFU, min_index);
    }
}

node* delete_top(LFUCache *LFU){
    if(is_empty(LFU)){
        printf("Empty");
        return NULL;
    }else{
        node *temp = LFU->data[0];
        swap(LFU->data, LFU->data+(--LFU->cur_size));
        min_heapify(LFU, 0);
        temp->heap_index = -1;
        LFU->key_map[temp->key] = NULL;
        return temp;
    }
}

void insert_heap(LFUCache *LFU, node *data){
    if(is_full(LFU)){
        printf("FULL\n");
        return;
    }else if(data){
        LFU->data[LFU->cur_size] = data;
        data->heap_index = LFU->cur_size++;
        int parent_index = (LFU->cur_size-2)/2;
        for(;parent_index>0;parent_index=(parent_index-1)/2){
            min_heapify(LFU, parent_index);
        }
        if(parent_index==0){
            min_heapify(LFU, parent_index);
        }
        LFU->key_map[data->key] = data;
    }
}

LFUCache* lFUCacheCreate(int capacity) {
    LFUCache *lfu = (LFUCache*)malloc(sizeof(LFUCache));
    if(lfu){
        lfu->data = (node**)calloc(capacity, sizeof(node*));
        lfu->key_map = (node**)calloc(10001, sizeof(node*));
        lfu->cur_size = 0;
        lfu->max_size = capacity;
        lfu->oper_ser_no = 0;
    }
    return lfu;
}

int lFUCacheGet(LFUCache* obj, int key) {
    if(obj->key_map[key]==NULL) return -1;
    node *_node = obj->key_map[key];
    _node->freq_used++;
    _node->last_used = ++obj->oper_ser_no;
    min_heapify(obj, _node->heap_index);
    return _node->data;
}

void lFUCachePut(LFUCache* obj, int key, int value) {
    node *_node = obj->key_map[key];
    if(_node){
        _node->data = value;
        _node->freq_used++;
        _node->last_used = ++obj->oper_ser_no;
        min_heapify(obj, _node->heap_index);
    }else{
        if(is_full(obj)){
            delete_top(obj);
        }
        _node = init_heap_node(key, value);
        _node->freq_used = 1;
        _node->last_used = ++obj->oper_ser_no;
        insert_heap(obj, _node);
    }
}

void lFUCacheFree(LFUCache* obj) {
    free(obj->data);
    free(obj->key_map);
    free(obj);
}

/**
 * Your LFUCache struct will be instantiated and called as such:
 * LFUCache* obj = lFUCacheCreate(capacity);
 * int param_1 = lFUCacheGet(obj, key);
 
 * lFUCachePut(obj, key, value);
 
 * lFUCacheFree(obj);
*/