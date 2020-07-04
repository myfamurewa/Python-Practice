class Student:
    def __init__(self, name, major, gpa, is_on_probation, year):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        self.year = year
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    def is_upperclassmen(self):
        if self.year > 2:
            return True
        else:
            return False

class Professor:
    def __init__(self, name, field, tenured, years):
        self.name = name
        self.field = field
        self.tenured = tenured
        self.years = years
