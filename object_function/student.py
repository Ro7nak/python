class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
