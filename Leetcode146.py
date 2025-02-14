#Time Complexity = O(1)
#Space Complexity = O(c) c is capacity

class Node:
    def __init__(self, key, val): 
        self.key, self.val = key, val
        self.prev, self.next = None, None  # Initialize previous and next pointers

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Mapping from key to node
        
        #  two dummy nodes to mark the bounds (left = LRU, right = MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # Connect the two ends
    
    # Remove node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev  # Adjust pointers to skip over 'node'

    # Insert node at the right (MRU end)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right  # Get the node before and after the insertion point
        prev.next = nxt.prev = node  # Link node between 'prev' and 'right'
        node.next, node.prev = nxt, prev  # Adjust node's own pointers

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed node to the most recently used position
            self.remove(self.cache[key])  # Remove from its current position
            self.insert(self.cache[key])  # Insert it at the MRU end
            return self.cache[key].val  # Return the value associated with the key
        else:
            return -1  # Key not found in cache

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, remove the old node
            self.remove(self.cache[key])
        # Insert the new key-value pair
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # If the cache exceeds capacity, remove the least recently used (LRU) node
            lru = self.left.next  # LRU node is next to the left dummy node
            self.remove(lru)  # Remove LRU node from the linked list
            del self.cache[lru.key]  # Delete LRU node from the cache