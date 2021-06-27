import sys


def my_precious_logger(text: str):
    if text.startswith("error"):
        print(text, file=sys.stderr)
    else:
        print(text)
