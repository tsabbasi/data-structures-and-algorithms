INITIAL_CAPACITY = 2

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def find(self, key):
        index = hash(key)
        node = self.buckets[index]
        while node is not None and self.key != None:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def insert(self, key, value):
        # convert your key to idx val
        # check if there is a node at current idx
        # if so, iterate through linked list until empty spot, then insert
        # otherwise just insert
        self.size += 1
        index = hash(key)
        node = buckets[index]

        if node is None:
            node = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

def isUnique(ht, string):
    charList = list(string)
    for ch in charList:
        if ht.find(ch) > 0:
            ht.node.value += 1
            return "not unique"
        else:
            ht.insert(ch, 0)
    return "all unique char"
    
        
