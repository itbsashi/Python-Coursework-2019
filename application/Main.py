from Student import *
from Center import *

student1 = Student("Aleksandar Kanchev", 17311042, "CITN", 6)
student2 = Student("Marin Karabulev", 1735132, "CITN", 4)
student4 = Student("Mandarinka Hlebova", 1783455, "CIUN", 3)

CITN_students = [student1, student2]
CIUN_students = [student4]

CITN = Center(CITN_students, "CITN", "Radostin Dolchinkov")
CIUN = Center(CIUN_students, "CIUN", "Iuliq Yorgova")

student3 = Student("Iliqna Bakalova", 3525534, "CITN", 5.5)
CITN.add_student(student3)

# Проверява дали студентите са годни за стипендия.
CITN.print_scholarship()


def get_center_average(students_list):
    grade = 0
    number_of_students = 0
    for student in students_list:
        grade = grade + float(student.grade)
        number_of_students += 1
    round_num = round((grade / number_of_students), 2)
    print("\n" + str(round_num))


get_center_average(CITN_students)
