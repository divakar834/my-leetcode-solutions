class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None
        if original is target:
            return cloned
        result = self.getTargetCopy(
            original.left,
            cloned.left,
            target
        )
        if result is not None:
            return result
        return self.getTargetCopy(
            original.right,
            cloned.right,
            target
        )