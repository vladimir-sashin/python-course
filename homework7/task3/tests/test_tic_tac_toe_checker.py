from homework7.task3 import tic_tac_toe_checker


def test_win_on_row():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_win_on_column():
    board = [["x", "o", "x"], ["x", "o", "-"], ["o", "o", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_win_on_column1():
    board = [["x", "-", "o"], ["x", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_win_on_right_diagonal():
    board = [["x", "x", "o"], ["x", "o", "-"], ["o", "-", "-"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_win_on_left_diagonal():
    board = [["o", "x", "x"], ["-", "o", "x"], ["-", "-", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_draw():
    board = [["o", "x", "o"], ["o", "x", "x"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "draw!"


def test_unfinished():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "unfinished"
