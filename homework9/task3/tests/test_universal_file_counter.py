from homework9.task3 import universal_file_counter


def make_files(files):
    """Auxiliary function that that creates temporary text files with names and contents given in dict
    that is passed in arguments: '{'file1_name': 'file1 content', 'file2_name': 'file2 content'}'"""

    def make_file_decorator(func):
        def make_file_decorator_inner(tmp_path):
            for key, value in files.items():
                file = tmp_path / key
                file.write_text(value)
            return func(tmp_path)

        return make_file_decorator_inner

    return make_file_decorator


@make_files(
    {
        "file1.txt": "line1\nline2\n",
        "file2.txt": "line1\n",
        "file3.txt": "line1\nline2\nline3",
    }
)
def test_universal_file_counter_no_tokenizer(paths):
    """No optional tokenizer - directory with multiple files"""
    assert universal_file_counter(paths, "txt") == 6


def test_universal_file_counter_no_tokenizer_empty_dir(tmp_path):
    """No optional tokenizer - empty directory"""
    assert universal_file_counter(tmp_path, "txt") == 0


@make_files(
    {
        "file1.txt": "line1\nline2\n",
        "file2.txt": "line1\n",
        "json_file.json": '{"key": 12345}',
    }
)
def test_universal_file_counter_no_tokenizer_dir_with_other_files(paths):
    """No optional tokenizer - directory with multiple files, including files with other extension"""
    assert universal_file_counter(paths, "txt") == 3


@make_files(
    {
        "file1.txt": "line 1\nline 2\n",
        "file2.txt": "line 1\n",
        "file3.txt": "line 1\nline 2\nline 3",
    }
)
def test_universal_file_counter_with_tokenizer(paths):
    """Optional tokenizer - directory with multiple files"""
    assert universal_file_counter(paths, "txt", str.split) == 12


def test_universal_file_counter_with_tokenizer_empty_dir(tmp_path):
    """Optional tokenizer - empty directory"""
    assert universal_file_counter(tmp_path, "txt", str.split) == 0


@make_files(
    {
        "file1.txt": "line 1\nline 2\n",
        "file2.txt": "line 1\n",
        "json_file.json": '{"key": "word1 word2"}',
    }
)
def test_universal_file_counter_with_tokenizer_dir_with_other_files(paths):
    """Optional tokenizer - directory with multiple files, including files with other extension"""
    assert universal_file_counter(paths, "txt", str.split) == 6
