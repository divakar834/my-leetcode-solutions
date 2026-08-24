class Solution:
    def maxPower(self, s: str) -> int:
        count = ans = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                if count > ans:
                    ans = count
            else:
                count = 1
        return ans