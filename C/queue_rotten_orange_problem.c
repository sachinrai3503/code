// https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
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

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int ip[], int row, int col){
    int i = 0;
    for(;i<col;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2D(int (*ip)[50], int row, int col){
    int i = 0;
    for(;i<row;i++){
        print_arr(ip[i],row,col);
    }
}

typedef struct{
    int row, col;
}que_data;

que_data* init_que_data(int row, int col){
    que_data *data = (que_data*)malloc(sizeof(que_data));
    if(data){
        data->row = row;
        data->col = col;
    }
    return data;
}

typedef struct {
    que_data **data;
    int front, rear;
    int max_size;
}queue;

queue* init_queue(int max_size){
    queue *que = (queue*)malloc(sizeof(queue));
    if(que){
        que->data = (que_data**)calloc(max_size,sizeof(que_data*));
        que->front = que->rear = -1;
        que->max_size = max_size;
    }
    return que;
}

int is_empty(queue *que){
    if(que->front==-1) return 1;
    return 0;
}

int is_full(queue *que){
    if((que->front==0 && que->rear==que->max_size-1) || (que->rear==que->front-1)) return 1;
    return 0;
}

void insert_que(queue *que, que_data *data){
    if(is_full(que)){
        printf("Full\n");
    }else if(data){
        if(que->rear==que->max_size-1) que->rear = 0;
        else que->rear++;
        if(que->front==-1) que->front=0;
        que->data[que->rear] = data;
    }
}

que_data* delete_front(queue *que){
    if(is_empty(que)){
        printf("Empty\n");
        return NULL;
    }else{
        que_data *temp = que->data[que->front];
        if(que->front==que->rear) que->front = que->rear = -1;
        else if(que->front==que->max_size-1) que->front = 0;
        else que->front++;
        return temp;
    }
}

int is_valid_position(int row, int col, int i, int j){
    if(i<0 || j<0 || i>=row || j>=col) return 0;
    return 1;
}

int has_all_rotten(int (*ip)[50], int row, int col){
    int i = 0;
    for(;i<row;i++){
        int j = 0;
        for(;j<col;j++){
            if(ip[i][j]==1) return 0;
        }
    }
    return 1;
}

void insert_all_rotten_oranges(int (*ip)[50], int row, int col, queue *que){
    int i = 0;
    for(;i<row;i++){
        int j = 0;
        for(;j<col;j++){
            if(ip[i][j]==2){
                insert_que(que,init_que_data(i,j));
            }
        }
    }
}

void mark_rotten(int (*ip)[50], int row, int col, int i, int j){
    if(is_valid_position(row,col,i,j)) ip[i][j] = 2;
}

int is_fresh(int (*ip)[50], int row, int col, int i, int j){
    if(is_valid_position(row,col,i,j) && ip[i][j]==1) return 1;
    return 0;
}

void rot_adjacent(int (*ip)[50], queue *que, que_data *temp, int row, int col){
    int step[2][4] = {  {1,-1,0,0},
                        {0,0,1,-1}};
    int i = 0;
    for(;i<4;i++){
        if(is_fresh(ip,row,col,temp->row+step[0][i],temp->col+step[1][i])){
            mark_rotten(ip,row,col,temp->row+step[0][i],temp->col+step[1][i]);
            insert_que(que,init_que_data(temp->row+step[0][i],temp->col+step[1][i]));
        }
    }
}

int get_min_time_to_rot(int (*ip)[50], int row, int col){
    int min_time = 0;
    queue *que = init_queue(row*col+10);
    que_data *null_node = init_que_data(INT_MIN,INT_MIN);
    insert_all_rotten_oranges(ip,row,col,que);
    insert_que(que,null_node);
    while(!is_empty(que) && que->data[que->front]!=null_node){
        min_time++;
        while(!is_empty(que) && que->data[que->front]!=null_node){
            que_data *temp = delete_front(que);
            rot_adjacent(ip,que,temp,row,col);
        }
        delete_front(que);
        insert_que(que,null_node);
    }
    if(has_all_rotten(ip,row,col)) return min_time-1;
    return -1;
}

int main(){
    int ip[50][50] = {  {2, 1, 1, 1, 2},
                        {0, 0, 0, 0, 0},
                        {1, 1, 1, 1, 1}};
    int row = 3;
    int col = 5;

    print_2D(ip,row,col);

    printf("Min time to rot = %d\n",get_min_time_to_rot(ip,row,col));

    return 0;
}