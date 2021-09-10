# https://leetcode.com/problems/solve-the-equation/
"""
Solve a given equation and return the value of 'x' in the form of a string "x=#value".
The equation contains only '+', '-' operation, the variable 'x' and its coefficient.
You should return "No solution" if there is no solution for the equation, or
 "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of
 'x' is an integer.

Example 1:
Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:
Input: equation = "x=x"
Output: "Infinite solutions"

Example 3:
Input: equation = "2x=x"
Output: "x=0"

Example 4:
Input: equation = "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:
Input: equation = "x=x+2"
Output: "No solution"

Constraints:
3 <= equation.length <= 1000
equation has exactly one '='.
equation consists of integers with an absolute value in the range [0, 100]
 without any leading zeros, and the variable 'x'.
"""

def get_coeff(num, last_operator):
    if last_operator=='+': return num
    return -1*num

def evaluate(values , exp):
    last_operator = '+'
    t_num = 0
    length = len(exp)
    i = 0
    while i<length:
        if exp[i]=='x':
            t_num = 1 if (i==0 or exp[i-1]=='+' or exp[i-1]=='-') else t_num
            values[0] = values[0] + get_coeff(t_num, last_operator)
            last_operator = exp[i+1] if i!=(length-1) else '+'
            i+=2
            t_num=0
        elif exp[i]=='+' or exp[i]=='-':
            values[1] = values[1] + get_coeff(t_num, last_operator)
            last_operator = exp[i]
            i+=1
            t_num=0
        else:
            t_num = t_num*10 + (ord(exp[i])-48)
            i+=1
    if t_num!=0:
        values[1] = values[1] + get_coeff(t_num, last_operator)
    
class Solution:
    def solveEquation(self, equation: str) -> str:
        # values[0] = x value, values[1] = coeff
        values = [0, 0]
        exp1, exp2 = equation.split('=')
        evaluate(values, exp1)
        values[0], values[1] = values[0]*-1, values[1]*-1
        evaluate(values, exp2)
        if values[0]==0 and values[1]!=0: return "No solution"
        elif values[0]==0 and values[1]==0: return 'Infinite solutions'
        else:
            return 'x='+str((values[1]*-1)//values[0])