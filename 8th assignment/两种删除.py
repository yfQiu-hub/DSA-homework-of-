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

    def delete_by_predecessor(self, key):
        """用中序前驱（左子树最大值）删除"""
        self.root = self._delete_by_predecessor(self.root, key)
    
    def _delete_by_predecessor(self, node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self._delete_by_predecessor(node.left, key)
        elif key > node.val:
            node.right = self._delete_by_predecessor(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # 找左子树的最大值（前驱）
            pred = node.left
            while pred.right:
                pred = pred.right
            node.val = pred.val
            node.left = self._delete_by_predecessor(node.left, pred.val)
        return node
    
    def delete_by_successor(self, key):
        """用中序后继（右子树最小值）删除"""
        self.root = self._delete_by_successor(self.root, key)
    
    def _delete_by_successor(self, node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self._delete_by_successor(node.left, key)
        elif key > node.val:
            node.right = self._delete_by_successor(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # 找右子树的最小值（后继）
            succ = node.right
            while succ.left:
                succ = succ.left
            node.val = succ.val
            node.right = self._delete_by_successor(node.right, succ.val)
        return node
    
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
bst.print_tree()

print("\n"*2)

# 方法1：中序前驱删除
bst1 = BST()
for val in sequence:
    bst1.insert(val)
bst1.delete_by_predecessor(50)
bst1.print_tree()

print("\n"*2)

# 方法2：中序后继删除
bst2 = BST()
for val in sequence:
    bst2.insert(val)
bst2.delete_by_successor(50)
bst2.print_tree()