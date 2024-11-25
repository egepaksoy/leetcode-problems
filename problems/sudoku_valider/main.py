class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        inspected_number = "0"

        y = 0
        while y < len(board):
            x = 0
            inspected_number = "0"
            while x < len(board[y]):
                if board[y][x] != ".":
                    inspected_number = board[y][x]
                    z = x + 1
                    # satıra bakma
                    while z < len(board[y]):
                        if board[y][z] == inspected_number:
                            return False
                        z += 1
                    # sutuna bakma
                    y2 = y + 1
                    while y2 < len(board):
                        if board[y2][x] == inspected_number:
                            return False
                        y2 += 1
                    # kucuk kareye bakma
                x += 1
            y += 1
        return True