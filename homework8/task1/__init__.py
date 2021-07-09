class KeyValueStorage:
    """Class that reads a text file whose lines contain key-value pairs divided by '=',
    accepts path to the file as an argument.
    To get value by key:
        - KeyValueStorage(filepath).'key' if 'key' is not a number
        - KeyValueStorage(filepath)['key'] (works for numeric keys as well)
    Numbers in values are treated as numbers, not strings."""

    def __init__(self, filepath):
        self._f = open(filepath, "r")
        self._pairs = (line.rstrip().split("=") for line in self._f)
        self._storage = {}

        for pair in self._pairs:
            key, value = pair[0], pair[1]
            if self._is_int(key) or self._is_float(key):
                raise ValueError

            if self._is_int(value):
                value = int(value)
            elif self._is_float(value):
                value = float(value)

            self._storage[key] = value

        self._f.close()

    def __getattr__(self, key):
        return self._storage.get(key)

    def __getitem__(self, key):
        return self._storage.get(key)

    @staticmethod
    def _is_float(string):
        try:
            float(string)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def _is_int(string):
        try:
            int(string)
        except ValueError:
            return False
        else:
            return True
