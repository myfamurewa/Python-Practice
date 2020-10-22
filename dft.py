def tree_paths_sum(root):
    nonlocal total
    if root is None:
        return
    total += root.value
    if root.left is not None:
        tree_paths_sum(root.left)
    if root.right is not None:
        tree_paths_sum(root.right)
        
    return total

def dft(root):
    if root is None:
        return
    print(root)
    if root.left is not None:
        dft(root.left)
    if root.right is not None:
        dft(root.right)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        else:
            return min(map(self.minDepth, (root.left, root.right) ) ) + 1