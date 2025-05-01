# https://leetcode.com/problems/lru-cache
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add 
 the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f'({self.key=}:{self.val=})'

class DLL:
    def __init__(self):
        self.start = None
        self.end = None
    
    def append_node(self, node):
        if self.start==None:
            self.start = node
        else:
            self.end.right = node
            node.left = self.end
        self.end = node
    
    def delete_node(self, node):
        left, right = node.left, node.right
        if left:
            left.right = node.right
        else:
            self.start = node.right
        if right:
            right.left = node.left
        else:
            self.end = node.left
        node.left = node.right = None
        return node
    
    def delete_start_node(self):
        return self.delete_node(self.start)
    
    def print_DLL(self):
        temp = self.start
        while temp:
            print(temp, end = '')
            temp = temp.right
        print('*'*50)

class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.cur_size = 0
        self.dll = DLL()
        self.key_dll_map = dict()

    def get(self, key: int) -> int:
        key_node = self.key_dll_map.get(key, None)
        if key_node is None: return -1
        self.dll.append_node(self.dll.delete_node(key_node))
        # self.dll.print_DLL()
        return key_node.val

    def put(self, key: int, value: int) -> None: 
        key_node = self.key_dll_map.get(key, None)
        if key_node is not None:
            self.dll.append_node(self.dll.delete_node(key_node))
            key_node.val = value
        else:
            if self.cur_size == self.max_size:
                dll_node = self.dll.delete_start_node()
                del(self.key_dll_map[dll_node.key])
                del(dll_node)
                self.cur_size-=1
            key_node = DLLNode(key, value)
            self.key_dll_map[key] = key_node
            self.dll.append_node(key_node)
            self.cur_size+=1
        # self.dll.print_DLL()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)