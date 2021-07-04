import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Exception that is raised if homework is expired"""


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        return self.created + self.deadline > datetime.datetime.now()


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active:
            homework.solution = solution
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.solution = solution
        self.author = author
        if isinstance(homework, Homework):
            self.homework = homework
            self.created = homework.created
        else:
            raise TypeError("You gave a not Homework object")


class Teacher(Person):
    homework_done = defaultdict(set)

    def create_homework(self, text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework="default"):
        if homework == "default":
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework)
