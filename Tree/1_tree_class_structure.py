class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
        self.node = 1
    
    def insert(self, val):
        root = self
        while(True):
            if(root.val == val):
                print('cannot be duplicate number')
                break
            if(val < root.val and not root.left ):
                root.left = Tree(val)
                self.node += 1
                break
            if(val < root.val and root.left ):
                root = root.left
            if(val > root.val and not root.right ):
                root.right = Tree(val)
                self.node += 1
                break
            if(val > root.val and root.right ):
                root = root.right
        return self.val
    
    def levelOrderTraversal(self):
        queue = [self]
        while(len(queue) != 0):
            temp = []
            while(len(queue) != 0):
                current = queue[0]
                queue.pop(0)
                if(not current):
                    print('null',end=' ')
                    continue
                else:
                    print(current.val, end=' ')
                    temp.append(current.left)
                    temp.append(current.right)
            print()
            
            queue = temp.copy()
        return

tree1 = Tree(10)
tree1.insert(4)
tree1.insert(15)
tree1.insert(2)
tree1.insert(6)

tree1.levelOrderTraversal()
        
            
    