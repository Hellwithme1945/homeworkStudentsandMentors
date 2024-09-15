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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = self._calculate_average_grade()
        res = f"Лектор\nИмя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {average_grade:.2f}"
        return res

    def _calculate_average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0


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
        res = f"Проверяющий\nИмя: {self.name}\nФамилия: {self.surname}"
        return res

student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress += ['Python', 'Git']

student2 = Student('Мария', 'Петрова', 'женский')
student2.courses_in_progress += ['Python']

lecturer1 = Lecturer('Алексей', 'Смирнов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Елена', 'Кузнецова')
lecturer2.courses_attached += ['Git']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 9)

reviewer = Reviewer('Ольга', 'Соколова')
reviewer.courses_attached += ['Python', 'Git']

reviewer.rate_hw(student1, 'Python', 10)
reviewer.rate_hw(student1, 'Git', 9)
reviewer.rate_hw(student2, 'Python', 8)
reviewer.rate_hw(student2, 'Git', 7)

print(lecturer1)
print()
print(lecturer2)
print()

print(f"Оценки студента {student1.name} {student1.surname}: {student1.grades}")
print(f"Оценки студента {student2.name} {student2.surname}: {student2.grades}")