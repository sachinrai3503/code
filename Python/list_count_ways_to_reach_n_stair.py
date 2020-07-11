#  https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
"""
There are n stairs, a person standing at the bottom wants to reach the top. 
The person can climb either 1 stair or 2 stairs at a time.
 Count the number of ways, the person can reach the top.

Input: n = 4
Output: 5
"""

# Sol. is generalized for n stair with m leaps

def get_ways_to_reach_top(n, m):
    count_list = [0]*(n+1)
    count = 0
    for i in range(n-1,-1,-1):
        count_list[i] = count
        if i+m>=n:
            count_list[i]+=1
        count+=count_list[i]
        if i+m<=n:
            count-=count_list[i+m]
    print(count_list)
    return count_list[0]

def main():
    n, m = 15, 5
    print('n =',n,'m =',m)
    print('No. of Ways =',get_ways_to_reach_top(n,m))

if __name__ == '__main__':
    main()