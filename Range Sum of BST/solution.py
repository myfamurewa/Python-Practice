total = 0
def rangeSumBST(root, low, high):
    if root is None:
        return
    if  low <= root.val and high <= root.val:
        total += root.val
    if root.left > low:
        rangeSumBST(root.left, low, high)
    if root.right < high:
        rangeSumBST(root.right, low, high)

