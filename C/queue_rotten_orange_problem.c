// https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
// https://leetcode.com/problems/rotting-oranges/
/*
Given a matrix of dimension m*n where each cell in the matrix 
can have values 0, 1 or 2 which has the following meaning:
0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges 

Determine what is the minimum time required so that
 all the oranges become rotten. 
A rotten orange at index [i,j] can rot other 
    fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] 
    (up, down, left and right). 

If it is impossible to rot every orange then simply return -1.

Examples:
Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2-time frames.
*/

// For python sol. refer queue_rotten_orange_problem.py

#include <stdio.h>
#include <malloc.h>
#define true 1
#define false 0

typedef int bool;

typedef struct{
    int i, j;
}queueNode;

typedef struct{
    queueNode **data;
    int front, rear;
    int maxsize;
}queue;

queueNode* init_queue_node(int i, int j){
    queueNode *node = (queueNode*)malloc(sizeof(queueNode));
    if(node){
        node->i = i;
        node->j = j;
    }
    return node;
}

queue* init_queue(int maxsize){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->data = (queueNode**)calloc(maxsize, sizeof(queueNode*));
        que->front = que->rear = -1;
        que->maxsize = maxsize;
    }
    return que;
}

bool is_full(queue *que){
    if((que->front==0 && que->rear==(que->maxsize-1)) || (que->front==que->rear+1)) return true;
    return false;
}

bool is_empty(queue *que){
    if(que->front==-1) return true;
    return false;
}

void insert_in_queue(queue *que, queueNode *node){
    if(is_full(que)){
        printf("Full\n");
        return;
    }else{
        if(que->rear==que->maxsize-1) que->rear=0;
        else que->rear++;
        if(que->front==-1) que->front=0;
        que->data[que->rear] = node;
    }
}

queueNode* delete_from_queue(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return NULL;
    }else{
        queueNode *temp = que->data[que->front];
        if(que->front==que->rear) que->rear=que->front=-1;
        else if(que->front==que->maxsize-1) que->front=0;
        else que->front++;
        return temp;
    }
}

int orangesRotting(int** grid, int gridSize, int* gridColSize){
    int times = 0;
    int col = *gridColSize;
    int row = gridSize;
    int adj[][4] = {{0,-1,0,1},{-1,0,1,0}};
    queue *que = init_queue(gridSize*(*gridColSize)+1);
    int i = 0;
    for(;i<gridSize;i++){
        int j = 0;
        for(;j<col;j++){
            if(grid[i][j]==2)
                insert_in_queue(que, init_queue_node(i,j));
        }
    }
    insert_in_queue(que, NULL);
    while(que->data[que->front]!=NULL){
        while(que->data[que->front]!=NULL){
            queueNode *temp = delete_from_queue(que);
            int k = 0;
            for(;k<4;k++){
                int t_i = temp->i + adj[0][k], t_j = temp->j + adj[1][k];
                if(t_i<0 || t_i>=row || t_j<0 || t_j>=col) continue;
                if(grid[t_i][t_j]==1){
                    insert_in_queue(que, init_queue_node(t_i,t_j));
                    grid[t_i][t_j] = 2;
                }
            }
        }
        delete_from_queue(que);
        times++;
        insert_in_queue(que, NULL);
    }
    i = 0;
    for(;i<gridSize;i++){
        int j = 0;
        for(;j<col;j++){
            if(grid[i][j]==1)
                return -1;
        }
    }
    if(times==0) return 0;
    return times-1;
}