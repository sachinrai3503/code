// https://www.geeksforgeeks.org/least-frequently-used-lfu-cache-implementation
// https://leetcode.com/problems/lfu-cache
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

typedef struct{
    int key, value;
    int freq, last_accessed_at;
    int cache_index;
}page;

typedef struct {
    page **data;
    int max_size;
    int cur_size;
    page **page_index;
    int counter;
} LFUCache;

page* init_page(int key, int value, int freq, int last_accessed_at){
    page *_page = (page*)malloc(sizeof(page));
    if(_page){
        _page->key = key;
        _page->value = value;
        _page->freq = freq;
        _page->last_accessed_at = last_accessed_at;
        _page->cache_index = -1;
    }
    return _page;
}

LFUCache* lFUCacheCreate(int capacity) {
    LFUCache *lfu = (LFUCache*)malloc(sizeof(LFUCache));
    if(lfu){
        lfu->data = (page**)calloc(capacity, sizeof(page*));
        lfu->max_size = capacity;
        lfu->cur_size = 0;
        lfu->page_index = (page**)calloc(10000, sizeof(page*));
        lfu->counter = 0;
    }
    return lfu;
}

int is_full(LFUCache *lfu){
    if(lfu->cur_size==lfu->max_size) return 1;
    return 0;
}

int is_empty(LFUCache *lfu){
    if(lfu->cur_size==0) return 1;
    return 0;
}

void print_cache(LFUCache *lfu){
    int i = 0;
    for(;i<lfu->cur_size;i++){
        page *_page = lfu->data[i];
        printf("(k=%d-v=%d-f=%d-lac=%d-in=%d) ",_page->key, _page->value, 
               _page->freq, _page->last_accessed_at, _page->cache_index);
    }
    printf("\n");
}

void swap(page **a, page **b){
    page *temp = *a;
    *a = *b;
    *b = temp;
    int t_index = (*a)->cache_index;
    (*a)->cache_index = (*b)->cache_index;
    (*b)->cache_index = t_index;
}

int compare(page *a, page *b){
    if(a->freq<b->freq) return -1;
    if(a->freq>b->freq) return 1;
    if(a->last_accessed_at<b->last_accessed_at) return -1;
    if(a->last_accessed_at>b->last_accessed_at) return 1;
    return 0;
}

void min_heapify(LFUCache *lfu, int index){
    int left = index*2+1;
    int right = index*2+2;
    int min_index = index;
    if(left<lfu->cur_size && compare(lfu->data[left], lfu->data[min_index])==-1)
        min_index = left;
    if(right<lfu->cur_size && compare(lfu->data[right], lfu->data[min_index])==-1)
        min_index = right;
    if(min_index!=index){
        swap(lfu->data+min_index, lfu->data+index);
        min_heapify(lfu, min_index);
    }
}

void insert_in_lfu_cache(LFUCache *lfu, page *_page){
    if(is_full(lfu)){
        printf("Full\n");
        return;
    }else if(_page){
        _page->cache_index = lfu->cur_size;
        lfu->data[lfu->cur_size++] = _page;
        int parent_index = (lfu->cur_size-2)/2;
        for(;parent_index>0;parent_index = (parent_index-1)/2){
            min_heapify(lfu, parent_index);
        }
        if(parent_index==0){
            min_heapify(lfu, parent_index);
        }
    }
}

page* delete_cache_top(LFUCache *lfu){
    if(is_empty(lfu)){
        printf("Empty\n");
        return NULL;
    }else{
        page *temp = lfu->data[0];
        swap(lfu->data,lfu->data + (--lfu->cur_size));
        min_heapify(lfu, 0);
        return temp;
    }
}

int lFUCacheGet(LFUCache* obj, int key) {
    obj->counter++;
    if(obj->page_index[key]==NULL) return -1;
    page *temp = obj->page_index[key];
    temp->freq++;
    temp->last_accessed_at = obj->counter;
    min_heapify(obj, temp->cache_index);
    // printf("Get=>");print_cache(obj);
    return temp->value;
}

void lFUCachePut(LFUCache* obj, int key, int value) {
    if(obj->max_size==0) return;
    page *_page = NULL;
    if(obj->page_index[key]!=NULL){
        obj->counter++;
        page *temp = obj->page_index[key];
        temp->freq++;
        temp->last_accessed_at = obj->counter;
        temp->value = value;
        min_heapify(obj, temp->cache_index);
    }else{
        obj->counter++;
        _page = init_page(key, value, 1, obj->counter);
        if(is_full(obj)){
            page *t_page = delete_cache_top(obj);
            obj->page_index[t_page->key] = NULL;
            free(t_page);
        }
        insert_in_lfu_cache(obj, _page);
        obj->page_index[_page->key] = _page;
    }
    // printf("Put=>");print_cache(obj);
}

void lFUCacheFree(LFUCache* obj) {
    free(obj->data);
    free(obj->page_index);
    free(obj);
}

/**
 * Your LFUCache struct will be instantiated and called as such:
 * LFUCache* obj = lFUCacheCreate(capacity);
 * int param_1 = lFUCacheGet(obj, key);
 
 * lFUCachePut(obj, key, value);
 
 * lFUCacheFree(obj);
*/