import os
import sqlite3
from shutil import copyfile

import pytest

from homework8.task2 import TableData


def get_file_path(file_name):
    """Auxiliary function to get filepath"""
    return os.path.join(os.path.dirname(__file__), file_name)


def make_temp_db(original_db_filename):
    """Auxiliary decorator to make a temporary copy of sqlite db file from 'tests' directory for every test,
    based on 'tmp_path' pytest fixture"""

    def make_temp_db_decorator(func):
        def make_temp_db_decorator_inner(tmp_path):
            temp_db = tmp_path / "temp_db"
            copyfile(original_db_filename, temp_db)
            result = func(temp_db)
            return result

        return make_temp_db_decorator_inner

    return make_temp_db_decorator


def modify_bd(db, values_tuple_to_insert=(), name_to_delete=""):
    """Auxiliary function to modify test database. Returns modified database file. OPTIONAL arguments:
    - values_tuple_to_insert is the tuple of values to be inserted, for example ('Biden', '12345', 'US')
    - name_to_delete is the 'name' in the row to be deleted"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    if values_tuple_to_insert:
        cursor.execute(
            "INSERT INTO presidents VALUES (?, ?, ?)", values_tuple_to_insert
        )
    if name_to_delete:
        cursor.execute("DELETE FROM presidents WHERE name = ?", (name_to_delete,))
    conn.commit()
    conn.close()
    return db


original_test_db_file = get_file_path("example.sqlite")


@make_temp_db(original_test_db_file)
def test_get_len(db_file):
    """Get number of rows in the table"""
    presidents = TableData(db_file, "presidents")
    assert len(presidents) == 3


@make_temp_db(original_test_db_file)
def test_table_doesnt_exist(db_file):
    """Try to create a TableData instance passing table name that doesn't exist in database"""
    with pytest.raises(KeyError) as error:
        pokemons = TableData(db_file, "pokemons")
        assert str(error.value) == "Table not found"


@make_temp_db(original_test_db_file)
def test_get_row_by_name(db_file):
    """Get whole row where column 'name' == value passed in []"""
    presidents = TableData(db_file, "presidents")
    assert presidents["Big Man Tyrone"] == ("Big Man Tyrone", 101, "Kekistan")


@make_temp_db(original_test_db_file)
def test_get_row_by_name_that_doesnt_exist(db_file):
    """Try to get a row passing 'name' that doesn't exist in table"""
    with pytest.raises(KeyError) as error:
        presidents = TableData(db_file, "presidents")
        presidents["Biden"]
    assert str(error.value) == "'Name not found'"


@make_temp_db(original_test_db_file)
def test_check_that_name_is_in_db(db_file):
    """Check that there is a row in the table with specified 'name' value"""
    presidents = TableData(db_file, "presidents")
    assert "Trump" in presidents


@make_temp_db(original_test_db_file)
def test_check_that_name_is_not_in_db(db_file):
    """Check that there is no row in the table with specified 'name' value"""
    presidents = TableData(db_file, "presidents")
    assert ("Qwerty" in presidents) is False


@make_temp_db(original_test_db_file)
def test_iterate_in_for_loop(db_file):
    """Iterate over all database rows to get all values in the list of dicts"""
    presidents = TableData(db_file, "presidents")
    presidents_data = []
    for president in presidents:
        presidents_data.append(president)
    assert presidents_data == [
        {"name": "Yeltsin", "age": 999, "country": "Russia"},
        {"name": "Trump", "age": 1337, "country": "US"},
        {"name": "Big Man Tyrone", "age": 101, "country": "Kekistan"},
    ]


@make_temp_db(original_test_db_file)
def test_iterate_in_for_loop_and_get_column_by_square_brackets(db_file):
    """Iterate over all database rows to get values of 'name' column"""
    presidents = TableData(db_file, "presidents")
    presidents_names = []
    for president in presidents:
        presidents_names.append(president["name"])
    assert presidents_names == ["Yeltsin", "Trump", "Big Man Tyrone"]


@make_temp_db(original_test_db_file)
def test_add_row_then_get_len(db_file):
    """Make a TableData instance, add new row to the database and get it's updated len()"""
    presidents = TableData(db_file, "presidents")
    modify_bd(db_file, ("Biden", "12345", "US"))
    assert len(presidents) == 4


@make_temp_db(original_test_db_file)
def test_delete_row_then_get_len(db_file):
    """Make a TableData instance, delete a row from the database and get it's updated len()"""
    presidents = TableData(db_file, "presidents")
    modify_bd(db_file, name_to_delete="Trump")
    assert len(presidents) == 2


@make_temp_db(original_test_db_file)
def test_add_row_and_get_it_by_name(db_file):
    """Make a TableData instance, add new row to the database and get added row by it's 'name'"""
    presidents = TableData(db_file, "presidents")
    modify_bd(db_file, values_tuple_to_insert=("Biden", 12345, "US"))
    assert presidents["Biden"] == ("Biden", 12345, "US")


@make_temp_db(original_test_db_file)
def test_delete_row_and_try_to_get_it_by_name(db_file):
    """Make a TableData instance, delete a row from the database and try to get deleted row by it's 'name'"""
    with pytest.raises(KeyError) as error:
        presidents = TableData(db_file, "presidents")
        modify_bd(db_file, name_to_delete="Trump")
        presidents["Trump"]
    assert str(error.value) == "'Name not found'"


@make_temp_db(original_test_db_file)
def test_add_row_and_check_that_name_is_in_db(db_file):
    """Make a TableData instance, add new row to the database and check if added row is in table by it's 'name'"""
    presidents = TableData(db_file, "presidents")
    modify_bd(db_file, values_tuple_to_insert=("Biden", 12345, "US"))
    assert "Biden" in presidents


@make_temp_db(original_test_db_file)
def test_delete_row_and_check_that_name_is_not_in_db(db_file):
    """Make a TableData instance, delete a row from the database and check that
    deleted row is not in table by it's 'name'"""
    presidents = TableData(db_file, "presidents")
    modify_bd(db_file, name_to_delete="Trump")
    assert ("Trump" in presidents) is False


@make_temp_db(original_test_db_file)
def test_iterate_in_for_loop_after_modifying_db(db_file):
    """Make a TableData instance, delete a row from the database and add a new one, then iterate over new data to get
    all updated values"""
    presidents = TableData(db_file, "presidents")
    modify_bd(
        db_file,
        values_tuple_to_insert=("Biden", 12345, "US"),
        name_to_delete="Big Man Tyrone",
    )
    presidents_data = []
    for president in presidents:
        presidents_data.append(president)
    assert presidents_data == [
        {"name": "Yeltsin", "age": 999, "country": "Russia"},
        {"name": "Trump", "age": 1337, "country": "US"},
        {"name": "Biden", "age": 12345, "country": "US"},
    ]
