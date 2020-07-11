# https://www.geeksforgeeks.org/trapping-rain-water/

INT_MIN = -999999999

def get_trapper_water_amount(ip_list):
    amount = 0
    max_bar_on_left, max_bar_on_right = INT_MIN, INT_MIN
    i, j = 0, len(ip_list)-1
    while i<j:
        if ip_list[i]<=ip_list[j]:
            if ip_list[i] < max_bar_on_left:
                amount+=(max_bar_on_left-ip_list[i])
            else:
                max_bar_on_left = ip_list[i]
            i+=1
        else:
            if ip_list[j] < max_bar_on_right:
                amount+=(max_bar_on_right-ip_list[j])
            else:
                max_bar_on_right = ip_list[j]
            j-=1
    return amount

def main():
    ip_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print('ip = ',ip_list)
    print('amount = ',get_trapper_water_amount(ip_list))

if __name__ == '__main__':
    main()
