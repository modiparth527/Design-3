class LRUCache:
    class Node:
        def __init__(self, key:int, value: int)-> None:
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    def addToHead(self, node: Node)-> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    
    def removeNode(self, node: Node)-> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail # Intialize the doubly Linked List
        self.tail.prev = self.head
        self.hashMap = {}

    def get(self, key: int) -> int: #O(1)
        if key not in self.hashMap: # Check if the key already exists
            return -1
        node = self.hashMap[key] # if it exists remove the node and place it towards head (MRU)
        self.removeNode(node) # 
        self.addToHead(node)
        return node.value # return the value of the node
        

    def put(self, key: int, value: int) -> None: # O(1)
        if key in self.hashMap: # check if already exists 
            node = self.hashMap[key]
            node.value = value # update its value
            self.removeNode(node) 
            self.addToHead(node)
            return
        
        if self.capacity == len(self.hashMap): # capacity is full
            tailPrev = self.tail.prev # remove the last node 
            self.removeNode(tailPrev) # tailPrev is the lastNode
            del self.hashMap[tailPrev.key] # Also delete it from hashmap
        
        node = self.Node(key, value) # If capacity if NOT full add new node
        self.addToHead(node)
        self.hashMap[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)