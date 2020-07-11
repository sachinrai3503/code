// https://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/
/*
Given a number line from -infinity to +infinity. 
You start at 0 and can go either to the left or to the right. 
The condition is that in i’th move, you take i steps.

a) Find if you can reach a given number x
b) Find the most optimal way to reach a given number x, 
if we can indeed reach it. 

For example, 3 can be reached in 2 steps, (0, 1) (1, 3)
 and 4 can be reached in 3 steps (0, -1), (-1, 1) (1, 4).

*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

typedef struct{
    int *data;
    int front, rear, max_size;
}que;

que* init_que(int max_size){
    que *q = (que*)malloc(sizeof(que));
    if(q){
        q->data = (int*)calloc(max_size,sizeof(int));
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

void insert_que(que *q, int data){
    if(is_full(q)){
        printf("Full\n");
    }else{
        if(q->rear==q->max_size-1) q->rear = 0;
        else q->rear++;
        if(q->front==-1) q->front = 0;
        q->data[q->rear] = data; 
    }
}

int delete_que(que *q){
    if(is_empty(q)){
        printf("Empty\n");
        return INT_MIN;
    }else{
        int temp = q->data[q->front];
        if(q->rear==q->front) q->rear = q->front = -1;
        else if(q->front==q->max_size-1) q->front = 0;
        else q->front++;
        return temp;
    }
}

int is_equal(int a, int b){
    if(a==b || -a==b) return 1;
    return 0;
}

int find_min_steps(int dest){
    if(dest==0) return 0;
    if(is_equal(dest,1)) return 1;
    int count = 1;
    int step = 2;
    que *q = init_que(2000);
    insert_que(q,1);
    insert_que(q,INT_MIN);
    while(!is_empty(q) && q->data[q->front]!=INT_MIN){
        while(!is_empty(q) && q->data[q->front]!=INT_MIN){
            int temp = delete_que(q);
            if(is_equal(temp,dest))
                return count;
            insert_que(q,temp+step);
            insert_que(q,temp-step);
        }
        delete_que(q);
        insert_que(q,INT_MIN);
        count++;
        step++;
    }
    return count;
}

// https://www.geeksforgeeks.org/find-minimum-moves-reach-target-infinite-line/
int find_min_steps_2(int dest){
    if(dest==0) return 0;
    int sum = 0;
    int step = 1;
    while(sum<dest){
        sum+=step;
        step++;
    }
    if(sum==dest || (sum-dest)%2==0){
        return step-1;
    }else if((sum+step-dest)%2==0){
        return step;
    }
    return step+1;
}

int main(){
    int dest = 0;
    for(;dest<=50;dest++){
        printf("Dest = %d Min step = %d  Min step_2 = %d\n",
            dest,find_min_steps(dest),
                find_min_steps_2(dest));
    }

    return 0;
}