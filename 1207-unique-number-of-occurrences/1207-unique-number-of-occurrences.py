class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for a in arr:
            map[a]=map.get(a,0)+1
        return len(set(map.values()))==len(map)