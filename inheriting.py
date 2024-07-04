from mod_cgrade import Letter_Processor
import csv

class MyInheritedOne(Letter_Processor):
    def __init__(self, filename):
        super().__init__(filename)

    def letter_grade(self, grade):
        if grade >= 40:
            return "A"
        elif grade >= 30:
            return "B"
        elif grade >= 20:
            return "C"
        else:
            return "F"

    def add_letter_grades_to_csv(self, output_filename):
        self.process_grades()
        grade_dict = self.create_grade_dict()

        # Create modified lines with letter grades
        modified_lines = []
        for name, grade in grade_dict.items():
            letter_grade = self.letter_grade(grade)
            modified_line = f"{name},{grade},{letter_grade}\n"
            modified_lines.append(modified_line)

        # Write the modified lines to the output file
        with open(output_filename, 'wt') as file:
            file.writelines(modified_lines)

my_obj = MyInheritedOne("students_grades.csv")
my_obj.add_letter_grades_to_csv("students_grades.csv")
print(my_obj.get_grade_dist())

