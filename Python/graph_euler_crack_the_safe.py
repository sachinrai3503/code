# https://leetcode.com/problems/cracking-the-safe
"""
There is a safe protected by a password. The password is a sequence of n digits 
 where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence,
 it checks the most recent n digits that were entered each time you type a digit.

For example, the correct password is "345" and you enter in "012345":
After typing 0, the most recent 3 digits is "0", which is incorrect.
After typing 1, the most recent 3 digits is "01", which is incorrect.
After typing 2, the most recent 3 digits is "012", which is incorrect.
After typing 3, the most recent 3 digits is "123", which is incorrect.
After typing 4, the most recent 3 digits is "234", which is incorrect.
After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
Return any string of minimum length that will unlock the safe at some point of entering it.

Example 1:
Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.

Example 2:
Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the safe.

Constraints:
1 <= n <= 4
1 <= k <= 10
1 <= kn <= 4096
"""

from sys import maxsize

class Solution:

    def generate_pass_dfs(self, n, k, op, visited, count):
        # print(f'{op=} {visited=} {count=}')
        if count==self.possible_count:
            # print(f'till here')
            if len(op)<self.password_len:
                self.password = ''.join(op)
                self.password_len = len(op)
                # print(f'till here 1 {op=} {self.password=}')
        else:
            for i in range(k):
                op.append(str(i))
                last_pass = ''.join(op[-n:])
                if last_pass not in visited:
                    if len(op)>=n:
                        visited.add(last_pass)
                        self.generate_pass_dfs(n, k, op, visited, count+1)
                        visited.remove(last_pass)
                    else:
                        self.generate_pass_dfs(n, k, op, visited, count)
                op.pop()


    # Will time out
    def crackSafe_dfs(self, n: int, k: int) -> str:
        self.possible_count = k**n
        self.password = None
        self.password_len = maxsize
        print(f'{self.possible_count=}')
        self.generate_pass_dfs(n, k, list(), set(), 0)
        return self.password

    def hierholzer_circuit(self, start, seen, circuit):
        for i in map(str, range(self.k)):
            v = start + i
            if v not in seen:
                seen.add(v)
                self.hierholzer_circuit(v[1:], seen, circuit)
                circuit.append(i)

    # Uses Euler circuit print logic - Hierholzer’s algo. Given graph will always have Euler circuit
    # Graph vertex count = k**(n-1)
    # n = 3, k = 2
    # Vertex = [00, 01, 10, 11]
    # Each vertex will have edges = [0, 1] # [0, k-1]
    # Vertex + edge == state eg. 00 + 0 = 000
    # Transition from vertex 00 ->(with edge x) -> (0)0x (use last n-1 chars to know the landing vertex) 
    def crackSafe(self, n: int, k: int) -> str:
        self.n = n
        self.k = k
        start = '0'*(n-1)
        circuit = list()
        self.hierholzer_circuit(start, set(), circuit)
        # print(f'{circuit=}')
        return ''.join(circuit) + start