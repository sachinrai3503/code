# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

"""
Given a set of integers, 
 the task is to divide it into two sets S1 and S2 such that the absolute
difference between their sums is minimum. 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11  
"""

def get_sum(ip_list):
    sum = 0
    for num in ip_list:
        sum+=num
    return sum

def get_min(a, b):
    if a<b:
        return a
    else:
        return b

def get_diff(a, b):
    if a>b:
        return a-b
    else:
        return b-a

def get_min_diff_DP(ip_list):
    """
    Returns min diff between 2 subset of the arr.
    """
    if len(ip_list)==0:
        print('Invalid')
        return -999999999
    list_sum = get_sum(ip_list)
    op_length = (list_sum//2) + 1
    op_list = [[0]*op_length,[0]*op_length]
    for i in range(len(ip_list)-1,-1,-1):
        list_sum-=ip_list[i]
        cur_row = i%2
        prev_row = 1 if cur_row==0 else 0
        # print('cur_row =',cur_row,'prev_row =',prev_row)
        s1, s2 = 0, list_sum
        while s1<=s2:
            # print('s1=',s1,'s2=',s2)
            ts1_1, ts2_1 = s1+ip_list[i], s2
            ts1_2, ts2_2 = s1, s2+ip_list[i]
            if i==len(ip_list)-1:
                op_list[cur_row][s1] = get_min(get_diff(ts1_1,ts2_1),get_diff(ts1_2,ts2_2))
            else:
                op_list[cur_row][s1] = get_min(op_list[prev_row][get_min(ts1_1,ts2_1)],\
                        op_list[prev_row][get_min(ts1_2,ts2_2)])
            s1+=1
            s2-=1
            # print('op_list',op_list)
    return op_list[0][0]

def main():
    ip_list = [40,20,60,10,50,30]
    print('ip =',ip_list)
    print('Diff =',get_min_diff_DP(ip_list))

if __name__ == '__main__':
    main()

