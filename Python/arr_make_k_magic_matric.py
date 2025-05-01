# https://leetcode.com/discuss/interview-question/341295/Google-or-Online-Assessment-2019-or-Fill-Matrix
# https://www.magischvierkant.com/two-dimensional-eng/4x4/explanation/#:~:text=A%20pure%20magic%204x4%20square,always%20give%20the%20same%20result

"""
Given a NxN matrix. Fill the integers from 1 to n*n to this matrix that makes the sum of each row, each column and 
 the two diagonals equal.

Example 1:
Input: n = 2
Output: null
Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.

Example 2:
Input: n = 3
Output:
[[8, 3, 4],
 [1, 5, 9],
 [6, 7, 2]]
Explanation: We need to fill [1, 2, 3... 9] into a 3x3 matrix. This is one way to do it
Each row [8, 3, 4] [1, 5, 9] [6, 7, 2] sum is 15.
Each column [8, 1, 6] [3, 5, 7] [4, 9, 2] sum is 15.
The two diagonals [8, 5, 2] [4, 5, 6] sum is 15.
"""

from regex import R


class MagicSquare:
    def __init__(self, n):
        self.n = n
        self.s, self.e = 1, n**2
        self.matrix = [[None for j in range(n)] for i in range(n)]
        self.expected_sum = ((self.e + 1)*n)//2
        self.row_sum = [0 for i in range(n)]
        self.col_sum = [0 for i in range(n)]
        self.diagonal_sum = [0, 0]
    
    def is_valid(self, i, j):
        if i<0 or i>=self.n or j<0 or j>=self.n: return False
        return True

    def is_sqaure_matrix(self):
        for i in range(self.n):
            if self.row_sum[i]!=self.expected_sum: return False
            if self.col_sum[i]!=self.expected_sum: return False
        if self.diagonal_sum[0]!=self.expected_sum or self.diagonal_sum[1]!=self.expected_sum:
            return False
        return True

    def _generate_matrix(self, i, j, visited):
        # print(f'{i=} {j=} {visited=}')
        if i==(self.n) and j==0:
            print(f"{self.matrix} {self.col_sum} {self.row_sum} {self.diagonal_sum}")
            return True if self.is_sqaure_matrix() else False
        # if not self.is_valid(i, j): return False
        for num in range(self.s, self.e+1):
            if num not in visited:
                self.row_sum[i]+=num
                self.col_sum[j]+=num
                if i==j:
                    self.diagonal_sum[0]+=num
                if (i+j)==(self.n-1):
                    self.diagonal_sum[1]+=num
                if not (self.row_sum[i]>self.expected_sum or \
                    self.col_sum[j]>self.expected_sum or \
                    self.diagonal_sum[0]>self.expected_sum or\
                    self.diagonal_sum[1]>self.expected_sum):
                    visited.add(num)
                    self.matrix[i][j] = num
                    if j==(self.n-1):
                        if self._generate_matrix(i+1, 0, visited):
                            return True
                    else:
                        if self._generate_matrix(i, j+1, visited):
                            return True
                    visited.remove(num)
                self.row_sum[i]-=num
                self.col_sum[j]-=num
                if i==j:
                    self.diagonal_sum[0]-=num
                if (i+j)==(self.n-1):
                    self.diagonal_sum[1]-=num
            # print(f'{self.row_sum=} {self.col_sum=} {self.diagonal_sum=}')
        return False
        

    def get_matrix(self):
        visited = set()
        if self._generate_matrix(0, 0, visited):
            return self.matrix
        else: return None

def main():
    n = 4
    magic_square = MagicSquare(n)
    print(f'{magic_square.expected_sum} {magic_square.row_sum=} {magic_square.col_sum=} {magic_square.diagonal_sum=}')
    print(magic_square.get_matrix())
    

if __name__ == '__main__':
    main()