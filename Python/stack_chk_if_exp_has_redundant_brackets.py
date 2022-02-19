# https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/
# https://www.interviewbit.com/problems/redundant-braces/
"""
Given a string of balanced expression, find if it contains a redundant 
parenthesis or not. 
A set of parenthesis are redundant if same sub-expression is surrounded by 
unnecessary or multiple brackets. Print ‘Yes’ if redundant else ‘No’.

Note: Expression may contain ‘+‘, ‘*‘, ‘–‘ and ‘/‘ operators.
 Given expression is valid and there are no white spaces present.

Example:

Input: 
((a+b))
(a+(b)/c)
(a+b*(c-d))

Output: 
Yes
Yes
No
"""

def is_paranthesis(c):
    if c=='(' or c==')':
        return True
    else:
        return False

def is_operator(op):
    if op=='*' or op=='/' or op=='+' or op=='-':
        return True
    return False

def get_priority(op):
    if op=='*' or op=='/':
        return 2
    if op=='+' or op=='-':
        return 1
    if op=='(' or op==')':
        return 0

def contains_redundant_paranthesis(ip_str):
    stck = list()
    for c in ip_str:
        if is_operator(c):
            while len(stck)>0 and get_priority(stck[-1])>get_priority(c):
                stck.pop()
            stck.append(c)
        elif c=='(':
            stck.append(c)
        elif c==')':
            is_redundant = True
            while stck[-1]!='(':
                is_redundant = False
                stck.pop()
            stck.pop()
            if is_redundant:
                return True
    return False

def main():
    ip_str = '(a-)b'
    print('Ip>',ip_str)
    print('Has redundant paranthesis=',contains_redundant_paranthesis(ip_str))

if __name__=='__main__':
    main()