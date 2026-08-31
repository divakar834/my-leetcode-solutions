class Solution:
    def mergeTrees(self, root1, root2):
        return self.merge(root1, root2)
    def merge(self, r1, r2):
        if r1 is None:
            return r2
        if r2 is None:
            return r1
        r1.val += r2.val
        r1.left = self.merge(r1.left, r2.left)
        r1.right = self.merge(r1.right, r2.right)
        return r1