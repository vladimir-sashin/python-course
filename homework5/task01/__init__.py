import datetime


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        return self.created + self.deadline > datetime.datetime.now()


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if not homework.is_active:
            print("You are late")
            return None
        else:
            return homework


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        return Homework(text, deadline)


teacher = Teacher("Teacher lastname", "Teacher firstname")
student = Student("Sashin", "Vladimir")
print(teacher.last_name)
print(student.first_name)

expired_homework = teacher.create_homework('Learn functions', 0)
print(expired_homework.created)
print(expired_homework.deadline)
print(expired_homework.text)

create_homework_too = teacher.create_homework
oop_homework = create_homework_too('create 2 simple classes', 0)
print(oop_homework.deadline)

student.do_homework(oop_homework)
student.do_homework(expired_homework)
