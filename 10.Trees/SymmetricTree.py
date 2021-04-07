# level order traversal
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checkSym(root.left, root.right)

    def checkSym (self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and self.checkSym(node1.left, node2.right) and self.checkSym(node1.right, node2.left)
        else:
            return node1 == node2
