# https://leetcode.com/problems/insert-delete-getrandom-o1/
# https://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/
"""
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
                     Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. 
                     Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
                (it's guaranteed that at least one element exists when this 
                method is called). Each element must have the same probability
                of being returned.
You must implement the functions of the class such that each function works
 in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

import random

class RandomizedSet:

    def __init__(self):
        self.dict = dict()
        self.ele_list = [None for i in range(20000)]
        self.cur_size = 0
        self.max_size = 20000

    def search(self, val):
        if val not in self.dict: return None
        return self.dict[val]
        
    def insert(self, val: int) -> bool:
        if self.search(val) is not None: return False
        self.ele_list[self.cur_size] = val
        self.dict[val] = self.cur_size 
        self.cur_size+=1
        # print(self.dict, self.ele_list[:self.cur_size])
        return True

    def remove(self, val: int) -> bool:
        index = self.search(val)
        if index is None: return False
        self.cur_size-=1
        if self.cur_size != index: # If the ele to be deleted is not the last element
            self.ele_list[index] = self.ele_list[self.cur_size]
            self.dict[self.ele_list[index]] = index
        self.dict.pop(val)
        # print(self.dict, self.ele_list[:self.cur_size])
        return True

    def getRandom(self) -> int:
        return self.ele_list[random.randint(0,self.cur_size-1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()