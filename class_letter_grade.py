class Letter_Processor:
    def __init__(self, filename):
        self.filename = filename
        self.student_name = []
        self.grades = []
        self.grades_dist = {}
    def read_file(self):
        with open(self.filename, 'rt') as f:
            lines = f.readlines()
        return lines
    def process_dta(self, lines):
        for line in lines:
            name, grade = line.strip().split(',')
            self.student_name.append(name)
            self.grades.append(int(grade))
    def create_grade_dict(self):
        return dict(zip(self.student_name, self.grades))
    def letter_grade_value(self, grade_dict):
        for value in grade_dict.values():
            if value >= 90:
                grade_letter="A"
            elif value >= 80:
                grade_letter="B"
            elif value >= 70:
                grade_letter="C"
            elif value >= 60:
                grade_letter="D"
            else:
                grade_letter="F"
            if grade_letter in self.grades_dist:
                self.grades_dist[grade_letter] += 1
            else:
                self.grades_dist[grade_letter] = 1
    def process_grades(self):
        lines=self.read_file()
        self.process_dta(lines)
        grade_dict=self.create_grade_dict()
        self.letter_grade_value(grade_dict)
    def get_grade_dist(self):
        return self.grades_dist

if __name__ == '__main__':
   file_handling = Letter_Processor("students_grades.csv")
   file_handling.process_grades()
   print(file_handling.get_grade_dist())




