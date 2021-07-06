from homework7.task1 import extract_values_from_tree


def test_extract_from_tree_of_lists():
    tree_lists = {
        1: ["RED", "BLUE"],
        2: {
            "embedded in 2nd": ["RED", "RED", "BLUE"],
        },
        3: {
            "embedded in 3rd": {
                "another": [["RED", "RED"], "BLUE", "BLUE"],
            }
        },
    }
    assert extract_values_from_tree(tree_lists, "RED") == 5


def test_extract_from_tree_of_sets():
    tree_sets = {
        1: {"RED", "BLUE"},
        2: {
            "embedded in 2nd": {"BLUE", "RED"},
        },
        3: {
            "embedded in 3rd": {
                "another": {"RED"},
            }
        },
    }
    assert extract_values_from_tree(tree_sets, "RED") == 3


def test_extract_from_tree_of_tuples():
    tree_tuples = {
        1: ("RED", "BLUE"),
        2: {
            "embedded in 2nd": ("RED", "RED", "BLUE"),
        },
        3: {
            "embedded in 3rd": {
                "another": (("RED", "RED"), "BLUE", "BLUE"),
            }
        },
    }
    assert extract_values_from_tree(tree_tuples, "RED") == 5


def test_extract_from_tree_of_different_non_collection_types():
    tree_lists = {
        1: ["RED", 1],
        2: {
            "embedded in 2nd": ["RED", False, "BLUE"],
        },
        3: {
            "embedded in 3rd": {
                "another": [[None, "RED"], True, 2.5],
            }
        },
    }
    assert extract_values_from_tree(tree_lists, "RED") == 3


def test_extract_from_tree_of_different_collections():
    tree_tuples = {
        1: {"RED", "BLUE"},
        2: {
            "embedded in 2nd": ["RED", "RED", "BLUE", {"RED": "BLUE"}],
        },
        3: {
            "embedded in 3rd": {
                "another": ({"RED", "BLUE"}, ["BLUE"], "BLUE"),
            }
        },
    }
    assert extract_values_from_tree(tree_tuples, "RED") == 4


def test_extract_from_tree_of_all_basic_types():
    tree_tuples = {
        1: ["RED", 1],
        2: {
            "embedded in 2nd": ["RED", False, "BLUE"],
        },
        3: {
            "embedded in 3rd": {
                "another": [[None, "RED"], True, 2.5, {"RED": "BLUE"}],
            }
        },
        4: 1,
        5: False,
        6: "BLUE",
    }
    assert extract_values_from_tree(tree_tuples, "RED") == 3
