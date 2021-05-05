// https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
/*
There are 2 sorted arrays A and B of size n each.

Write an algorithm to find the median of the array obtained after merging the
  above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)). 

arr1 = [1, 12, 15, 26, 38]
arr2 = [2 , 13, 17, 30 ,45]
op = 16 // (15+17)/2
*/

#include <stdio.h>
#include <limits.h>

void print_arr(int *ip, int length){
  int i = 0;
  for(;i<length;i++){
    printf("%d ",ip[i]);
  }
  printf("\n");
}

int get_min(int a, int b){
  if(a<b) return a;
  return b;
}

int get_max(int a, int b){
  if(a>b) return a;
  return b;
}

int find_median(int *ip, int s, int e){
  int length = e-s+1;
  if(length==0) return INT_MIN;
  int mid = s + (e-s)/2;
  if(length%2) return ip[mid];
  return (ip[mid]+ip[mid+1])/2;
}

int get_median_log_n(int *ip1, int *ip2, int length){
  if(length<1) return INT_MIN;
  int s1 = 0, e1 = length-1;
  int s2 = 0, e2 = length-1;
  while((e1-s1)>1 && (e2-s2)>1){
    printf("s1=%d e1=%d s2=%d e2=%d\n",s1,e1,s2,e2);
    int tlen = e1-s1+1;
    int m1 = find_median(ip1, s1, e1);
    int m2 = find_median(ip2, s2, e2);
    printf("m1=%d m2=%d\n",m1, m2);
    if(m1==m2) return m1;
    if(m1<m2){
      s1 = (e1+s1)/2;
      e2 = (e2+s2)/2;
      if(tlen%2==0){
        e2 = e2 + 1;
      }
    }else{
      e1 = (e1+s1)/2;
      s2 = (e2+s2)/2;
      if(tlen%2==0){
        e1 = e1 + 1;
      }
    }
    printf("s1=%d e1=%d s2=%d e2=%d\n",s1,e1,s2,e2);
  }
  if(s1==e1 && s2==e2) return (ip1[s1]+ip2[s2])/2;
  return (get_max(ip1[s1], ip2[s2]) + get_min(ip1[e1], ip2[e2]))/2;
}

int main(){
  int ip1[] = {0, 1, 3, 4};
  int ip2[] = {0,2,6,7};
  int l1 = sizeof(ip1)/sizeof(ip1[0]);
  int l2 = sizeof(ip2)/sizeof(ip2[0]);
  print_arr(ip1, l1);
  print_arr(ip2, l2);

  printf("Median = %d\n", get_median_log_n(ip1, ip2, l1));

  return 0;
}