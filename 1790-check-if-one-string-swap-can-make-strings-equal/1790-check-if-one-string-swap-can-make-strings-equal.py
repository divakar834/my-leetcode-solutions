class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i] not in s2:
                    return False
                else:
                    if s1.count(s1[i])!=s2.count(s1[i]):
                        return False
                c+=1
        if c==2 or c==0:
            return True 
        return False
        