class Stack:
    def __init__(self):
        self.stack = []

    # functions: push, pop, peak, size, is_empty
    def push(self, data):
        return self.stack.append(data)
  
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def peak(self):
        if self.is_empty():
            return None
        else: 
            return self.stack[-1]
  
    def size(self):
        return len(self.stack)

    def is_empty(self):
       return self.size() == 0
