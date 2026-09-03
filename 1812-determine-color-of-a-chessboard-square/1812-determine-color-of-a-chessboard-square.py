class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        if((column + row) % 2 == 0):
            return False
        else:
            return True