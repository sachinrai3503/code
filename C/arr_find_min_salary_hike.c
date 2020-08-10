// https://www.geeksforgeeks.org/minimum-salary-hike-for-each-employee-such-that-no-employee-feels-unfair/
/*
Given an array arr[] of N +ve integers which denotes the ratings of N employees,
 the task is to find the minimum hike that should be raised for each employee,
 such that no employee feels unfair.

An employee only knows the hike and rating of its neighbors 
i.e., on the left and right side of the employee.

Note: The hikes are positive integers only and 
the ratings are always greater than zero.

Input: arr[] = {5, 3, 4, 2, 1, 6}
Output: 2 1 3 2 1 2
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int get_max(int a, int b){
    if(a>b) return a;
    else return b;
}

/*
    Returns the last decreasing number index.
 */
int get_last_decreasing_index_in_subarr(int ip[], int length, int from_index){
    int prev = INT_MAX;
    int i = from_index;
    for(;i<length;i++){
        if(ip[i]>prev) return i-1;
        prev = ip[i];
    }
    return i-1;
}

int* get_min_hike(int ratings[], int length){
    int *hike = (int*)calloc(length,sizeof(int));
    int prev_hike = 0;
    int i = 0;
    while(i<length){
        int ldr = get_last_decreasing_index_in_subarr(ratings,length,i);
        int min_hike = 1;
        int j = ldr;
        while(ratings[j]<ratings[i]){
            hike[j] = min_hike;
            if(ratings[j-1]>ratings[j])
                min_hike+=1;
            j--;
        }
        while(j>=i){
            hike[j] = get_max(prev_hike+1,min_hike);
            j--;
        }
        prev_hike = hike[ldr];
        i = ldr+1;
    }
    return hike;
}

int main(){
    int rating[] = {5,3,4,2,1,6};
    int length = sizeof(rating)/sizeof(rating[0]);
    print_arr(rating,length);
    int *hike = get_min_hike(rating,length);
    print_arr(hike,length);
    return 0;
}