# https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array
# https://www.codingninjas.com/codestudio/problems/n-stacks-in-an-array_1164271
"""
 Create a data structure kStacks that represents k stacks. Implementation of
  kStacks should use only one array, i.e., k stacks should use the same array for
 storing elements. 

Following functions must be supported by kStacks. push(int x, int sn) –> pushes x
  to stack number ‘sn’ where sn is from 0 to k-1 pop(int sn) –> pops an element 
  from stack number ‘sn’ where sn is from 0 to k-1 
"""

class NStack:
    def __init__(self, n, s):
        self.stack_count = n
        self.arr_size = s
        self.arr = [None for i in range(s)]
        self.free_list = [i for i in range(s)]
        self.stacks = [list() for i in range(n)]

    def is_full(self):
        return len(self.free_list)==0

    def is_empty(self, stack_number):
        return len(self.stacks[stack_number-1])==0
    
    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, 
    # and false otherwise.
    def push(self, x, m):
        if self.is_full():
            return False
        free_index = self.free_list.pop()
        self.arr[free_index] = x
        self.stacks[m-1].append(free_index)
        return True

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, 
    # otherwise returns the popped element.
    def pop(self, m):
        if self.is_empty(m):
            return -1
        pop_index = self.stacks[m-1].pop()
        temp = self.arr[pop_index]
        self.free_list.append(pop_index)
        return temp