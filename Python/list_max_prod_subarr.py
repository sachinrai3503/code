# https://www.geeksforgeeks.org/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/

INT_MIN = -999999999

def find_max_prod_sub_arr(ip_list):
    max_prod, s, e = INT_MIN, 0, -1
    t_p1, t_p2, t_s1, t_s2 = 1, 1, 0, -1
    flag_1st_neg = False
    for i in range(len(ip_list)):
        t_p1*=ip_list[i]
        if flag_1st_neg:
            t_p2*=ip_list[i]
        if t_p1 >= max_prod:
            max_prod = t_p1
            s = t_s1
            e = i
        if flag_1st_neg and t_p2 >= max_prod:
            max_prod = t_p2
            s = t_s2
            e = i
        if ip_list[i] == 0:
            flag_1st_neg = False
            t_s1, t_s2 = i+1, -1
            t_p1, t_p2 = 1, 1
        elif ip_list[i] < 0:
            flag_1st_neg = True
            t_s2 = i+1
    if max_prod == 0:
        s, e = 0, len(ip_list)-1
    print('max prod= ',max_prod, ' s=',s, ' e=',e)
    print('op= ', ip_list[s:e+1])

def main():
    ip_list = [-2,0,-1]
    print('ip= ',ip_list)
    find_max_prod_sub_arr(ip_list)

if __name__ == '__main__':
    main()
