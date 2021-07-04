import datetime
from unittest.mock import Mock, patch

import pytest

from homework6.task2 import DeadlineError, HomeworkResult, Student, Teacher


def create_teacher(teacher_lastname, teacher_firstname):
    """Auxiliary function for tests. It initializes a teacher instance"""
    return Teacher(teacher_lastname, teacher_firstname)


def create_student(student_lastname, student_firstname):
    """Auxiliary function for tests. It initializes a student instance"""
    return Student(student_firstname, student_lastname)


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


def student_submits_homework(*args, student, homework, solution):
    """Auxiliary function for tests. Student submits homework at specified time."""
    # mock datetime.datetime object
    datetime_mock = Mock(wraps=datetime.datetime)
    # set the date when student submitted the homework
    datetime_mock.now.return_value = datetime.datetime(*args)
    # patch original datetime.datetime with mock
    with patch("datetime.datetime", new=datetime_mock):
        # student submits the homework
        return student.do_homework(homework, solution)


def test_correct_homework_done_in_time():
    """Case - happy flow: correct homework (solution is >6 characters long) is submitted before deadline, result is
    checked by a teacher, stored result is accessed by 'Teacher' class
    Expected result:
        True is returned by 'teacher.check_homework(result)'
        Result is added to Teacher.homework_done defaultdict"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework, solution="test solution"
    )
    assessment = teacher.check_homework(result)
    homework_stored = Teacher.homework_done[homework]
    assert (assessment, homework_stored) == (True, {result})


def test_correct_homework_done_in_time_edge_deadline():
    """Case: correct homework (solution is >6 characters long) is submitted in 1 second before deadline,
    result is checked by a teacher, stored result is accessed by 'Teacher' class
    Expected result:
        True is returned by 'teacher.check_homework(result)'
        Result is added to Teacher.homework_done defaultdict"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021,
        7,
        2,
        23,
        59,
        59,
        student=student,
        homework=homework,
        solution="test solution",
    )
    assessment = teacher.check_homework(result)
    homework_stored = Teacher.homework_done[homework]
    assert (assessment, homework_stored) == (True, {result})


def test_correct_homework_done_in_time_correctness_edge_case():
    """Case: correct homework (solution is 6 characters long) is submitted before deadline, result is checked by a
    teacher, stored result is accessed by 'Teacher' class
    Expected result:
        True is returned by 'teacher.check_homework(result)'
        Result is added to Teacher.homework_done defaultdict"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework, solution="123456"
    )
    assessment = teacher.check_homework(result)
    homework_stored = Teacher.homework_done[homework]
    assert (assessment, homework_stored) == (True, {result})


def test_homework_expired():
    """Case: homework is submitted after deadline
    Expected result: 'DeadlineError' is raised on 'student.do_homework(homework) call'
    """
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    with pytest.raises(DeadlineError) as exc_info:
        student_submits_homework(
            2021,
            7,
            3,
            12,
            0,
            1,
            student=student,
            homework=homework,
            solution="test solution",
        )
    assert str(exc_info.value) == "You are late"


def test_homework_expired_edge_case():
    """Case: homework is submitted at the moment of deadline
    Expected result: 'DeadlineError' is raised on 'student.do_homework(homework) call'
    """
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    with pytest.raises(DeadlineError) as exc_info:
        student_submits_homework(
            2021,
            7,
            3,
            12,
            student=student,
            homework=homework,
            solution="test solution",
        )
    assert str(exc_info.value) == "You are late"


def test_incorrect_homework():
    """Case: incorrect homework (solution is < 5 characters long) is submitted before deadline, result is
    checked by a teacher, result is not stored
    Expected result:
        False is returned by 'teacher.check_homework(result)'
        Result is not added to Teacher.homework_done"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework, solution="123"
    )
    assessment = teacher.check_homework(result)
    homework_stored = Teacher.homework_done[homework]
    assert (assessment, homework_stored) == (False, set())


def test_incorrect_homework_edge_case():
    """Case: incorrect homework (solution is = 5 characters long) is submitted before deadline, result is
    checked by a teacher, result is not stored
    Expected result:
        False is returned by 'teacher.check_homework(result)'
        Result is not added to Teacher.homework_done defaultdict"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework, solution="12345"
    )
    assessment = teacher.check_homework(result)
    homework_stored = Teacher.homework_done[homework]
    assert (assessment, homework_stored) == (False, set())


def test_result_of_different_homeworks_are_stored():
    """Case: Student submits different correct homeworks
    Expected result: Results of all homeworks are added to Teacher.homework_done"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework1 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result1 = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework1, solution="1234567"
    )
    homework2 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="OOP", deadline=3
    )
    result2 = student_submits_homework(
        2021, 7, 2, 13, student=student, homework=homework2, solution="1234567"
    )
    teacher.check_homework(result1)
    teacher.check_homework(result2)
    homework1_stored = Teacher.homework_done[homework1]
    homework2_stored = Teacher.homework_done[homework2]
    assert (homework1_stored, homework2_stored) == ({result1}, {result2})


