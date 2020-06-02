# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.val) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


class Solution:
    level = None
    def maxDepth(self, root, depth):
        if (root == None):
            return 
        elif (root.left == None and root.right == None):
            if (Solution.level == None):
                Solution.level = 1
            else:
                Solution.level = max(Solution.level, depth)
        else:
            self.maxDepth(root.left, depth+1)
            self.maxDepth(root.right, depth+1) 
        return Solution.level



tree = BinaryTree(3)
tree.root.left = TreeNode(3)
tree.root.right = TreeNode(10)

tree.root.left.left = TreeNode(1)
tree.root.left.right = TreeNode(6)

tree.root.right.right = TreeNode(14)
tree.root.right.right.left = TreeNode(13)

print(tree.preorder_print(tree.root, "preorder: "))

test = Solution()
print(test.maxDepth(tree.root, 1))