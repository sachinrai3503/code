# https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/

INT_MIN = -9999999999

def sort(ip_list):
    for i in range(len(ip_list)):
        min = i
        for j in range(i+1,len(ip_list)):
            if ip_list[j] < ip_list[min]:
                min = j
        temp = ip_list[min]
        ip_list[min] = ip_list[i]
        ip_list[i] = temp

def mean(ip_list):
    if len(ip_list)==0:
         return -99999999999
    return sum(ip_list)/len(ip_list)

def median(ip_list):
    if len(ip_list)==0:
         return -99999999999
    sort(ip_list)
    length = len(ip_list)
    if length%2 == 0:
        return (ip_list[length//2-1] + ip_list[length//2])/2
    else:
        return ip_list[length//2]

def mode(ip_list):
    if len(ip_list)==0:
         return -99999999999
    max_num_count, max_occ_num = 0, INT_MIN
    num_count_dict = dict()
    for num in ip_list:
        if num_count_dict.__contains__(num):
            num_count_dict[num] = num_count_dict[num] + 1 
        else:
            num_count_dict[num] = 1
        if num_count_dict[num] > max_num_count:
            max_occ_num = num
            max_num_count = num_count_dict[num]
    print('=======>>',num_count_dict)
    return max_occ_num

def main():
    ip_list = [1, 2, 3, 4, 5, 5]
    print('ip=',ip_list)
    print('Mean = ',mean(ip_list))
    print('Mode = ',mode(ip_list))
    print('Median = ',median(ip_list))

if __name__ == '__main__' :
    main()
