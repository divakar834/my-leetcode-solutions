class Solution(object):
    def numIdenticalPairs(self, nums):
        compare = {}
        count = 0
        for i,n in enumerate(nums):
            if n in compare:
                count += compare[n]
            compare[n] = compare.get(n, 0) + 1
        return count