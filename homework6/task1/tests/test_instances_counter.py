from homework6.task1 import instances_counter


def initialize_test_class():
    @instances_counter
    class User:
        """Test class to be decorated by 'instances_counter'"""

        def __init__(self):
            self.username = "username"

        def print_arg(self, message):
            print(message)

    return User


def test_get_created_instances_no_instances():
    """Test for 'instances_counter' decorator:
    There are no instances of decorated class
    Expected result: decorated class has 'get_created_instances' method that returns 0"""
    user_class = initialize_test_class()
    assert user_class.get_created_instances() == 0


def test_get_created_instances_when_instances_exist():
    """Test for 'instances_counter' decorator:
    Create instances of decorated class
    Expected result: decorated class has 'get_created_instances' method that returns a number of instances"""
    user_class = initialize_test_class()
    user, _, _ = user_class(), user_class(), user_class()
    assert user.get_created_instances() == 3


def test_reset_instances_counter_when_counter_is_not_null():
    """Test for 'reset_instances_counter' decorator:
    Instances counter != 0
    Expected result: decorated class has 'reset_instances_counter' method that
        1. returns a number of instances
        2. makes instance counter = 0"""
    user_class = initialize_test_class()
    user, _, _ = user_class(), user_class(), user_class()
    assert (user.reset_instances_counter(), user.counter) == (3, 0)


def test_reset_instances_counter_when_counter_is_null():
    """Test for 'reset_instances_counter' decorator:
    Instances counter == 0
    Expected result: decorated class has 'reset_instances_counter' method that
        1. returns 0
        2. makes instance counter = 0"""
    user_class = initialize_test_class()

    assert (user_class.reset_instances_counter(), user_class.counter) == (0, 0)


def test_instances_counter_reset_counter_then_create_instance():
    """Test for 'instances_counter' decorator to check that methods 'get_created_instances' and
    'reset_instances_counter' can be sequentially called:
    Make instances of decorated class, reset counter, make 2 more instances and get number of created instances
    Expected result: 1 is returned"""
    user_class = initialize_test_class()
    user, _, _ = user_class(), user_class(), user_class()
    user_class.reset_instances_counter()
    user1, user2 = user_class(), user_class()
    assert user_class.get_created_instances() == 2


def original_class_attributes_are_available():
    """Test for 'instances_counter' decorator to check that attributes of original decorated class are available:
    Make an instance of decorated class and get it's attribute
    Expected result: original attribute value is returned"""
    user_class = initialize_test_class()
    user = user_class()
    assert user.username == "username"


def original_class_methods_are_available(capsys):
    """Test for 'instances_counter' decorator to check that methods of original decorated class are available:
    Make an instance of decorated class and call it's method with an argument
    Expected result: original method output is returned"""
    user_class = initialize_test_class()
    user = user_class()
    user.print_arg("test")
    captured = capsys.readouterr()
    assert captured.out == "test"
