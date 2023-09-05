# https://leetcode.com/problems/restore-ip-addresses
"""
A valid IP address consists of exactly four integers separated by single dots. 
 Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
 "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that
 can be formed by inserting dots into s. You are not allowed to reorder or remove any
 digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
1 <= s.length <= 20
s consists of digits only.
"""

from typing import List

class Solution:

    def get_all_ip(self, s, s_len, i, dot_count, cur_op, op):
        if i>=s_len: return
        if dot_count==3:
            if i!=(s_len-1) and s[i]=='0': return
            num = 0
            while i<s_len:
                num=num*10 + int(s[i])
                if num>255: return
                i+=1
            cur_op.append(str(num))
            op.append('.'.join(cur_op))
            cur_op.pop()
        elif dot_count<3:
            if s[i]=='0':
                cur_op.append(s[i])
                self.get_all_ip(s, s_len, i+1, dot_count+1, cur_op, op)
                cur_op.pop()
            else:
                num = 0
                j = 0
                while j<3 and i<s_len:
                    num=num*10 + int(s[i])
                    if num>255: break
                    cur_op.append(str(num))
                    self.get_all_ip(s, s_len, i+1, dot_count+1, cur_op, op)
                    cur_op.pop()
                    j+=1
                    i+=1

    def restoreIpAddresses(self, s: str) -> List[str]:
        s_len = len(s)
        op = list()
        cur_op = list()
        self.get_all_ip(s, s_len, 0, 0, cur_op, op)
        return op