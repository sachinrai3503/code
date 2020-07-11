# https://www.geeksforgeeks.org/find-number-subarrays-even-sum/

def count_subarr_with_even_sum(ip_list):
    even_subarr_count = 0
    even_count, odd_count = 0, 0
    for num in ip_list:
        if num%2 == 0:
            even_count+=1
            even_subarr_count+=even_count
        else:
            temp = even_count
            even_count = odd_count
            odd_count = temp
            odd_count+=1
            even_subarr_count+=even_count
    return even_subarr_count

def main():
    ip_list = [1,2,2,2,2]
    print('ip =',ip_list)
    print('Sub arr with even count = ',count_subarr_with_even_sum(ip_list))

if __name__ == '__main__':
    main()

