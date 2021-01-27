// https://www.geeksforgeeks.org/partition-given-string-manner-ith-substring-sum-1th-2th-substring/
/*
Partition given string in such manner that i’th substring is sum of (i-1)’th 
 and (i-2)’nd substring.

Examples:
Input : "11235813"
Output : ["1", "1", "2", "3", "5", "8", "13"]

Input : "1111223"
Output : ["1", "11", "12", "23"]

Input : "1111213"
Output : ["11", "1", "12", "13"]

Input : "11121114"
Output : []
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

void print_op(char *ip, int length, int *op, int k){
    int j = 0;
    int i = 0;
    for(;i<length;i++){
        printf("%c",ip[i]);
        if(i==op[j]){
            printf(" ");
            j++;
        }
    }
    printf("\n");
}

void print_partition(char *ip, int length, int i, int a, int b, int dig_a, 
                     int dig_b, int last_found_flag, int *op, int k){
    if(i==length && last_found_flag==1){
        print_op(ip, length, op, k);
        return;
    }else if(i==length) return;
    if(a==-1 || b==-1){
        int t_num = 0;
        int t_i = i;
        for(;t_i<length;t_i++){
            t_num = t_num*10 + (ip[t_i]-48);
            op[k] = t_i;
            if(a==-1){
                print_partition(ip,length,t_i+1,t_num,b,t_i-i+1,dig_b,0,op,k+1);
            }else{
                print_partition(ip,length,t_i+1,a,t_num,dig_a,t_i-i+1,0,op,k+1);
            }
        }
    }else{
        int dig_c_1 = get_max(dig_a, dig_b);
        int dig_c_2 = dig_c_1 + 1;
        int t_c_1 = 0, t_c_2 = 0;
        int t_num = 0;
        int t_i = i;
        for(;t_i<length && t_i<i+dig_c_2;t_i++){
            t_num = t_num*10 + (ip[t_i]-48);
            if(t_i==i+dig_c_1-1) t_c_1 = t_num;
            else if(t_i==i+dig_c_2-1) t_c_2 = t_num;
        }
        if(a+b==t_c_1){
            op[k] = i+dig_c_1-1;
            print_partition(ip,length,i+dig_c_1,b,t_c_1,dig_b,dig_c_1,1,op,k+1);
        }else if(a+b==t_c_2){
            op[k] = i+dig_c_2-1;
            print_partition(ip,length,i+dig_c_2,b,t_c_2,dig_b,dig_c_2,1,op,k+1);
        }
    }
}

int main(){
    char *ip = "101020";
    int length = strlen(ip);
    printf("ip=%s\n",ip);
    int *op = (int*)calloc(length,sizeof(int));
    print_partition(ip,length,0,-1,-1,0,0,0,op,0);
    return 0;
}