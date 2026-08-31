class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[0 for _ in range(3)] for _ in range(3)]
        for i, move in enumerate(moves):
            matrix[move[0]][move[1]] = 5 if i % 2 else 1
        res = {1: 'A', 5: 'B'}
        for row in matrix:
            S = sum(row)
            if S in (3, 15):
                return res[S // 3]
        for col in zip(*matrix):
            S = sum(col)
            if S in (3, 15):
                return res[S // 3]
        S = matrix[0][0] + matrix[1][1] + matrix[2][2]
        if S in (3, 15):
            return res[S // 3]
        S = matrix[0][2] + matrix[1][1] + matrix[2][0]
        if S in (3, 15):
            return res[S // 3]
        return 'Draw' if len(moves) == 9 else 'Pending'