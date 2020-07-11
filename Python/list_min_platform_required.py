# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station-set-2-map-based-approach/

"""
Given arrival and departure times of all trains that reach a railway station, 
the task is to find the minimum number of platforms required 
for the railway station so that no train waits.

We are given two arr which represent arrival & departure 
times of trains that stop.

Examples:

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Input: arr[] = {9:00, 9:40}
dep[] = {9:10, 12:00}
Output: 1
"""

def get_min_platform_sort(arr_list, dep_list):
    count, t_count = 0, 0
    i,j = 0, 0
    arr_list.sort()
    dep_list.sort()
    while i<len(arr_list) and j<len(dep_list):
        if arr_list[i]<=dep_list[j]:
            t_count+=1
            i+=1
        else:
            t_count-=1
            j+=1
        count = t_count if t_count>count else count
    if i!=len(arr_list):
        print('Invalid arrival timing given')
        return -1
    else:
        return count

def get_min_platform_map(arr_list, dep_list):
    count, t_count = 0, 0
    platform_map = [0 for i in range(2401)]
    for i in range(len(arr_list)):
        platform_map[arr_list[i]]+=1
        platform_map[dep_list[i]+1]-=1
    for num in platform_map:
        t_count+=num
        count = t_count if t_count>count else count
    return count

def main():
    arr_list = [10,20,40,40,45,50,70,80,90]
    dep_list = [20,30,50,50,50,90,80,100,120]
    print('arrival>',arr_list)
    print('depart>',dep_list)
    print('Count map method =>',get_min_platform_map(arr_list,dep_list))
    print('Count sort method =>',get_min_platform_sort(arr_list,dep_list))

if __name__ == '__main__':
    main()