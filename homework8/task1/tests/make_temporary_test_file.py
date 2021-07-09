def make_file(content):
    def make_file_decorator(func):
        def make_file_decorator_inner(tmp_path):
            file = tmp_path / "test_file.txt"
            file.write_text(content)
            return func(file)

        return make_file_decorator_inner

    return make_file_decorator
