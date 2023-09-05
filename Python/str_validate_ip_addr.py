# https://leetcode.com/problems/validate-ip-address
# https://www.geeksforgeeks.org/program-to-validate-an-ip-address
"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP
 is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi
 cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid
 IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter 
 ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.

For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334"
  are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334"
  and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 
Constraints:
queryIP consists only of English letters, digits and the characters '.' and ':'.
"""

class Solution:

    def is_valid_IPv4(self, ip, ip_len) -> bool:
        dot_count = 0
        x, x_len = 0, 0
        i = 0
        while i<ip_len and dot_count<4:
            char = ip[i]
            if char=='.':
                if x_len==0: return False
                dot_count+=1
                x, x_len = 0, 0
            elif '0'<=char<='9':
                x = x*10 + int(char)
                x_len+=1
                if x==0 and (i!=(ip_len-1) and ip[i+1]!='.'): return False
                if x>255: return False
                # print(f'{x=}, {x_len=}')
            else: return False
            i+=1
        # print('ipv4', i, x, x_len)
        return i==ip_len and x_len>0 and dot_count==3

    def is_valid_IPv6(self, ip, ip_len) -> bool:
        colon_count = 0
        x_len = 0
        i = 0
        while i<ip_len and colon_count<8:
            char = ip[i]
            if char==':':
                if x_len==0: return False
                colon_count+=1
                x_len = 0
            elif ('0'<=char<='9') or ('a'<=char<='f') or ('A'<=char<='F'):
                x_len+=1
                if x_len>4: return False
            else: return False
            i+=1
        return i==ip_len and x_len>0 and colon_count==7

    def validIPAddress(self, queryIP: str) -> str:
        ip_len = len(queryIP)
        if self.is_valid_IPv4(queryIP, ip_len): return 'IPv4'
        if self.is_valid_IPv6(queryIP, ip_len): return 'IPv6'
        return 'Neither'