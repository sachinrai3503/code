// https://leetcode.com/problems/design-circular-queue
/*
Design your implementation of the circular queue. The circular queue is a linear
 data structure in which the operations are performed based on FIFO (First In First Out)
 principle, and the last position is connected back to the first position to make a circle.
 It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front 
 of the queue. In a normal queue, once the queue becomes full, we cannot insert the next
 element even if there is a space in front of the queue. But using the circular queue, we
 can use the space to store new values.

Implement the MyCircularQueue class:
MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true
 if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the
 operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your
 programming language. 

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull",
     "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
*/

#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>

typedef struct {
    int *data;
    int maxsize;
    int front, rear;
} MyCircularQueue;

bool myCircularQueueIsEmpty(MyCircularQueue*);
bool myCircularQueueIsFull(MyCircularQueue*);

void print_queue(MyCircularQueue *que){
  printf("front=%d rear=%d\n",que->front, que->rear);
}

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *que = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    if(que){
        que->data = (int*)malloc(sizeof(int)*k);
        que->maxsize = k;
        que->front = que->rear = -1;
    }
    return que; 
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
  if(myCircularQueueIsFull(obj)) return false;
  if(obj->rear==(obj->maxsize-1)) obj->rear=0;
  else obj->rear++;
  if(obj->front==-1) obj->front = 0;
  obj->data[obj->rear] = value;
  // print_queue(obj);
  return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
  if(myCircularQueueIsEmpty(obj)) return false;
  int temp = obj->data[obj->front];
  if(obj->front==obj->rear) obj->front = obj->rear = -1;
  else if(obj->front==(obj->maxsize-1)) obj->front = 0;
  else obj->front++;
  // print_queue(obj);
  return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
  if(myCircularQueueIsEmpty(obj)) return -1;
  return obj->data[obj->front];
}

int myCircularQueueRear(MyCircularQueue* obj) {
  if(myCircularQueueIsEmpty(obj)) return -1;
  return obj->data[obj->rear];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
  return obj->front==-1;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
  if((obj->front==0 && obj->rear==(obj->maxsize-1)) || (obj->rear==(obj->front-1))) return true;
  return false;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->data);
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/