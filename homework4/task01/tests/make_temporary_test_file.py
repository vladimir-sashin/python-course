import os


def make_file(filename, content):
    def make_file_decorator(func):
        def make_file_decorator_inner(tmp_path):
            file = tmp_path / filename
            file.write_text(content)
            try:
                result = func(file)
            finally:
                os.remove(file)
            return result

        return make_file_decorator_inner

    return make_file_decorator
