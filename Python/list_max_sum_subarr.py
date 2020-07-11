# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

INT_MIN = -999999999

def find_max_sum_subarr(ip_list):
    max_sum, s, e = INT_MIN, 0, -1
    t_sum, t_s = 0, 0
    for i in range(len(ip_list)):
        t_sum+=ip_list[i]
        if t_sum >= max_sum:
            max_sum = t_sum
            s = t_s
            e = i
        if t_sum < 0:
            t_sum = 0
            t_s = i+1
    print('Sum = ',max_sum,' s= ',s, ' e=',e)
    print(ip_list[s:e+1])

def main():
    ip_list = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print('ip =',ip_list)
    find_max_sum_subarr(ip_list)

if __name__ == '__main__':
    main()