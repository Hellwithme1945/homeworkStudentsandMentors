class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (
                isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached
        ):
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Ошибка: Оценка должна быть от 0 до 10.')
        else:
            print('Ошибка при выставлении оценки лектору.')

    def _calculate_average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        return total / count if count else 0

    def __str__(self):
        average_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}"
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить: объект не является студентом")
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить: объект не является студентом")
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calculate_average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        return total / count if count else 0

    def __str__(self):
        average_grade = self._calculate_average_grade()
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average_grade:.1f}"
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить: объект не является лектором")
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить: объект не является лектором")
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
                isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress
        ):
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                print('Ошибка: Оценка должна быть от 0 до 10.')
        else:
            print('Ошибка при выставлении оценки студенту.')

    def __str__(self):
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )
        return res

student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Мария', 'Петрова', 'женский')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']


lecturer1 = Lecturer('Алексей', 'Смирнов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Елена', 'Кузнецова')
lecturer2.courses_attached += ['Git']


reviewer1 = Reviewer('Ольга', 'Соколова')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Дмитрий', 'Попов')
reviewer2.courses_attached += ['Python']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)


reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)

print("Проверяющие:")
print(reviewer1)
print()
print(reviewer2)
print()

print("Лекторы:")
print(lecturer1)
print()
print(lecturer2)
print()

print("Студенты:")
print(student1)
print()
print(student2)
print()


if student1 > student2:
    print(f"{student1.name} {student1.surname} учится лучше, чем {student2.name} {student2.surname}")
elif student1 < student2:
    print(f"{student2.name} {student2.surname} учится лучше, чем {student1.name} {student1.surname}")
else:
    print(f"{student1.name} {student1.surname} и {student2.name} {student2.surname} учатся одинаково хорошо")
print()


if lecturer1 > lecturer2:
    print(f"{lecturer1.name} {lecturer1.surname} имеет более высокую среднюю оценку за лекции, чем {lecturer2.name} {lecturer2.surname}")
elif lecturer1 < lecturer2:
    print(f"{lecturer2.name} {lecturer2.surname} имеет более высокую среднюю оценку за лекции, чем {lecturer1.name} {lecturer1.surname}")
else:
    print(f"{lecturer1.name} {lecturer1.surname} и {lecturer2.name} {lecturer2.surname} имеют одинаковую среднюю оценку за лекции")
print()

def average_student_grade(students_list, course_name):
    total = 0
    count = 0
    for student in students_list:
        if course_name in student.grades:
            grades = student.grades[course_name]
            total += sum(grades)
            count += len(grades)
    if count == 0:
        return 0
    return total / count

def average_lecturer_grade(lecturers_list, course_name):
    total = 0
    count = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            grades = lecturer.grades[course_name]
            total += sum(grades)
            count += len(grades)
    if count == 0:
        return 0
    return total / count

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_student_python = average_student_grade(students_list, 'Python')
avg_student_git = average_student_grade(students_list, 'Git')

avg_lecturer_python = average_lecturer_grade(lecturers_list, 'Python')
avg_lecturer_git = average_lecturer_grade(lecturers_list, 'Git')

print(f"Средняя оценка за домашние задания по всем студентам в рамках курса Python: {avg_student_python:.2f}")
print(f"Средняя оценка за домашние задания по всем студентам в рамках курса Git: {avg_student_git:.2f}")
print()

print(f"Средняя оценка за лекции всех лекторов в рамках курса Python: {avg_lecturer_python:.2f}")
print(f"Средняя оценка за лекции всех лекторов в рамках курса Git: {avg_lecturer_git:.2f}")