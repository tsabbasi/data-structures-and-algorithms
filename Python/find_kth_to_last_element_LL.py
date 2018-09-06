class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    def traverse(self):
        # set current node
        # iterate through linked list, print nodes, until reached end of list
        node = self
        while node != None:
            print(node.data)
            node = node.next
def find_k_to_last(size, k, node):
    curr = node
    counter = size
    while node != None and counter != k:
        counter -= 1
        node = node.next
    if node != None:
        return node.data
def sumLists(node1, node2):
    power = 0
    sum1 = 0
    sum2 = 0
    while node1 != None and node2 != None:
        sum1 += (node1.data * pow(10, power))
        node1 = node1.next
        power += 1
    power = 0
    while node2 != None:
        sum2 += (node2.data * pow(10, power))
        node2 = node2.next
        power += 1
    return sum1 + sum2
        
        
    

nodeA = Node(7)
nodeA2 = Node(1)
nodeA3 = Node(6)
nodeA.next = nodeA2
nodeA2.next = nodeA3
nodeA.traverse()

nodeB = Node(5)
nodeB2 = Node(9)
nodeB3 = Node(2)
nodeB.next = nodeB2
nodeB2.next = nodeB3
nodeB.traverse()
#find_k_to_last(4, 2, node)



    
