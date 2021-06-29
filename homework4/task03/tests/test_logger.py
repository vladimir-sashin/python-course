from homework4.task03 import my_precious_logger


def test_logger_not_error_out(capsys):
    """my_precious_logger test: input doesn't start with 'error' and goes to stdout"""
    my_precious_logger("test\nqwerty")
    captured = capsys.readouterr()
    assert captured.out == "test\nqwerty\n"


def test_logger_not_error_err(capsys):
    """my_precious_logger test: input doesn't start with 'error', nothing goes to stderr"""
    my_precious_logger("test\nqwerty")
    captured = capsys.readouterr()
    assert captured.err == ""


def test_logger_error_out(capsys):
    """my_precious_logger test: input starts with 'error', nothing goes to stdout"""
    my_precious_logger("error: test")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_logger_error_err(capsys):
    """my_precious_logger test: input starts with 'error' and goes to stderr"""
    my_precious_logger("error: test")
    captured = capsys.readouterr()
    assert captured.err == "error: test\n"
