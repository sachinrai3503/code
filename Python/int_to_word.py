# https://leetcode.com/problems/integer-to-english-words/
# https://www.geeksforgeeks.org/program-to-convert-a-given-number-to-words-set-2/
# https://www.geeksforgeeks.org/convert-number-to-words/
"""
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven 
         Thousand Eight Hundred Ninety One"
 
Constraints:
0 <= num <= 231 - 1
"""

class Solution:
    
    def __init__(self):
        self.place_list = ['','Hundred','Thousand','Million','Billion','Trillion']
        self.once_list = ['', 'One','Two','Three','Four','Five','Six','Seven','Eight',
                          'Nine','Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 
                          'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen','Nineteen']
        self.tens_list = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
                          'Eighty', 'Ninety']
    
    def to_word(self, num, flag):
        op = list()
        if num==0: return op
        a = num//100
        if a!=0:
            op.append(self.once_list[a])
            op.append(self.place_list[1])
        num=num%100
        if 0<num<20:
            op.append(self.once_list[num])
        else:
            b = num//10
            num = num%10
            if b!=0:      op.append(self.tens_list[b-2])
            if num!=0:    op.append(self.once_list[num])
        if flag!=0 :    op.append(self.place_list[flag+1])
        return op
    
    def numberToWords(self, num: int) -> str:
        if num==0: return 'Zero'
        op = list()
        flag = 0
        while num>0:
            t_op = self.to_word(num%1000,flag)
            op = t_op + op
            flag+=1
            num//=1000
        return ' '.join(op)