# https://www.geeksforgeeks.org/minimum-steps-to-make-the-product-of-the-array-equal-to-1/
"""
Given an array arr[] containing N integers. In one step, any element of the
array can either be increased or decreased by one. The task is to find minimum
steps required such that the product of the array elements becomes 1.

Examples:

Input: arr[] = { -2, 4, 0 }
Output: 5
We can change -2 to -1, 0 to -1 and 4 to 1.
So, a total of 5 steps are required to update the elements
such that the product of the final array is 1.

Input: arr[] = { -1, 1, -1 }
Output: 0
"""


def get_min(a, b):
    return a if a < b else b


def get_diff(a, b):
    if a > b:
        return a-b
    return b-a


def get_min_step(ip_list):
    prev_cost_1, prev_cost_minus_1 = None, None
    length = len(ip_list)
    for i in range(length-1, -1, -1):
        num = ip_list[i]
        # cost to make num 1 and -1.
        t_cost_1, t_cost_minus_1 = get_diff(1, num), get_diff(-1, num)
        if i < length-1:
            # cost to get product as 1
            p = get_min(t_cost_1+prev_cost_1, t_cost_minus_1+prev_cost_minus_1)
            # cost to get product as -1
            q = get_min(t_cost_1+prev_cost_minus_1, t_cost_minus_1+prev_cost_1)
            t_cost_1, t_cost_minus_1 = p, q
        prev_cost_1, prev_cost_minus_1 = t_cost_1, t_cost_minus_1
        # print(prev_cost_1, prev_cost_minus_1)
    return prev_cost_1


def main():
    ip_list = [3, 7, 0, 5, -8, -3, 2, 9, 4]
    print('ip>>', ip_list)
    print('Min cost to make prod = 1 is ', get_min_step(ip_list))


if __name__ == '__main__':
    main()
