class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
    def traverse(self):
        # set current node
        # iterate through linked list, print nodes, until reached end of list
        node = self
        while node != None:
            print(node.data)
            node = node.next_node



# remove duplicates from a linked list
# use an array to store new values, if new node already in array, remove current node from linked list, and continue.
# removing a node: point the previous node to the node after the current node
def remove_duplicates(node):
    unique_data = []
    previous = None
    while node != None:
        print(unique_data)
        if node.data in unique_data:
            previous.next_node = node.next_node
        else:
            unique_data.append(node.data)
        previous = node
        node = node.next_node
def remove_dup_w_runner(node):
    current = node
    while current != None:
        runner = current
        while runner.next_node != None:
            if runner.next_node.data != current.data:
                runner = runner.next_node
            else:
                runner.next_node = runner.next_node.next_node
        current = current.next_node

#Test:
node = Node(8)
node2 = Node(5)
node3 = Node(8)
node4 = Node(3)
node.next = node2
node.next_node = node2
node2.next_node = node3
node3.next_node = node4
node.traverse()
#remove_duplicates(node)
remove_dup_w_runner(node)

