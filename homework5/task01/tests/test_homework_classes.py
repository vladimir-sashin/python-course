import datetime
from unittest.mock import Mock, patch

from homework5.task01 import Student, Teacher


def preconditions(
    teacher_lastname, teacher_firstname, student_lastname, student_firstname
):
    """Auxiliary function for tests. It initializes teacher and student instances"""
    return Teacher(teacher_lastname, teacher_firstname), Student(
        student_lastname, student_firstname
    )


def teacher_creates_homework(*args, teacher, homework_text, deadline):
    """Auxiliary function for tests. Teacher creates homework object at specified time."""
    # mock datetime.datetime object
    datetime_mock = Mock(wraps=datetime.datetime)
    # set return_value for 'now' method of mocked datetime.datetime - this will be a date when teacher created a HW
    datetime_mock.now.return_value = datetime.datetime(*args)
    # patch original datetime.datetime with mock
    with patch("datetime.datetime", new=datetime_mock):
        # teacher creates homework with deadline in days
        return teacher.create_homework(homework_text, deadline)


def student_submits_homework(*args, student, homework):
    """Auxiliary function for tests. Student submits homework at specified time."""
    # mock datetime.datetime object
    datetime_mock = Mock(wraps=datetime.datetime)
    # set the date when student submitted the homework
    datetime_mock.now.return_value = datetime.datetime(*args)
    # patch original datetime.datetime with mock
    with patch("datetime.datetime", new=datetime_mock):
        # student submits the homework
        return student.do_homework(homework)


def test_homework_expired(capsys):
    """Test for Homework, Teacher and Student classes
    Case: homework is submitted after deadline
    Expected result: 'You are late' printed to stdout, None is returned by 'student.do_homework(homework)'
    """
    teacher, student = preconditions(
        "Teacher lastname", "Teacher firstname", "Student lastname", "Student firstname"
    )
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 3, 12, 0, 1, student=student, homework=homework
    )
    # catch stdout
    captured = capsys.readouterr()
    assert (captured.out, result) == ("You are late\n", None)


def test_homework_in_time(capsys):
    """Test for Homework, Teacher and Student classes
    Case: homework is submitted before deadline
    Expected result: Nothing is printed to stdout, 'homework' object is returned by 'student.do_homework(homework)'"""
    teacher, student = preconditions(
        "Teacher lastname", "Teacher firstname", "Student lastname", "Student firstname"
    )
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 23, 59, 59, student=student, homework=homework
    )
    # catch stdout
    captured = capsys.readouterr()
    assert (captured.out, result) == ("", homework)


def test_homework_expired_edge_case(capsys):
    """Test for Homework, Teacher and Student classes Case: homework is submitted at the moment of deadline
    Expected result: 'Homework is expired: You are late' printed to stdout, None is returned by
    'student.do_homework(homework)'"""
    teacher, student = preconditions(
        "Teacher lastname", "Teacher firstname", "Student lastname", "Student firstname"
    )
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 3, 12, student=student, homework=homework
    )
    # catch stdout
    captured = capsys.readouterr()
    assert (captured.out, result) == ("You are late\n", None)
