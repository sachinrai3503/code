//https://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/
//https://www.geeksforgeeks.org/sum-two-large-numbers/

#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <limits.h>

void printCharArr(char *ip, int s, int e){
    int i = s;
    for(;i<=e;i++){
        printf("%d",ip[i]);
    }
    printf("\n");
}

int multiply_digit(int a, int b){
    return a*b;
}

int multiply_num(char *num1, int len1, char num2_digit, int carry, char *op, int from){
    int i = len1-1;
    for(;i>=0;i--){
        int temp = multiply_digit(num1[i]-48,num2_digit-48);
        temp= temp + carry + op[from];
        op[from--]=(temp%10);
        carry = temp/10;
    }
    if(carry){
        op[from] = carry;
    }else{
        from++;
    }
    return from;
}

void multiply_nums(char *num1, int len1, char *num2, int len2){
    char *op = (char*)calloc(200,sizeof(char));
    int from = 199;
    int till = 200;
    int i = len2-1;
    for(;i>=0;i--){
        till = multiply_num(num1,len1,num2[i],0,op,from);
        // printCharArr(op,till,199);
        from--;
    }
    printCharArr(op,till,199);
}

void add_nums(char *num1, int len1, char *num2, int len2){
    char *op = (char*)calloc(200,sizeof(char));
    int k = 199;
    int carry = 0;
    int i = len1-1, j = len2-1;
    while(i>=0 || j>=0){
        int a = 0 , b = 0;
        if(i>=0) a = num1[i]-48;
        if(j>=0) b = num2[j]-48;
        op[k--] = (a+b+carry)%10;
        carry = (a+b+carry)/10;
        i--;
        j--;
    }
    if(carry){
        op[k--] = carry;
    }
    printCharArr(op,k+1,199);
}


int main(){
    char *num1 = "7777555511111111";
    int len1 = strlen(num1);
    char *num2 = "3332222221111";
    int len2 = strlen(num2);

    printf("%s\n",num1);
    printf("%s\n",num2);

    multiply_nums(num1,len1,num2,len2);
    add_nums(num1,len1,num2,len2);

    return 0;
}