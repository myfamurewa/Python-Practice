class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.serial = ""
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string

        """
        if root is None:
            return
        self.serial += str(root.val)
        if root.left is not None:
            self.serialize(root.left)
        if root.right is not None:
            self.serialize(root.right)
        return self.serial
    
    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree

        """
        if self.serial == "":
            return TreeNode(None) 
        root = TreeNode(int(self.serial[0]))
        self.serial.pop(0)
        def add(root, node):
            if node.val > root.val:
                if root.right is None:
                    root.right = node
                    return
                else:
                    add(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                    return
                else:
                    add(root.left, node)

        for node in self.serial:
            newnode = TreeNode(int(node))
            add(root, newnode)

        return root

# My edited solution for leet code
    #     def __init__(self):
#         self.serial = ""
#     def serialize(self, root: TreeNode) -> str:
#         """Encodes a tree to a single string.
#         """
#         if root is None:
#             return
#         self.serial += str(root.val)
#         if root.left is not None:
#             self.serialize(root.left)
#         if root.right is not None:
#             self.serialize(root.right)
#         return self.serial

#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         if data == "":
#             return TreeNode(data) 
#         root = TreeNode(int(data[0]))
#         def add(root, node):
#             if node.val > root.val:
#                 if root.right is None:
#                     root.right = node
#                     return
#                 else:
#                     add(root.right, node)
#             else:
#                 if root.left is None:
#                     root.left = node
#                     return
#                 else:
#                     add(root.left, node)

#         for node in data[1:]:
#             newnode = TreeNode(int(node))
#             add(root, newnode)
#         return root

# solution from leet code
# class Codecv2:
    
#     def encode_succinct(self, node, q):
#         if not node:
#             q.append(None)
#             return
#         q.append(node.val)
#         self.encode_succinct(node.left, q)
#         self.encode_succinct(node.right, q)

#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         q = collections.deque()
#         self.encode_succinct(root, q)
#         return q

#     def decode_succinct(self, q):
#         b = q.popleft()
#         if b == None:
#             return None
#         n = TreeNode(b)
#         n.left = self.decode_succinct(q)
#         n.right = self.decode_succinct(q)
#         return n

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         return self.decode_succinct(data)



