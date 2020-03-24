class MaxStack:
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.maxStack = []

    def push(self, val):
        # Fill this in.
        self.stack.append(val)
        if(val > self.stack[-1] if len(self.stack) > 0 else True):
            self.stack.append(val)
        else:
            self.stack.append(val)

    def pop(self):
        # Fill this in.
        if(len(self.stack) > 0):
            return self.stack.pop() 
        else:
            return None

    def max(self):
        # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2