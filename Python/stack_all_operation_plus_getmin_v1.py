# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
"""
Design a Data Structure SpecialStack that supports all the stack operations
like push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
which should return minimum element from the SpecialStack. 

All these operations of SpecialStack must be O(1). 
To implement SpecialStack, you should only use standard Stack data structure 
and no other data structure like arrays, list, .. etc.

Example:
Consider the following SpecialStack
16  --> TOP
15
29
19
18
getMin() should return 15

After 2 pop()
29  --> TOP
19
18
getmin() returns 18
"""
# Below method is O(1) time O(n) space
# For O(1) time O(1) space see stack_all_operation_plus_getmin_v2.py

class spcl_stack:
    
    def __init__(self, max_size):
        self.data_list = list()
        self.min_list = list()
        self.max_size = max_size
    
    def is_empty(self):
        return True if len(self.data_list) is 0 else False

    def is_full(self):
        return True if len(self.data_list)==self.max_size else False
    
    def push(self, data):
        if self.is_full():
            print('Stack is Full')
        else:
            if not len(self.min_list) or data<=self.min_list[-1]:
                self.min_list.append(data)
            self.data_list.append(data)
    
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            if self.data_list[-1]==self.min_list[-1]:
                self.min_list.pop()
            return self.data_list.pop()
    
    def get_min(self):
        if not len(self.min_list):
            import sys; return sys.maxsize
        return self.min_list[-1]

    def print(self):
        print(self.data_list)

def test_stack(ip_list):
    stck = spcl_stack(20)
    for num in ip_list:
        stck.push(num)
        print('Stack',end='=>')
        stck.print()
        print('Min =',stck.get_min())
    while not stck.is_empty():
        print('Stack',end='=>')
        stck.print()
        print('Min =',stck.get_min())
        stck.pop()

def main():
    ip_list = [18,19,29,15,16]
    print('ip>>',ip_list)
    test_stack(ip_list)

if __name__ == '__main__':
    main()