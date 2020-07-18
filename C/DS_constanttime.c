// https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/

/**
Design a data structure that supports the following operations in Θ(1) time
insert(x): Inserts an item x to the data structure if not already present.
remove(x): Removes an item x from the data structure if present.
search(x): Searches an item x in the data structure.
getRandom(): Returns a random element from current set of elements
*/

// Java version @DS_ConstantTime.java

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

typedef struct{
    int *data;
    int *map;
    int max_size, cur_size;
}data_strct;

void init_arr(int ip[], int length, int value){
    int i=0;
    for(;i<length;i++){
        ip[i] = value;
    }
}

data_strct* init_data_strct(int max_size){
    data_strct *ds = (data_strct*)malloc(sizeof(data_strct));
    if(ds){
        ds->data = (int*)calloc(max_size,sizeof(int));
        ds->map = (int*)calloc(10000,sizeof(int));
        init_arr(ds->map,10000,-1);
        ds->max_size = max_size;
        ds->cur_size = 0;
    }
    return ds;
}

void print_ds(data_strct *ds){
    int i = 0;
    for(;i<ds->cur_size;i++){
        printf("%d ",ds->data[i]);
    }
    printf("\n");
}

int search_ds(data_strct *ds, int data){
    if(ds->map[data]==-1){
        printf("Not present\n");
        return -1;
    }
    return ds->map[data];
}

void insert_ds(data_strct *ds, int data){
    if(search_ds(ds,data)!=-1){
        printf("Data already present\n");
        return;
    }else{
        printf("Inserting %d\n",data);
    }
    ds->data[ds->cur_size] = data;
    ds->map[data] = ds->cur_size;
    ds->cur_size++;
}

int get_random_ds(data_strct *ds){
    if(ds->cur_size<=0){
        printf("DS empty\n");
        return INT_MIN;
    }
    srand (time(NULL)); 
    int random_index = rand() % ds->cur_size;
    printf("Random index = %d\n",random_index);
    return ds->data[random_index];
}

int delete_ds(data_strct *ds, int data){
    int index = search_ds(ds,data);
    if(index!=-1){
        ds->data[index] = ds->data[--ds->cur_size];
        ds->map[data] = -1;
        ds->map[ds->data[index]] = index;
        return data;
    }else{
        printf("Not deleted\n");
        return INT_MIN;
    }
}

int main(){

    data_strct *ds = init_data_strct(100);
    int choice = 0;
    int num = 0;
    int i = 0;
    while(choice!=INT_MIN){
        printf("Press 1 to Insert\nPress 2 to delete\nPress 3 get random\n"
                    "Press 4 to exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1 : printf("Enter num to insert :");
                     scanf("%d",&num);
                     insert_ds(ds,num);
            break;
            case 2 : printf("Enter num to delete :");
                     scanf("%d",&num);
                     delete_ds(ds,num);
            break;
            case 3 : num = get_random_ds(ds);
                     printf("Random num is %d\n",num);
            break;
            case 4 : choice = INT_MIN;
            break;
            default : printf("Enter valid choice\n");
        }
        print_ds(ds);
    }

    return 0;
}