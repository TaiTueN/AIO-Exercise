from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f'Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}')


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = []

    def add_person(self, person):
        self.__list_people.append(person)

    def describe(self):
        print(f'Ward Name: {self.__name}')
        for per in self.__list_people:
            per.describe()

    def count_doctor(self):
        counter = 0
        for per in self.__list_people:
            if isinstance(per, Doctor):
                counter += 1
        return counter

    def sort_age(self):
        self.__list_people.sort(key=lambda per: per.get_yob(), reverse=True)

    def compute_average(self):
        counter = 0
        total = 0
        for per in self.__list_people:
            if isinstance(per, Teacher):
                counter += 1
                total += per.get_yob()
        return total / counter


# 2a
student1 = Student(name='studentA', yob=2010, grade='7')
student1.describe()

teacher1 = Teacher(name='teacherA', yob=1969, subject='Math')
teacher1.describe()

doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
doctor1.describe()

# 2b
print()
teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')
ward1 = Ward(name='Ward1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2c
print(f'\nNumber of doctors: {ward1.count_doctor()}')

# 2d
print('\nAfter sorting Age of Ward1 people')
ward1.sort_age()
ward1.describe()

# 2e
print(f'\nAverage year of birth (teachers): {ward1.compute_average()}')
