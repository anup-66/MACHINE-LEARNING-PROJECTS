from typing import NamedTuple

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

current_moves = [[Move(row, col) for col in range(3)]for row in range(3)]
# print(current_moves)
rows = [
    [(move.row, move.col) for move in row]
    for row in current_moves
]
columns =[
    [(move.col, move.row) for move in col]
    for col in current_moves
]
second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
first_diagonal = [row for i, row in enumerate(rows)]
winning_combo = rows + columns + [first_diagonal, second_diagonal]
# current_moves[0][0]='w'
# for combo in winning_combo:
#             results = set(
#                 current_moves[n][m].label
#                 for n, m in combo
#
#             )
            # print(combo)
            # asaw = [(n,'y') for n,m in combo]
            # print(asaw)
played_moves = (
            move.label for row in current_moves for move in row
        )
for row, row_content in enumerate(current_moves):
    for col, _ in enumerate(row_content):
        # print(row_content)
        row_content[col] = Move(row,col,"f")
    print(current_moves)

# print(rows)
# print(results)

# print(sede)
# print([row[i] for row in rows] for i in range(3))
# print([[(row[i][i],row[i][i]) for row in rows]for i in range(2)])