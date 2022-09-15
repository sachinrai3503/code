"""
Reverse a stck

Example: 
Input: elements present in stack from top to bottom 1 2 3 4 
Output: 4 3 2 1 
"""

class Solution:

    def get_last_ele(self, stck):
        if len(stck)==0: return None
        temp = stck.pop()
        last_ele = self.get_last_ele(stck)
        if last_ele is None: return temp
        stck.append(temp)
        return last_ele

    # https://www.geeksforgeeks.org/reverse-a-stack-using-recursion
    """
    Write a program to reverse a stack using recursion, without using any loop.
    """
    def reverse_stack_with_recursion(self, stck):
        if len(stck)==0: return
        last_ele = self.get_last_ele(stck)
        self.reverse_stack_with_recursion(stck)
        stck.append(last_ele)
    
    # https://www.geeksforgeeks.org/reverse-stack-without-using-extra-space/
    """
    Implement the stack using linked list
    """
    def reverse_stack_in_O1_space(self, stck):
        # implement as SLL and reverse
        pass

    # https://www.geeksforgeeks.org/reversing-a-stack-with-the-help-of-another-empty-stack/
    """
    Given a Stack consisting of N elements, the task is to reverse the Stack 
    using an extra stack.
    """
    def reverse_using_extra_stack(self, stck1, stck2):
        if len(stck1)==0: return
        temp = stck1.pop()
        self.reverse_using_extra_stack(stck1, stck2)
        stck2.append(temp)
    
    def reverse_stck_using_extra_stack(self, stck1, stck2):
        self.reverse_using_extra_stack(stck1, stck2)
        while len(stck2)>0:
            stck1.append(stck2.pop())

def main():
    sol = Solution()
    stck = [0,1]
    print(f'{stck=}')
    # sol.reverse_stack_with_recursion(stck)
    sol.reverse_stck_using_extra_stack(stck, [])
    print(f'{stck=}')

if __name__ == '__main__':
    main()