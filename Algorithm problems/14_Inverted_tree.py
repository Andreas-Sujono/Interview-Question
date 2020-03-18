class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value, end=" ")
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(root):
    # Fill this in.
    if not root:
        return None
    leftTree = Node(invert(root.left))
    rightTree = Node(invert(root.right))
    root.left = rightTree.value
    root.right = leftTree.value
    return root
    

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print()
invert(root)
root.preorder()
print()
# a c f b e d