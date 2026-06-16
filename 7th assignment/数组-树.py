class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def array_to_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    
    for i in range(len(nodes)):
        if nodes[i]:
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]
    
    return nodes[0]

def print_tree(node, level=0):
    if not node:
        return
    print_tree(node.right, level + 1)
    print("    " * level + str(node.val))
    print_tree(node.left, level + 1)


# 测试
arr = [10, 5, 15, 3, 7, None, 20]
print(f"给定数组: {arr}")
print("\n还原后的二叉树结构:")
root = array_to_tree(arr)
print_tree(root)