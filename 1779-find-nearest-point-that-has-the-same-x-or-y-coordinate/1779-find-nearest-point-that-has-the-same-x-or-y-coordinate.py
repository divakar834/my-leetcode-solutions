class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        current_min_distance = float(inf)
        current_min_index = -1
        for i, [a, b] in enumerate(points):
            if x == a or y == b:
                distance = abs(x-a) + abs(y-b)
                if distance < current_min_distance:
                    current_min_distance = distance
                    current_min_index = i
        return current_min_index