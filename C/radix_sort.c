// https://www.geeksforgeeks.org/radix-sort/
/*
Radix Sort - 

We saw in counting sort how to sort an array of size n if all elements are in the range 1 to k,
 in 0(n+k) time. What if the elements vary from 1 to n2. Counting sort will take O(n2) 
 time in this case. Can we sort such an array in linear time? Radix sort comes to our rescue.

Radix sort is a very interesting sorting method. It is used to sort data by grouping elements
 on the basis of digits that share the same significant position. That is, we sort digit
 by digit, from the least to the most significant digit. Counting sort is used as a part 
 of radix sort.

Description
As we can see in the image, we sort the numbers on the basis of the least significant
 digit to the most significant digit (in base b).

Suppose the numbers vary from 1 to k. The number of digits in base b is O(logb(k)).
 We use counting sort to sort the numbers on the basis of these digits 
 (we know that the digits range from 0 to b-1 in time O(n+b).
 Thus the overall complexity is O((n+b)*logb(k)).

Note that if k = n^2, we choose b = n and we get complexity O(n)! 

Algorithm
Step 1: Find the maximum possible most significant digit. Call this D. 
        Note that D = logb(k) where b is the chosen base and k is the maximum value
        that the numbers of the array can take. 

Step 2: Iterate from the least significant to the most significant digit (i = 0 to D).

Step 3: In each iteration sort the numbers in the given array on the basis of their
        digit at position i. Note that the digits vary from 0 to b-1 since we have
        represented each number in base b.

Step 4: Make sure that for numbers that have the same digit at position i, their 
        relative position remains the same. (Think why?)

Step 5: The array we obtain finally is sorted.
*/

#include <stdio.h>
#include <malloc.h>

void print_arr(int *a, int length){
    int i = 0;
    for(i=0;i<length;i++){
        printf("%d ",a[i]);
    }
    printf("\n");
}

/*
Radix sort assumes ip has number in range (1, (length*length)) or (1, length^x) so 
 that we can take base of length  
b = base
k = max num
*/
void radixSort(int *ip, int length, int b, int k){
    int i = 1;
    for(;i<=k;i*=b){
        int *count = (int*)calloc(b, sizeof(int));

        // Taking the count of least sig. digit in base b representation of ip[j]
        int j = 0;
        for(;j<length;j++){
            count[(ip[j]/i)%b]++;
        }
        // This will be needed when we use counting sort technique to arrange the 
        // element back to arr.
        for(j=1;j<b;j++){
            count[j]+=count[j-1];
        }
        // print_arr(count, b);

        // Arranging the elements as per the least sig. digit
        int *t_arr = (int*)calloc(length, sizeof(int));
        for(j=length-1;j>=0;j--){
            t_arr[count[(ip[j]/i)%b]-1] = ip[j];
            count[(ip[j]/i)%b]--;
            // print_arr(t_arr, length);
        }

        // print_arr(count, b);
        for(j=0;j<length;j++){
            ip[j] = t_arr[j];
        }
        // printf("=============================\n");
    }
}

int main(){
    // Note if arr length is n then have the max element of type n^c. This helps in 
    // taking base as n. Here c = 2 is assumed.
	int a[] = {99,5,1,79,100,10,3,56,66,89,166,50,376,400,375,16,275,194,333,399};
    int n = sizeof(a)/sizeof(a[0]);
    print_arr(a, n);
	radixSort(a,n,n,n*n);
	print_arr(a, n);
    return 0;
}
