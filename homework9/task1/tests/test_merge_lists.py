from homework9.task1 import merge_sorted_files, merge_sorted_files_heapq


def make_files(files):
    """Auxiliary function that that creates temporary text files with names and contents given in dict
    that is passed in arguments: '{'file1_name': 'file1 content', 'file2_name': 'file2 content'}'"""

    def make_file_decorator(func):
        def make_file_decorator_inner(tmp_path):
            files_list = []
            for key, value in files.items():
                file = tmp_path / key
                file.write_text(value)
                files_list.append(file)
            return func(files_list)

        return make_file_decorator_inner

    return make_file_decorator


@make_files(
    {
        "file1.txt": "1\n6\n7\n",
        "file2.txt": "4\n5\n15\n",
        "file3.txt": "8\n9\n100\n",
    }
)
def test_merge_sorted_files(files):
    assert list(merge_sorted_files(files)) == [1, 4, 5, 6, 7, 8, 9, 15, 100]


@make_files({"file1.txt": "1\n3\n6\n7\n", "file2.txt": "4\n5\n10\n"})
def test_merge_sorted_files_different_file_length(files):
    assert list(merge_sorted_files(files)) == [1, 3, 4, 5, 6, 7, 10]


@make_files(
    {
        "file1.txt": "1\n6\n7\n",
        "file2.txt": "4\n5\n15\n",
        "file3.txt": "8\n9\n100\n",
    }
)
def test_merge_merge_sorted_files_heapq(files):
    assert list(merge_sorted_files_heapq(files)) == [1, 4, 5, 6, 7, 8, 9, 15, 100]


@make_files({"file1.txt": "1\n3\n6\n7\n", "file2.txt": "4\n5\n10\n"})
def test_merge_merge_sorted_files_heapq_different_file_length(files):
    assert list(merge_sorted_files_heapq(files)) == [1, 3, 4, 5, 6, 7, 10]
