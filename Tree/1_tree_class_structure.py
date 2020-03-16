class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
    
    def insert(self, val):
        root = self.val
        while(True):
            if(root.val == val):
                print('cannot be duplicate number')
                break
            if(val < root.val and not root.left ):
                root.left = Tree(val)
                break
            if(val < root.val and root.left ):
                root = root.left
            if(val > root.val and not root.right ):
                root.right = Tree(val)
                break
            if(val > self.root.val and root.right ):
                root = root.right

        return self.root

tree1 = Tree(5)
tree1.insert(10)

        
            
    