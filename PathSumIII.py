# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # set up a stack
            # lists node, path, and total
        # initialize the stack with starting values
        # create a while loop - while stack contains values
        # pull off the a node
            # take its value and add it to the path
            # take value and add to total
            # check if it has a left
                # if so we'll add a new item to stack with new node, updated path, and updated value
            # check if it has a right
                # if so we'll add a new item to stack with new node, updated path, and updated value
            # check if left & right are none
                # if so and value is equal to sum
                    # add pathway to an answers list
        # return answers list
        if root == None:
            return []
        stack = []
        answs = []
        stack.append([root, [], 0])
        while len(stack) != 0:
            cur_node = stack[0]
            del stack[0]
            pathway = copy.copy(cur_node[1])
            pathway.append(cur_node[0].val)
            total = cur_node[2] + cur_node[0].val
            if cur_node[0].right != None:
                stack.append([cur_node[0].right, pathway, total])
            if cur_node[0].left != None:
                stack.append([cur_node[0].left, pathway, total])
            if cur_node[0].left == None and cur_node[0].right == None and total == sum:
                answs.append(pathway)
        return answs