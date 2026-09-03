class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        pointer1, idx1, pointer2, idx2 = 0, 0, 0, 0  
        while pointer1 < len(word1) and pointer2 < len(word2):
            char1, char2 = word1[pointer1][idx1], word2[pointer2][idx2]
            if char1 != char2:
                return False
            idx1 += 1
            idx2 += 1
            if idx1 == len(word1[pointer1]):
                idx1, pointer1 = 0, pointer1 + 1 
            if idx2 == len(word2[pointer2]):
                idx2, pointer2 = 0, pointer2 + 1
        return pointer1 == len(word1) and pointer2 == len(word2)        