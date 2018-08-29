INITIAL_CAPACITY = 50

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

    # key is a string of characters
    # the hash function converts this to an integer
    # this calculation focuses on uniformity
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            print("hashsum before mod {}".format(hashsum))
            hashsum = hashsum % self.capacity
            print("hashsum after mod {}".format(hashsum))
        return hashsum

    # increment the size of hashtable
    # compute index of key using hash function
    # if bucket at index is empty, create a new node and add it there
    # otherwise a collision occured: add the new node to the existing node
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        #find node at index above
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        
        # iterate through linked list until next node is none
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # once you find the end of linkedlist, add node
        prev.next = Node(key, value)

    # compute index for the key using hash function
    # go to bucket for that index
    # iterate nodes in that linked list until key is found or end of list reached
    # return value of found node, or None if not found
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    # compute hash for the key to determine index
    # iterate linked list of nodes, continue until end of list or key is found
    # if key not found, return None
    # else remove node from linked list and return node value
    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None 
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result
            
        

        
            
