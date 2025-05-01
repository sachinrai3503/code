# https://leetcode.com/problems/maximum-binary-string-after-change
"""
You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations
 any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than
 binary string y if x's decimal representation is greater than y's decimal representation.

Example 1:
Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"

Example 2:
Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.

Constraints:
1 <= binary.length <= 105
binary consist of '0' and '1'.
"""

class Solution:

    # Not very fast
    def maximumBinaryString1(self, binary: str) -> str:
        last_0_index = None
        binary_len = len(binary)
        for i in range(binary_len):
            c = binary[i]
            if c=='1':
                continue
            else:
                if last_0_index is None:
                    last_0_index = i
                if last_0_index==i and (i!=(binary_len-1) and binary[i+1]=='0'):
                    last_0_index = i+1
                elif last_0_index!=i:
                    last_0_index+=1
        return ''.join(['0' if i==last_0_index else '1' for i in range(binary_len)])

    def maximumBinaryString(self, binary: str) -> str:
        first_0_index = binary.find('0')
        zero_count = binary.count('0')
        if zero_count == 0:
            return binary
        only_0_index = first_0_index + zero_count - 1
        return ''.join(['0' if i==only_0_index else '1' for i in range(len(binary))])