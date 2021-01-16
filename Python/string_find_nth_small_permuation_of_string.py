# https://www.geeksforgeeks.org/lexicographically-n-th-permutation-string
# https://www.geeksforgeeks.org/find-n-th-lexicographically-permutation-string-set-2
# https://leetcode.com/problems/permutation-sequence/

# Note - Leetcode one is same logic but without repeation of char allowed.

"""
Given a string of length m containing lowercase alphabets only. We need to find
 the n-th permutation of string lexicographically.

Examples:

Input: str[] = "abc", n = 3
Output: Result = "bac"
All possible permutation in sorted order: abc, acb, bac, bca, cab, cba

Input: str[] = "aba", n = 2
Output: Result = "aba"
All possible permutation in sorted order: aab, aba, baa
"""

def get_all_factorial(n):
    op = [1]*(n+1)
    i = 1
    while i<=n:
        op[i] = op[i-1]*i
        i+=1
    return op

def get_freq(ip_str):
    freq_list = [0]*(26)
    for c in ip_str:
        freq_list[ord(c)-97]+=1
    return freq_list

class Solution:
    # This won't handle repeatition of chars
    def getPermutation(self, n: int, k: int) -> str:
        length = n
        fact_list = get_all_factorial(length)
        if k<=0 or k>fact_list[-1]: return None
        op = list()
        ele_list = [str(i) for i in range(1, n+1)]
        # print(ele_list)
        while k>1:
            prem_with_len_minus_1 = fact_list[length-1]
            quo, rem = k//prem_with_len_minus_1, k%prem_with_len_minus_1
            quo = quo + (1 if rem!=0 else 0)
            op.append(ele_list.pop(quo-1))
            # print(ele_list)
            length-=1
            k = k - ((quo-1)*prem_with_len_minus_1)
        # print(ele_list)
        op.extend(ele_list)
        return ''.join(op)
    
    # This will handle repeatition of chars
    def getPermutation2(self, ip_str, k):
        op = list()
        digit_count = len(ip_str)
        freq_list = get_freq(ip_str)
        fact_list = get_all_factorial(digit_count)
        denominator = 1
        for freq in freq_list:
            denominator*=fact_list[freq]
        if k<=0 or k>(fact_list[-1]//denominator): return None
        # print(freq_list)
        # print(fact_list)
        # print(digit_count)
        # print(denominator)
        length = digit_count
        while k>1:
            i = 0
            while i<len(freq_list):
                if freq_list[i]>0:
                    t_permut_count = (fact_list[length-1]*freq_list[i])//denominator
                    if t_permut_count<k:
                        k-=t_permut_count
                    else:
                        op.append(chr(i+97))
                        denominator//=freq_list[i]
                        freq_list[i]-=1
                        length-=1
                        break
                i+=1
        for i in range(len(freq_list)):
            while freq_list[i]>0:
                op.append(chr(i+97))
                freq_list[i]-=1
        return ''.join(op)


def main():
    sol = Solution()
    ip_str = 'aabbcddef'
    k = 45359
    print('ip>',ip_str)
    print('k=',k)
    kth_small_permuatation = sol.getPermutation2(ip_str, k)
    print('Kth small permuatation =',kth_small_permuatation)

if __name__ == '__main__':
    main()