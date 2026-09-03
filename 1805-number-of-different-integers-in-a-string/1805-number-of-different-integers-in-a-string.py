class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        matches = re.findall(r'-?\d*\.?\d+', word)
        ans=[int(i) for i in matches]
        return len(set(ans))