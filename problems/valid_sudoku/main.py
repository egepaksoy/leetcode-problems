def isValidSudoku(board: List[List[str]]):
    inspected_number = "0"

    y = 0
    while y < len(board):
        x = 0
        inspected_number = "0"
        while x < len(board[y]):
            if board[y][x] != ".":
                inspected_number = board[y][x]
                x2 = x + 1
                
                # satıra bakma
                while x2 < len(board[y]):
                    if board[y][x2] == inspected_number:
                        return False
                    x2 += 1

                # sutuna bakma
                y2 = y + 1
                while y2 < len(board):
                    if board[y2][x] == inspected_number:
                        return False
                    y2 += 1

                # kucuk kareye bakma
                min_x = x//3 * 3
                max_x = (x//3*3) + 2

                min_y = y//3 * 3
                max_y = (y//3*3) + 2

                y2 = min_y
                while y2 <= max_y:
                    x2 = min_x
                    while x2 <= max_x:
                        if board[y2][x2] == inspected_number and not (y2 == y and x2 == x):
                            return False
                        x2 += 1
                    y2 += 1
                
            x += 1
        y += 1
    return True