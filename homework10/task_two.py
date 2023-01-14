class ValidationError(Exception):
    pass


class Student:
    def __init__(self, surname, name, group_number, academic_progress):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.academic_progress = academic_progress

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, line):
        if not isinstance(line, str):
            raise ValidationError('name must be str')
        self._name = line

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, line):
        if not isinstance(line, str):
            raise ValidationError('surname must be str')
        self._surname = line


class School:
    def __init__(self):
        self.list_of_students = list()

    def add_students(self, student):
        self.list_of_students.append(student)

    def get_best_students(self):
        for student in self.list_of_students:
            is_student_best = True
            for element in student.academic_progress:
                if element != 5 and element != 6:
                    is_student_best = False
            if is_student_best is True:
                print(f'{student.surname}, {student.group_number}')

    def get_students(self, group_number):
        for student in self.list_of_students:
            if student.group_number == group_number:
                print(f'{student.name} {student.surname}')

    def get_students_without_exams(self):
        for student in self.list_of_students:
            middle_value = 0
            for element in student.academic_progress:
                middle_value += element
            if middle_value/5 >= 7:
                print(f'{student.surname}, {student.group_number}')


A = Student('Alex', 'Mohi', 222, [6, 5, 9, 7, 8])
B = Student('Denis', 'Somow', 111, [2, 4, 5, 6, 8])
C = Student('Andry', 'Koh', 333, [5, 6, 6, 5, 5])
D = School()
D.add_students(A)
D.add_students(B)
D.add_students(C)
D.get_best_students()
D.get_students_without_exams()
D.get_students(222)
