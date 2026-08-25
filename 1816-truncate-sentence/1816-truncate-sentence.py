class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1 = s.split()
        return " ".join(s1[:k])