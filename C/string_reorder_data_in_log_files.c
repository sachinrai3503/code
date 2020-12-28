// https://leetcode.com/problems/reorder-data-in-log-files/
/*
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  

Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  

It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log. 

The letter-logs are ordered lexicographically ignoring identifier,
 with the identifier used in case of ties.  

The digit-logs should be put in their original order.

Return the final order of the logs.
Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

int get_first_space_index(char *ip, int length){
    int i = 0;
    for(;i<length;i++){
        if(ip[i]==' ') return i;
    }
    return i;
}

int is_num_log(char *ip, int length, int _1st_space_index){
    int i = _1st_space_index + 1;
    for(;i<length && ip[i]!=' ';i++){
        if(!(ip[i]>=48 && ip[i]<=57)) return 0;
    }
    return 1;
}

void swap_logs(char **a, char **b){
    char *temp = *a;
    *a = *b;
    *b = temp;
}

void swap_int(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int compare(char *ip1, int len1, int from1, char *ip2, int len2, int from2){
    int i = from1;
    int j = from2;
    while(i<len1 && j<len2){
        while(i<len1 && j<len2 && ip1[i]!=' ' && ip2[j]!=' '){
            if(ip1[i]>ip2[j]) return 1;
            else if(ip1[i]<ip2[j]) return -1;
            i++;
            j++;
        }
        if(i==len1 && j==len2) break;
        else if(i!=len1 && ip1[i]==' ' && j!=len2 && ip2[j]==' '){
            i++;
            j++;
        }
        else if(i==len1 || ip1[i]==' ') return -1;
        else if(j==len2 || ip2[j]==' ') return 1;
    }
    return compare(ip1, len1, 0, ip2, len2, 0);
}

typedef struct{
    char **data;
    int *_1st_space_index;
    int current_size, max_size;
}heap;

heap* init_heap(char **ip, int *_1st_space_index, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = ip;
        _heap->_1st_space_index = _1st_space_index;
        _heap->current_size = length;
        _heap->max_size = length;
    }
    return _heap;
}

void max_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int max_index = index;
    if(left<_heap->current_size && 
       compare(_heap->data[max_index],strlen(_heap->data[max_index]), _heap->_1st_space_index[max_index]+1,
               _heap->data[left],strlen(_heap->data[left]), _heap->_1st_space_index[left]+1)==-1) max_index = left;
    if(right<_heap->current_size && 
       compare(_heap->data[max_index],strlen(_heap->data[max_index]), _heap->_1st_space_index[max_index]+1,
               _heap->data[right],strlen(_heap->data[right]), _heap->_1st_space_index[right]+1)==-1) max_index = right;
    if(max_index!=index){
        swap_logs(_heap->data+max_index, _heap->data+index);
        swap_int(_heap->_1st_space_index+max_index, _heap->_1st_space_index+index);
        max_heapify(_heap, max_index);
    }
}

heap* build_heap(char **ip, int *_1st_space_index, int length){
    heap *_heap = init_heap(ip,_1st_space_index,length);
    int parent_index = (_heap->current_size-2)/2;
    for(;parent_index>=0;parent_index=parent_index-1){
        max_heapify(_heap, parent_index);
    }
    return _heap;
}

void heap_sort(char **ip, int *_1st_space_index, int length){
    heap *_heap = build_heap(ip,_1st_space_index,length);
    while(_heap->current_size>1){
        swap_logs(_heap->data, _heap->data+(--_heap->current_size));
        swap_int(_heap->_1st_space_index, _heap->_1st_space_index+_heap->current_size);
        max_heapify(_heap, 0);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** reorderLogFiles(char ** logs, int logsSize, int* returnSize){
    int *_1st_space_index = (int*)calloc(logsSize,sizeof(int));
    int k = logsSize-1;
    int i = logsSize-1;
    for(;i>=0;i--){
        int log_len = strlen(logs[i]);
        int _1st_space = get_first_space_index(logs[i], log_len);
        _1st_space_index[i] = _1st_space;
        if(is_num_log(logs[i], log_len, _1st_space)){
            if(i!=k){
                swap_logs(logs+i,logs+k);
                swap_int(_1st_space_index+i, _1st_space_index+k);
            }
            k--;
        }
    }
    heap_sort(logs,_1st_space_index,k+1);
    *returnSize = logsSize;
    return logs;
}