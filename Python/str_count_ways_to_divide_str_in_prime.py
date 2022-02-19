# https://www.geeksforgeeks.org/split-the-given-string-into-primes-digit-dp/
"""
Given numeric string str, the task is to count the number of ways the given string
 can be split, such that each segment is a prime number. Since the answer can be
  large, return the answer modulo 109 + 7. 

Note: A split that contains numbers with leading zeroes will be invalid and the
      initial string does not contain leading zeroes.

Examples: 
Input: str = “3175” 
Output: 3 
Explanation: 
There are 3 ways to split this string into prime numbers which are (31, 7, 5), 
 (3, 17, 5), (317, 5).

Input: str = “11373” 
Output: 6 
Explanation: 
There are 6 ways to split this string into prime numbers which are (11, 3, 7, 3),
 (113, 7, 3), (11, 37, 3), (11, 3, 73), (113, 73) and (11, 373). 
"""

# Have not handled the case for leading zeros

import math

def is_prime(num):
    if num<=1: return False
    sqr_root = math.ceil(math.sqrt(num)) + 1
    for i in range(2, sqr_root):
        if num%i == 0: return False
    return True

def count_ways_to_divide_in_prime_str(num_str):
    length = len(num_str)
    if length<=0: return -1
    dp = [0 for i in range(length)]
    for i in range(length-1, -1, -1):
        count = 0
        for j in range(i, length):
            t_num = int(num_str[i:j+1])
            if is_prime(t_num):
                count+= (1 if j==(length-1) else dp[j+1])
        dp[i] = count
    print(dp)
    return dp[0]

def main():
    num_str = '11373'
    print("ways =", count_ways_to_divide_in_prime_str(num_str))

if __name__ == '__main__':
    main()