class Node:
    def __init__(self, data):
        self.left = None
        self.right= None
        self.data = data

    # start from root, check if value is less than/equal to root
    # then find empty spot
    # otherwise go to right node
    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    # start from left, then root, then right
    def printInorder(self):
        if self.left != None:
            self.left.printInorder()
        print(self.data)
        if self.right != None:
            self.right.printInorder()


    # start from root, then left, then right
    def printPreorder(self):
        print(self.data)
        if self.left != None:
            self.left.printPreorder()
        if self.right != None:
            self.right.printPreorder()

    # start from left, then right, then root
    def printPostorder(self):
        if self.left != None:
            self.left.printPostorder()
        if self.right != None:
            self.right.printPostorder()
        print(self.data)


    # no child
    # one child
    # two children
   # def delete(self, data):
#        if self.contains(data):
#            # no child
#            if self.data == data:
                

#        else:
#            return None

        
        
            


        
            
                
