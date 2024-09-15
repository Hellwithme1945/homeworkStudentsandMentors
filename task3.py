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
lecturer2.courses_attached += ['Python']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)

reviewer = Reviewer('Ольга', 'Соколова')
reviewer.courses_attached += ['Python', 'Git']

reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student1, 'Git', 9)
reviewer.rate_hw(student2, 'Python', 8)


print(reviewer)
print()

print(lecturer1)
print()
print(lecturer2)
print()

print(student1)
print()
print(student2)
print()

if student1 > student2:
    print(f"{student1.name} {student1.surname} учится лучше, чем {student2.name} {student2.surname}")
else:
    print(f"{student2.name} {student2.surname} учится лучше, чем {student1.name} {student1.surname}")
print()

if lecturer1 < lecturer2:
    print(f"{lecturer2.name} {lecturer2.surname} имеет более высокую среднюю оценку за лекции, чем {lecturer1.name} {lecturer1.surname}")
else:
    print(f"{lecturer1.name} {lecturer1.surname} имеет более высокую среднюю оценку за лекции, чем {lecturer2.name} {lecturer2.surname}")