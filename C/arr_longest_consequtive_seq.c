// https://leetcode.com/problems/longest-consecutive-sequence/
/**
Given an unsorted array of integers nums, return the length of the longest
 consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9 
*/

// Python - list_longest_consequtive_seq.py

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
const int HASH_SIZE = 10001;
const int BRANCH_SIZE = 1000;
const int LEAF_SIZE = 100;

typedef struct{
    int parent;
    int rank;
}cell;

typedef struct{
    cell *pos, *neg;
}node;

typedef struct{
    node **data;
}leaf;

typedef struct{
    leaf **data;
}branch;

typedef struct{
    branch **data;
}hash;

cell* init_cell(int parent, int rank){
    cell *_cell = (cell*)malloc(sizeof(cell));
    if(_cell){
        _cell->parent = parent;
        _cell->rank = 1;
    }
    return _cell;
}

node* init_node(){
    node *_node = (node*)malloc(sizeof(node));
    if(_node){
        _node->pos = _node->neg = NULL;
    }
    return _node;
}

leaf* init_leaf(){
    leaf *_leaf = (leaf*)malloc(sizeof(leaf));
    if(_leaf){
        _leaf->data = (node**)calloc(LEAF_SIZE, sizeof(node*));
    }
    return _leaf;
}

branch* init_branch(){
    branch *_branch = (branch*)malloc(sizeof(branch));
    if(_branch){
        _branch->data = (leaf**)calloc(BRANCH_SIZE, sizeof(leaf*));
    }
    return _branch;
}

hash* init_hash(){
    hash *_hash = (hash*)malloc(sizeof(hash));
    if(_hash){
        _hash->data = (branch**)calloc(HASH_SIZE, sizeof(branch*));
    }
    return _hash;
}

typedef struct{
    hash *hash;
}dj_set;

dj_set* init_dj_set(){
    dj_set *set = (dj_set*)malloc(sizeof(dj_set));
    if(set){
        set->hash = init_hash();
    }
    return set;
}

cell* find_dj_cell(dj_set *set, int key, int create_flag){
    int t_key = key;
    int neg_flag = 0;
    if(key<0){
        key*=-1;
        neg_flag = 1;
    }
    int hash_index = key%HASH_SIZE;
    if(set->hash->data[hash_index]==NULL)
        if(create_flag) set->hash->data[hash_index] = init_branch();
        else return NULL;
    branch *_branch = set->hash->data[hash_index];
    key/=HASH_SIZE;
    int branch_index = key%BRANCH_SIZE;
    if(_branch->data[branch_index]==NULL)
        if(create_flag) _branch->data[branch_index] = init_leaf();
        else return NULL;
    leaf *_leaf = _branch->data[branch_index];
    key/=BRANCH_SIZE;
    int leaf_index = key%LEAF_SIZE;
    if(_leaf->data[leaf_index]==NULL)
        if(create_flag) _leaf->data[leaf_index] = init_node();
        else return NULL;
    // printf("hash_index=%d branch_index=%d leaf_index=%d\n", hash_index, branch_index, leaf_index);
    node *_node = _leaf->data[leaf_index];
    if(neg_flag){
        if(_node->neg==NULL)
            if(create_flag) _node->neg = init_cell(t_key, 1);
            else return NULL;
        return _node->neg;
    }
    if(_node->pos==NULL)
        if(create_flag) _node->pos = init_cell(t_key, 1);
        else return NULL;
    return _node->pos;
}

int find_parent(dj_set *set, int i, int create_flag){
    cell *_cell = find_dj_cell(set, i, create_flag);
    if(!_cell) return INT_MIN;
    int parent = _cell->parent;
    if(parent==i) return i;
    _cell->parent = find_parent(set, parent, create_flag);
    return _cell->parent;
}

int union_set(dj_set *set, int i, int j){
    // printf("i=%d j=%d\n", i, j);
    int parent_i = find_parent(set, i, 1);
    int parent_j = find_parent(set, j, 0);
    // printf("p_i=%d p_j=%d\n", parent_i, parent_j);
    if(parent_j==INT_MIN) return 1;
    if(parent_i==parent_j) return 0; // Returning 0 won't harm. Ideally should return cell_parent_i->rank
    cell *cell_i = find_dj_cell(set, parent_i, 0);
    cell *cell_j = find_dj_cell(set, parent_j, 0);
    int rank_i = cell_i->rank;
    int rank_j = cell_j->rank;
    if(rank_i>=rank_j){
        cell_j->parent = parent_i;
        cell_i->rank+=cell_j->rank;
        return cell_i->rank;
    }else{
        cell_i->parent = parent_j;
        cell_j->rank+=cell_i->rank;
        return cell_j->rank;
    }
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int longestConsecutive(int* nums, int numsSize){
    dj_set *set = init_dj_set();
    int max_len = 0;
    int i = 0;
    for(;i<numsSize;i++){
        // if(nums[i]!=)
        max_len = get_max(max_len, union_set(set, nums[i], nums[i]-1));
        // printf("max_len=%d\n",max_len);
        max_len = get_max(max_len, union_set(set, nums[i], nums[i]+1));
        // printf("max_len=%d\n",max_len);
        // printf("===========\n");
    }
    return max_len;
}