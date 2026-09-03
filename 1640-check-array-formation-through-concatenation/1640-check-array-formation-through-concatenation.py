class Solution(object):
    def canFormArray(self, arr, pieces):
        m = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in m:
                return False
            p = m[arr[i]]
            for num in p:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1
        return True