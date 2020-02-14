from Center import Center


class Student:
    def __init__(self, name, ID, center, grade):
        self.name = name
        self.ID = ID
        self.center = center
        self.grade = grade

    def get_scholarship(self):
        if self.grade > 4.5:
            print("Congratulations! " + self.name + " is suitable for a scholarship.")
            return "\n"
        else:
            print(self.name + " is not suitable for a scholarship. Study more.")
            return "\n"