# https://www.geeksforgeeks.org/longest-subsegment-1s-formed-changing-k-0s/
# https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/

def get_longest_subseq_by_flipping_m_0s(ip_list, max_zero):
    max_len, start, end = 0, 0, -1
    t_start, t_end = 0, 0
    zero_count = 0
    list_length = len(ip_list)
    while t_end < list_length:
        if ip_list[t_end] == 0:
            zero_count+=1
        while zero_count>max_zero:
            if ip_list[t_start] == 0:
                zero_count-=1
            t_start+=1
        if t_end-t_start+1 > max_len:
            max_len = t_end - t_start + 1
            start = t_start
            end = t_end
        t_end+=1
    print('Max sub seq of 1 = ',ip_list[start:end+1])
    print('Length of sub seq = ',max_len)

def main():
    ip_list = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    print('ip = ',ip_list)
    i = 0
    while i <= len(ip_list):
        print("Max zero flip allowed = ",i)
        get_longest_subseq_by_flipping_m_0s(ip_list,i)
        i+=1
        print('---')

if __name__ == '__main__':
    main()
