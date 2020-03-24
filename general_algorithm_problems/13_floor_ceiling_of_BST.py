class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def findCeilingFloor(root, k, floor=None, ceil=None):
    # Fill this in.
    queue = [root]
    while (len(queue) != 0):
        current = queue[0]
        queue.pop(0)
        if(current.left):
            queue.append(current.left)
        if(current.right):
            queue.append(current.right)
        if((current.val > floor if floor else True) and current.val < k):
            floor = current.val
        if((current.val < ceil if ceil else True) and current.val > k):
            ceil = current.val
    return floor, ceil if floor and ceil else None


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)