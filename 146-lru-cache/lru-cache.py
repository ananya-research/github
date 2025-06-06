class Node:
    def __init__(self, key:int, val:int):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity
        self.left, self.right=Node(0,0), Node(0,0)
        self.left.next, self.right.prev= self.right, self.left

    def remove(self, node):
        prv, nxt= node.prev, node.next
        prv.next, nxt.prev= nxt, prv
    
    def insert(self, node):
        prv, nxt= self.right.prev, self.right
        prv.next, nxt.prev= node, node
        node.next, node.prev= nxt, prv
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return node
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            node.val=value
            self.insert(node)
        else:
            self.cache[key]=Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)