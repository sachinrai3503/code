# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# https://www.geeksforgeeks.org/subset-sum-problem-osum-space/
# https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
"""
Given a set of non-negative integers, and a value sum, determine if there is a
 subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

# Not a 100% correct sol to print all the unique subsets
def print_subsets(op, sum, subset_ele):
    if sum == 0:
        print(subset_ele)
        return
    if not op[sum]:
        print('No subset with sum=', sum)
        return
    for item in op[sum]:
        if (sum-item) in subset_ele: continue
        subset_ele.append(sum-item)
        print_subsets(op, item, subset_ele)
        subset_ele.pop()


def append(op_list, index, value):
    if op_list[index] == None:
        op_list[index] = list()
    op_list[index].append(value)


def find_subset_with_given_sum(ip_list, sum):
    op = [None]*(sum+1)
    for i in range(len(ip_list)-1, -1, -1):
        for j in range(sum, ip_list[i]-1, -1):
            if j == ip_list[i]:
                append(op, j, 0)
            elif op[j-ip_list[i]]:
                append(op, j, j-ip_list[i])
    print(op)
    print('All the subset with sum =', sum)
    print_subsets(op, sum, list())
    return op[sum]!=None


def main():
    ip_list = [2,2,2]
    sum = 4
    print('ip>>', ip_list)
    print('sum>>', sum)
    print('Subset present =', find_subset_with_given_sum(ip_list, sum))


if __name__ == '__main__':
    main()
