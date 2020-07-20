# https://www.geeksforgeeks.org/remove-invalid-parentheses/
"""
An expression will be given which can contain open and close parentheses 
and optionally some characters, No other operator will be there in string. 
We need to remove minimum number of parentheses to make the input string valid. 

If more than one valid output are possible removing same number of parentheses 
then print all such output.

Examples:
Input  : str = “()())()” -
Output : ()()() (())()

Input  : str = (v)())()
Output : (v)()()  (v())()
"""
# C based sol using que @remove_invalid_paranthesis.c

from collections import deque

def is_valid_exp(ip_str):
    count = 0
    for char in ip_str:
        if char=='(':
            count+=1
        elif char==')':
            count-=1
        if count<0:
            return False
    if count>0:
        return False
    return True

def is_paranthesis(c):
    if c == ')' or c =='(':
        return True
    return False

def check_and_insert(unique_exp_set, que, ip_str):
    if not unique_exp_set.__contains__(ip_str):
        unique_exp_set.add(ip_str)
        que.append(ip_str)

def get_valid_exp(ip_str):
    min_bracket_removed = 0
    result_list = list()
    unique_exp_set = set()
    que = deque()
    null_str = 'NULL'
    check_and_insert(unique_exp_set,que,ip_str)
    que.append(null_str)
    got_valid_exp = False
    while not len(que)==0 and (que[0] is not null_str):
        print(que)
        while not len(que)==0 and (que[0] is not null_str):
            temp = que.popleft()
            if is_valid_exp(temp):
                got_valid_exp = True
                result_list.append(temp)
            else:
                for i in range(len(temp)):
                    if not is_paranthesis(temp[i]):
                        continue
                    next_exp = temp[0:i] + temp[i+1:len(temp)]
                    check_and_insert(unique_exp_set,que,next_exp)
        que.popleft()
        min_bracket_removed+=1
        que.append(null_str)
        if got_valid_exp:
            return min_bracket_removed-1, result_list
    return min_bracket_removed-1, result_list

def main():
    ip_str = '(v)(((v)'
    print('Ip=>',ip_str)
    min_bracket_removed, result_list = get_valid_exp(ip_str)
    print('Min. bracket removed =',min_bracket_removed)
    print(result_list)

if __name__=='__main__':
    main()