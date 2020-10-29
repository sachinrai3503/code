#include <stdio.h>
#include <malloc.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_LIS(int *ip, int length, int *lis_index, int from){
    while(from!=-1){
        printf("%d ",ip[from]);
        from = lis_index[from];
    }
    printf("\n");
}

int LIS_DP(int *ip, int length){
    int *lis_len = (int*)calloc(length,sizeof(int));
    int *lis_index = (int*)calloc(length,sizeof(int));
    int max_len = 0;
    int from = -1;
    int i = length-1;
    for(;i>=0;i--){
        int t_len = 0;
        int t_index = -1;
        int j = i+1;
        for(;j<length;j++){
            if(ip[j]>ip[i] && lis_len[j]>t_len){
                t_len = lis_len[j];
                t_index = j;
            }
        }
        lis_len[i] = t_len + 1;
        lis_index[i] = t_index;
        if(lis_len[i]>max_len){
            max_len = lis_len[i];
            from = i;
        }
    }
    print_LIS(ip,length,lis_index,from);
    return max_len;
}

typedef struct {
    int *arr;
    int s, e;
}lis_info;

lis_info* init_lis_info(int length){
    lis_info *info = (lis_info*)malloc(sizeof(lis_info));
    if(info){
        info->arr = (int*)calloc(length, sizeof(int));
        info->s = 0;
        info->e = -1;
    }
    return info;
}

void extend_info(lis_info *info, int index, int data){
    if(info){
        if(info->e<index){
            info->e = index;
        }
        info->arr[index] = data;
    }
}

int get_floor(int *ip, lis_info *info, int data){
    int _floor = -1;
    int s = info->s;
    int e = info->e;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(ip[info->arr[mid]]<data){
            _floor = mid;
            s = mid+1;
        }else{
            e = mid-1;
        }
    }
    return _floor;
}

int LIS_NLOGN(int *ip, int length){
    lis_info *info = init_lis_info(length);
    int *op = (int*)calloc(length,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        int _floor = get_floor(ip,info,ip[i]);
        if(_floor==-1){
            op[i] = -1;
        }else{
            op[i] = info->arr[_floor];
        }
        extend_info(info,_floor+1,i);
    }
    // Would print LIS in reverse.
    if(info->e!=-1)
        print_LIS(ip,length,op,info->arr[info->e]);
    return info->e+1;
}

int main(){
    int ip[] = {2, 5, 3, 7, 11, 8, 10, 13, 6};
    int length = sizeof(ip)/sizeof(ip[0]);

    printf("IP >");
    print_arr(ip,length);
    printf("DP Len = %d\n",LIS_DP(ip,length));
    printf("NLOGN Len = %d\n",LIS_NLOGN(ip,length));

    return 0;
}