import sqlite3


class TableData:
    """Class for accessing table data from sqlite database file. Arguments:
        - database_name - filename of the database
        - table_name - name of the table

    Instance creation: presidents = TableData(database_name='example.sqlite', table_name='presidents')
    Use cases:
        - 'len(presidents)' returns current amount of rows in presidents table in database
        - 'presidents['Yeltsin']' returns single data row for president with name Yeltsin
        - ''Yeltsin' in presidents' returns if president with name Yeltsin exists in table
        - As object implements iteration protocol, it could be used in for loops to access all column values
         of the table. On each iteration a dict with {'column name': 'value'} for one row is returned.
            Example1 - print all values of 'name' column in the table:
            for president in presidents:
                print(president['name'])
            Example 2 - print dict with all column values in the table:
            for president in presidents:
                print(president)
    """

    def __init__(self, database_name, table_name):
        self._file_path = database_name
        self._index = -1
        # check if a table with given 'table_name' exists in table
        if self._exists_table(table_name):
            self._table_name = table_name
        else:
            raise KeyError("Table not found")

    def _connect(self):
        """Shortcut for connection to sqlite database
        CONNECTION SHOULD BE CLOSED AFTER EVERY CALL WHEN IT'S NOT NEEDED NO LONGER"""
        self._conn = sqlite3.connect(self._file_path)
        cursor = self._conn.cursor()
        return cursor

    def _generate_rows(self):
        """Generator that yields rows from table name given in arguments to class"""
        cursor = self._connect()
        cursor.execute("SELECT * FROM {}".format(self._table_name))
        for row in cursor:
            yield row

    def _exists_table(self, table_name):
        """Checks if table name given in arguments to class exists"""
        cursor = self._connect()
        cursor.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' and name = ?", (table_name,)
        )
        is_existing = bool([row for row in cursor])
        self._conn.close()
        return is_existing

    def __len__(self):
        """If len() is called on object instance it returns number of rows in table"""
        cursor = self._connect()
        cursor.execute("select count(*) from {}".format(self._table_name))
        len = cursor.fetchone()[0]
        self._conn.close()
        return len

    def _select_row_by_name(self, key):
        """Returns a generator that yields a row where 'name' column value is equal to given, if such row exists"""
        cursor = self._connect()
        cursor.execute(
            "SELECT * from {} where name = ?".format(self._table_name), (key,)
        )
        return (row for row in cursor)

    def __getitem__(self, key):
        try:
            row = next(self._select_row_by_name(key))
        except StopIteration:
            self._conn.close()
            raise KeyError("Name not found")
        else:
            return row

    def __contains__(self, key):
        try:
            a = next(self._select_row_by_name(key))
            print(a)
        except StopIteration:
            return False
        else:
            return True
        finally:
            self._conn.close()

    def __iter__(self):
        cursor = self._connect()
        cursor.execute("SELECT * FROM {}".format(self._table_name))
        self.column_names = [description[0] for description in cursor.description]
        self._conn.close()

        self._rows = self._generate_rows()
        self._rows_dict = (dict(zip(self.column_names, row)) for row in self._rows)
        return self

    def __next__(self):
        try:
            next_element = next(self._rows_dict)
        except StopIteration:
            self._conn.close()
            raise StopIteration
        else:
            return next_element
