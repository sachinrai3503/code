// https://www.geeksforgeeks.org/find-number-of-islands/
// https://www.geeksforgeeks.org/islands-in-a-graph-using-bfs/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

int adjacent_node[2][8] = { {-1, 1, 0, -1, 1,-1,0,1},
                            {-1, -1,-1, 0, 0, 1,1,1}
                        };

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2d(int (*ip)[50], int row, int col){
    int i = 0;
    for(;i<row;i++){
        print_arr(ip[i],col);
    }
}

void init_arr(int ip[], int length, int value){
    int i = 0;
    for(;i<length;i++){
        ip[i] = value;
    }
}

void init_arr_2d(int (*ip)[50], int row, int col, int value){
    int i = 0;
    for(;i<row;i++){
        init_arr(ip[i],col,value);
    }
}


typedef struct{
    int i,j;
}que_node;

que_node* make_que_node(int i, int j){
    que_node *nw = (que_node*)malloc(sizeof(que_node));
    if(nw){
        nw->i = i;
        nw->j = j;
    }
    return nw;
}

typedef struct{
    que_node **data;
    int front, rear;
    int max_size;
}que;

que* init_que(int max_size){
    que *q = (que*)malloc(sizeof(que));
    if(q){
        q->data = (que_node**)calloc(max_size,sizeof(que_node*));
        q->front = q->rear = -1;
        q->max_size = max_size;
    }
    return q;
}

int is_full(que *q){
    if((q->front==0 && q->rear==q->max_size-1) || (q->rear==q->front-1)) return 1;
    return 0;
}

int is_empty(que *q){
    if(q->front==-1) return 1;
    return 0;
}

void insert_que(que *q, que_node *data){
    if(is_full(q)){
        printf("Full\n");
    }else if(data){
        if(q->rear==q->max_size-1) q->rear = 0;
        else q->rear++;
        if(q->front==-1) q->front = 0;
        q->data[q->rear] = data;
    }
}

que_node* delete_que(que *q){
    if(is_empty(q)){
        printf("Empty\n");
        return NULL;
    }else{
        que_node *temp = q->data[q->front];
        if(q->rear==q->front) q->rear = q->front = -1;
        else if(q->front==q->max_size-1) q->front = 0;
        else q->front++;
        return temp;
    }
}

int is_visited(int (*visited)[50], int i, int j){
    if(visited[i][j]==0) return 0;
    return 1;
}

int is_valid_position(int row, int col, int i, int j){
    if(i<0 || j<0) return 0;
    if(i>=row || j>=col) return 0;
    return 1;
}

void visit_connected_comp_DFS(int (*ip)[50], int row, int col, int i, int j, int (*visited)[50]){
    if(is_valid_position(row,col,i,j)==0) return;
    if(ip[i][j]==0 || is_visited(visited,i,j)) return;
    visited[i][j] = 1;
    int k = 0;
    for(;k<8;k++){
        visit_connected_comp_DFS(ip,row,col,i+adjacent_node[0][k],j+adjacent_node[1][k],visited);
    }
}

int get_connected_comp_count_DFS(int (*ip)[50], int row, int col){
    int count = 0;
    int visited[50][50];
    init_arr_2d(visited,row,col,0);
    int i = 0;
    for(;i<row;i++){
        int j = 0;
        for(;j<col;j++){
            if(ip[i][j]==1 && visited[i][j]==0){
                visit_connected_comp_DFS(ip,row,col,i,j,visited);
                count++;
            }
        }
    }
    return count;
}

void visit_connected_comp_BFS(int (*ip)[50], int row, int col, int i, int j, int (*visited)[50]){
    que *q = init_que(20);
    insert_que(q,make_que_node(i,j));
    visited[i][j] = 1;
    while(!is_empty(q)){
        que_node *temp = delete_que(q);
        int k = 0;
        for(;k<8;k++){
            int next_i = temp->i+adjacent_node[0][k];
            int next_j = temp->j+adjacent_node[1][k];
            if(is_valid_position(row,col,next_i,next_j) && visited[next_i][next_j]==0 && ip[next_i][next_j]){
                insert_que(q,make_que_node(next_i,next_j));
                visited[next_i][next_j] = 1;
            }
        }
    }
}

int get_connected_comp_count_BFS(int (*ip)[50], int row, int col){
    int count = 0;
    int visited[50][50];
    init_arr_2d(visited,row,col,0);
    int i = 0;
    for(;i<row;i++){
        int j = 0;
        for(;j<col;j++){
            if(ip[i][j]==1 && visited[i][j]==0){
                visit_connected_comp_BFS(ip,row,col,i,j,visited);
                count++;
            }
        }
    }
    return count;
}

int main(){
    int ip[50][50] = {  {1, 1, 0, 0, 0},
                        {0, 1, 0, 0, 1},
                        {1, 0, 0, 1, 1},
                        {0, 1, 0, 0, 0},
                        {1, 0, 1, 1, 1}
                    };
    int row = 5;
    int col = 5;

    print_2d(ip,row,col);

    printf("(DFS)Connected comp. count = %d \n",get_connected_comp_count_DFS(ip,row,col));
    printf("(BFS)Connected comp. count = %d \n",get_connected_comp_count_BFS(ip,row,col));

    return 0;
}