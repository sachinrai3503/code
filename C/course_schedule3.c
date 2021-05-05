// https://leetcode.com/problems/course-schedule-iii/
/*
There are n different online courses numbered from 1 to n. Each course has some
 duration(course length) t and closed on dth day. A course should be taken
 continuously for t days and must be finished before or on the dth day.
 You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the
 maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
*/

// NOTE - This method is correct but it would exceed the time limits.
// See the CourseSchedule3.java for better approach. Time O(nlogn). Space - O(n)

/*
IMP Test cases - 
[[2,5],[2,19],[1,8],[1,3]] -- This test cases shows why sorting is needed.
[[100,200],[200,1300],[1000,1250],[2000,3200]]
[[100,200],[500,800],[900,1000],[200,300],[50,600]]
[[7,11],[1,11],[1,3],[2,6],[5,6],[7,7],[4,8],[2,20],[1,17],[8,11]]
*/

typedef struct{
    int **data;
    int max_size;
    int cur_size;
}heap;

heap* init_heap(int** data, int length){
    heap *_heap = (heap*)malloc(sizeof(heap));
    if(_heap){
        _heap->data = data;
        _heap->max_size = length;
        _heap->cur_size = length;
    }
    return _heap;
}

void swap(int **data, int i, int j){
    int a = data[i][0];
    int b = data[i][1];
    data[i][0] = data[j][0];
    data[i][1] = data[j][1];
    data[j][0] = a;
    data[j][1] = b;
}

int compare(int *a, int *b){
    if(a[1]>b[1]) return 1;
    if(a[1]<b[1]) return -1;
    if(a[0]>b[0]) return 1;
    if(a[0]<b[0]) return -1;
    return 0;
}

void max_heapify(heap *_heap, int index){
    int left = index*2+1;
    int right = index*2+2;
    int max_index = index;
    if(left<_heap->cur_size && compare(_heap->data[left], _heap->data[max_index])==1) max_index = left;
    if(right<_heap->cur_size && compare(_heap->data[right], _heap->data[max_index])==1) max_index = right;
    if(max_index!=index){
        swap(_heap->data, max_index, index);
        max_heapify(_heap, max_index);
    }
}

heap* build_heap(int **data, int length){
    heap *_heap = init_heap(data, length);
    int parent_index = (_heap->cur_size-2)/2;
    for(;parent_index>=0;parent_index--){
        max_heapify(_heap, parent_index);
    }
    return _heap;
}


void sort(int **data, int length){
    heap *_heap = build_heap(data, length);
    while(_heap->cur_size>1){
        swap(_heap->data, 0, --_heap->cur_size);
        max_heapify(_heap, 0);
    }
}

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2D(int **data, int length){
    int i = 0;
    for(;i<length;i++){
        print_arr(data[i],2);
    }
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}


int scheduleCourse(int** courses, int coursesSize, int* coursesColSize){
    sort(courses, coursesSize);
    // print_2D(courses, coursesSize);
    int *op = (int*)calloc(courses[coursesSize-1][1] + 1, sizeof(int));
    int i = coursesSize-1;
    for(;i>=0;i--){
        int max_start_time = courses[i][1]-courses[i][0];
        int duration = courses[i][0];
        int j = 0;
        for(;j<=max_start_time;j++){
            op[j] = get_max(op[j], 1 + op[j+duration]);
        }
    }
    return op[0];
}