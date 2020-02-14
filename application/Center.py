from Student import *


class Center:
    def __init__(self, student_list, center_name, dean):
        self.student_list = student_list
        self.center_name = center_name
        self.dean = dean

    def print_scholarship(self):
        for student in self.student_list:
            print("Checking student " + student.name + " for scholarship: ")
            print(student.get_scholarship())

    def add_student(self, name):
        self.student_list.append(name)