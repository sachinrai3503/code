# # https://www.geeksforgeeks.org/minimum-salary-hike-for-each-employee-such-that-no-employee-feels-unfair/
# """
# Given an array arr[] of N positive integers which denotes the ratings of N employees,
#  the task is to find the minimum hike that should be raised for each employee,
#   such that no employee feels unfair.

#    An employee only knows the hike and rating of its neighbors 
#    i.e., on the left and right side of the employee.

# Note: The hikes are positive integers only and the ratings are always greater than zero.

# Input: arr[] = {5, 3, 4, 2, 1, 6}
# Output: 2 1 3 2 1 2
# """

# def get_last_increasing_index(ip_list, from_index):
#     """
#     Returns index of last num in the continuously increasing subarray.
#     """
#     if len(ip_list)<=1:
#         return 0
#     for i in range(from_index,len(ip_list)-1,1):
#         if ip_list
