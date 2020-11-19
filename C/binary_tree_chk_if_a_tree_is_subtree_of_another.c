// https://leetcode.com/problems/subtree-of-another-tree/
// https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
/*
Given two non-empty binary trees s and t, check whether tree t has 
exactly the same structure and node values with a subtree of s. 

A subtree of s is a tree consists of a node in s and all
 of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node
 values with a subtree of s.
 
*/
#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#define false 0
#define true 1

typedef int bool;

//   Definition for a binary tree node.
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}treeNode;
 
void printArr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

typedef struct{
    int *data;
    int length;
    int index;
}list;

list* initList(int length){
    list *_list = (list*)malloc(sizeof(list));
    if(_list){
        _list->data = (int*)calloc(length,sizeof(int));
        _list->length = length;
        _list->index = -1;
    }
    return _list;
}

void extendListBy(list *_list, int extraLength){
    if(_list){
        int newLength = _list->length+extraLength;
        _list->data = (int*)realloc(_list->data, sizeof(int)*newLength);
        _list->length = newLength;
    }
}

bool isFull(list *_list){
    if(_list){
        if(_list->index==_list->length-1) return true;
        return false;
    }
    return false;
}

void addToList(list *_list, int data){
    if(_list){
        if(isFull(_list)) extendListBy(_list, 100);
     
     
        _list->data[++_list->index] = data;
    }
}

list* preOrder(treeNode *root, list *_list){
    if(!_list) _list = initList(100);
    if(root){
        addToList(_list, root->val);
        preOrder(root->left, _list);
        preOrder(root->right, _list);
    }else{
        addToList(_list, INT_MIN);
    }
    return _list;
}

list* inOrder(treeNode *root, list *_list){
    if(!_list) _list = initList(100);
    if(root){
        inOrder(root->left, _list);
        addToList(_list, root->val);
        inOrder(root->right, _list);
    }else{
        addToList(_list, INT_MIN);
    }
    return _list;
}

int* getLps(int *ip, int length){
    int *lps = (int*)calloc(length,sizeof(int));
    int i = 0;
    while(i<length){
        int j = i-1;
        while(j>0 && ip[lps[j]]!=ip[i]){
            j = lps[j]-1;
        }
        if(j==-1) lps[i] = 0;
        else if(ip[lps[j]]==ip[i]) lps[i] = lps[j]+1;
        else lps[i] = 0;
        i++;
    }
    return lps;
}

bool isPresent(int *text, int textLen, int *pat, int patLen){
    if(patLen<=0) return false;
    int *lps = getLps(pat, patLen);
    int i = 0, j = 0;
    while(i<textLen){
        if(text[i]==pat[j]){
            i++;
            j++;
        }else if(j==0){
            i++;
        }else{
            j = lps[j-1];
        }
        if(j==patLen){
            j = lps[j-1];
            return true;
        }
    }
    return false;
}

bool isSubtree(struct TreeNode* s, struct TreeNode* t){
    list *preListS = preOrder(s,NULL);
    list *inListS = inOrder(s,NULL);
    list *preListT = preOrder(t,NULL);
    list *inListT = inOrder(t,NULL);
    
    // printf("PreLen = %d index=%d\n",preListS->length,preListS->index);
    // printf("Pre s>>");printArr(preListS->data,preListS->index+1);
    // printf("In s>>");printArr(inListS->data,inListS->index+1);
    // printf("Pre t>>");printArr(preListT->data,preListT->index+1);
    // printf("In t>>");printArr(inListT->data,inListT->index+1);
    
    
    if(isPresent(preListS->data,preListS->index+1,preListT->data,preListT->index+1)){
       if(isPresent(inListS->data,inListS->index+1,inListT->data,inListT->index+1)){
            return true;
       }
    }
    return false;
}