# Task 1
# School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def sallary(self, hour_rate, total_hours):
        self.hour_rate = hour_rate
        self.total_hours = total_hours
        if self.position == 'student' or self.position == Teacher:
            return 'This option is not available for student'
        else:
            if self.hour_rate < 40:
                salary = self.hour_rate * self.total_hours
                return salary
            elif self.hour_rate > 40:
                salary = ((self.total_hours - 40) * 1.5 * self.hour_rate) + (40 * self.hour_rate)
                return salary


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject, *classes, position='teacher', ):
        super().__init__(first_name, last_name, age, position)
        self.subject = subject
        self.classes = classes

    def add_class(self, *num_class):
        self.classes += num_class
        return sorted(self.classes)

    def delete_class(self, del_class):
        self.classes -= del_class
        return sorted(self.classes)


class Student(Person):
    def __init__(self, first_name, last_name, age, grade, position='student'):
        super().__init__(first_name, last_name, age, position)
        self.grade = grade


if __name__ == '__main__':
    person1 = Person('Ana', 'White', 15, 'layer')
    print(person1.first_name)
    print(person1.sallary(25, 40))

    person2 = Teacher('Mary', 'Brown', 31, 'Math', 5, 6, 7)
    print(person2.classes)
    print(person2.position)
    print(person2.sallary(35, 41))
    print(person2.add_class(11, 2))

    person3 = Student('Kate', 'Wiliams', 15, 9)
    print(person3.age)
    print(person3.grade)
    print(person3.position)
    print(person3.sallary(15, 16))
