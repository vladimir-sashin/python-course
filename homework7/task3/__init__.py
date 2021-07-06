def tic_tac_toe_checker(board):
    columns_preprocess = ({x, y, z} for x, y, z in zip(*board) if x == y == z != "-")
    rows_preprocess = (
        set(row) for row in board if len(set(row)) == 1 and set(row).pop() != "-"
    )
    left_diagonal_preprocess = [row[i] for i, row in enumerate(board)]
    right_diagonal_preprocess = [row[-i - 1] for i, row in enumerate(board)]

    column_win_result = row_columns_check_win(columns_preprocess)
    row_win_result = row_columns_check_win(rows_preprocess)
    left_diagonal_win_result = diagonal_check_win(left_diagonal_preprocess)
    right_diagonal_win_result = diagonal_check_win(right_diagonal_preprocess)

    if (
        column_win_result
        == row_win_result
        == left_diagonal_win_result
        == right_diagonal_win_result
    ):
        return check_draw_or_unfinished(board)

    return (
        column_win_result
        or row_win_result
        or left_diagonal_win_result
        or right_diagonal_win_result
    )


def row_columns_check_win(winning_col_row_gen):
    try:
        value_in_set = next(winning_col_row_gen)
    except StopIteration:
        return None
    else:
        value = value_in_set.pop()
        return "{} wins!".format(value)


def diagonal_check_win(diagonal):
    if len(diagonal) == 3 and len(set(diagonal)) == 1:
        value = diagonal.pop()
        return "{} wins!".format(value)


def check_draw_or_unfinished(board):
    draw_rows = [
        set(row) for row in board if len(set(row)) == 2 and "-" not in set(row)
    ]
    if len(draw_rows) == 3:
        return "draw!"
    else:
        return "unfinished"
