class Solution:
    def __init__(self):
        self.min = float('inf')
        self.prev = None

    def minDiffInBST(self, root):
        self.helper(root)
        return self.min

    def helper(self, root):
        if root is None:
            return

        self.helper(root.left)

        if self.prev is not None:
            self.min = min(self.min, abs(self.prev - root.val))

        self.prev = root.val

        self.helper(root.right)