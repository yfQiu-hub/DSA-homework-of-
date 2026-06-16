class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return
        
        curr = self.root
        while curr:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right
    
    def print_tree(self):
        self._print(self.root, 0)
    
    def _print(self, node, level):
        if not node:
            return
        self._print(node.right, level + 1)
        print("    " * level + str(node.val))
        self._print(node.left, level + 1)


#构建 BST
print("构建 BST")

bst = BST()
sequence = [50, 30, 70, 20, 40, 60, 80]
for val in sequence:
    bst.insert(val)

print("最终 BST 结构:")
bst.print_tree()