def test_different_results_of_one_homework_are_stored():
    """Case: Student submits different correct results for one homework
    Expected result: All results are added to Teacher.homework_done[homework]"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework1 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result1 = student_submits_homework(
        2021,
        7,
        2,
        12,
        student=student,
        homework=homework1,
        solution="this is solution #1",
    )
    result2 = student_submits_homework(
        2021,
        7,
        2,
        13,
        student=student,
        homework=homework1,
        solution="this is solution #2",
    )
    teacher.check_homework(result1)
    teacher.check_homework(result2)
    homework1_stored = Teacher.homework_done[homework1]
    assert homework1_stored == {result1, result2}


def test_results_may_be_accessed_by_any_teacher():
    """Case: Teacher #1 checks homeworks' results, teachers #1 and #2 both accesses them
    Expected result: Homework results may be accessed by both teachers"""
    teacher1 = create_teacher("Teacher 1 lastname", "Teacher 1 firstname")
    teacher2 = create_teacher("Teacher 2 lastname", "Teacher 2 firstname")
    student = create_student("Student lastname", "Student firstname")
    homework1 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher1, homework_text="Learn functions", deadline=2
    )
    result1 = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework1, solution="1234567"
    )
    homework2 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher1, homework_text="OOP", deadline=3
    )
    result2 = student_submits_homework(
        2021, 7, 2, 13, student=student, homework=homework2, solution="1234568"
    )
    teacher1.check_homework(result1)
    teacher1.check_homework(result2)
    homework1_stored = teacher1.homework_done[homework1]
    homework2_stored = teacher2.homework_done[homework2]
    assert (homework1_stored, homework2_stored) == ({result1}, {result2})


def test_results_may_be_checked_by_any_teacher():
    """Case: Teacher #1 creates homework, student submits it, teacher #2 checks the results
    Expected result: Teacher #2 accesses results stored in Teacher.homework_done checked by teacher #1"""
    teacher1 = create_teacher("Teacher 1 lastname", "Teacher 1 firstname")
    teacher2 = create_teacher("Teacher 2 lastname", "Teacher 2 firstname")
    student = create_student("Student lastname", "Student firstname")
    homework = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher1, homework_text="Learn functions", deadline=2
    )
    result = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework, solution="1234567"
    )
    assert teacher2.check_homework(result)


def test_reset_homework_results():
    """Case: There are results in Teacher.homework_done, Teacher.reset_results() is called with homework in arguments
    Expected result:
        All results of passed in Teacher.reset_results() homework are deleted from Teacher.homework.done
        Results of other homeworks are not deleted"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework1 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result1 = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework1, solution="1234567"
    )
    homework2 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="OOP", deadline=3
    )
    result2 = student_submits_homework(
        2021, 7, 2, 13, student=student, homework=homework2, solution="1234567"
    )
    teacher.check_homework(result1)
    teacher.check_homework(result2)
    Teacher.reset_results(homework1)
    assert (
        Teacher.homework_done.get(homework1),
        Teacher.homework_done.get(homework2),
    ) == (None, {result2})


def test_reset_all_homework_results():
    """Case: There are results in Teacher.homework_done, Teacher.reset_results() is called with homework in arguments
    Expected result:
        All results of passed in Teacher.reset_results() homework are deleted from Teacher.homework.done
        Results of other homeworks are not deleted"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    homework1 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="Learn functions", deadline=2
    )
    result1 = student_submits_homework(
        2021, 7, 2, 12, student=student, homework=homework1, solution="1234567"
    )
    homework2 = teacher_creates_homework(
        2021, 7, 1, 12, teacher=teacher, homework_text="OOP", deadline=3
    )
    result2 = student_submits_homework(
        2021, 7, 2, 13, student=student, homework=homework2, solution="1234567"
    )
    teacher.check_homework(result1)
    teacher.check_homework(result2)
    Teacher.reset_results()
    assert (
        Teacher.homework_done.get(homework1),
        Teacher.homework_done.get(homework2),
    ) == (None, None)


def test_homework_result_exception():
    """Case: HomeworkResult instance gets not a homework object
    Expected result: TypeError exception with 'You gave a not Homework object' message is raised"""
    teacher = create_teacher("Teacher lastname", "Teacher firstname")
    student = create_student("Student lastname", "Student firstname")
    with pytest.raises(TypeError) as exc_info:
        HomeworkResult(student, teacher, "solution")
    assert str(exc_info.value) == "You gave a not Homework object"
