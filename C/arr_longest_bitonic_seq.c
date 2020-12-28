// https://www.geeksforgeeks.org/longest-bitonic-subsequence-dp-15/
// https://www.geeksforgeeks.org/longest-bitonic-subsequence-onlogn
/*
Given an array arr[0 … n-1] containing n positive integers, a subsequence of 
 arr[] is called Bitonic if it is first increasing, then decreasing. Write a
 function that takes an array as argument and returns the length of the
longest bitonic subsequence.

A sequence, sorted in increasing order is considered Bitonic with the
 decreasing part as empty. Similarly, decreasing order sequence is
 considered Bitonic with the increasing part as empty.

Examples:
Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)
*/

//TODO - Print the bitonic subseq

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
    int *nums;
    int *data;
    int curSize, maxSize;
}lisData;

lisData* initLisData(int *nums, int numsSize){
    lisData *_data = (lisData*)malloc(sizeof(lisData));
    if(_data){
        _data->nums = nums;
        _data->data = (int*)calloc(numsSize, sizeof(int));
        _data->curSize = 0;
        _data->maxSize = numsSize;
    }
    return _data;
}

int getFloor(lisData *_data, int k){
    int _floor = -1;
    int s = 0, e = _data->curSize-1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(_data->nums[_data->data[mid]]<k){
            _floor = mid;
            s = mid+1;
        }else{
            e = mid-1;
        }
    }
    return _floor;
}

void addLisData(lisData *_data, int index, int value){
    if(_data){
        if(_data->curSize<=index){
            _data->curSize++;
        }
        _data->data[index] = value;
    }
}

int* getLIS(int* nums, int numsSize){
    int *op = (int*)calloc(numsSize, sizeof(int));
    lisData *_data = initLisData(nums, numsSize);
    int i = 0;
    for(;i<numsSize;i++){
        int _floor = getFloor(_data, nums[i]);
        addLisData(_data, _floor+1, i);
        op[i] = _data->curSize;
    }
    return op;
}

int getBitonicSubseqLen(int *nums, int numsSize){
    int *lis = getLIS(nums, numsSize);
    int maxLen = lis[numsSize-1];
    lisData *_data = initLisData(nums, numsSize);
    int i = numsSize-1;
    for(;i>=0;i--){
        int _floor = getFloor(_data, nums[i]);
        addLisData(_data, _floor+1, i);
        int tLen = _data->curSize;
        if(i>0 && lis[i-1] + tLen > maxLen) maxLen = lis[i-1] + tLen;
        else if(i==0 && tLen > maxLen) maxLen = tLen;
    }
    return maxLen;
}

int main(){

    int nums[] = {0, 8, 4, 12, 2, 10, 6, 14, 
                  1, 9, 5, 13, 3, 11, 7, 15};
    int length = sizeof(nums)/sizeof(nums[0]);

    printArr(nums, length);
    printf("Max Bitonic length = %d\n",getBitonicSubseqLen(nums, length));

    return 0;
}