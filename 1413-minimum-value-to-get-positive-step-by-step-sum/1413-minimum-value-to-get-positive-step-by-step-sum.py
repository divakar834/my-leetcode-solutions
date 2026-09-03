class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        nums = [0] + nums
        n = len(nums)
        dp = [0] * n
        for i in range(1,n):
            dp[i] = dp[i-1] + nums[i]
        min_dp = min(dp[1:])
        return max(1, 1 - min_dp)