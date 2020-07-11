# https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/
"""
Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 } 
          { 5 , 5 }
"""

def get_sum(ip_list):
    sum = 0
    for num in ip_list:
        sum+=num
    return sum

def split_arr_in_equal_sum_subarr(ip_list):
    # total_sum = get_sum(ip_list)
    total_sum = sum(ip_list)
    left_sum = 0
    index = -1
    for i in range(len(ip_list)):
        left_sum+=ip_list[i]
        right_sum = total_sum-left_sum
        if left_sum==right_sum:
            index = i
            break
    else:
        print('Not possible')
        return
    print(ip_list[0:index+1],ip_list[index+1:len(ip_list)])

def main():
    ip_list = [4,1,3,2]
    print('ip=>',ip_list)
    split_arr_in_equal_sum_subarr(ip_list)

if __name__ == '__main__':
    main()