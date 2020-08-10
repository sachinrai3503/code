# https://www.geeksforgeeks.org/dice-throw-dp-30/
"""
Given n dice each with m faces, numbered from 1 to m, 
find the number of ways to get sum X. 

X is the summation of values on each face when all the dice are thrown.

Input : m=4 n=2 x=4
Output : 3

Input : m=6 n=3 x=12
Output : 25
"""

def count_ways(n, m, x):
    if n<=0 or m<=0 or x<=0:
        print('Invalid input')
        return 0
    op_list = [[0]*x,[0]*x]
    for i in range(n-1,-1,-1):
        cur_row = i%2
        prev_row= 1 if cur_row==0 else 0
        prev_count = 0 # Count of ways to get sum x with n-1 dice.
        for j in range(x):
            if i==n-1:
                if j<m:
                    op_list[cur_row][j] = 1
            else:
                op_list[cur_row][j] = prev_count
                prev_count+=op_list[prev_row][j]
                if j-m>=0:
                    prev_count-=op_list[prev_row][j-m]
    print(op_list)
    return op_list[0][x-1]

def main():
    n, m, x = 3, 4, 5
    print('Ways =',count_ways(n,m,x))

if __name__ == '__main__':
    main()