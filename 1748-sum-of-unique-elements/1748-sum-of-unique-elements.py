class Solution:
    from collections import Counter
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        unique = Counter(nums)
        for key, val in unique.items():
            if(val == 1):
                sum += key
        return sum
        
