from class_letter_grade import  Letter_Processor


#class my_inherited_one(Letter_Processor):
class my_inherited_one():
    pass


my_obj = my_inherited_one("students_grades.csv")

my_obj.process_grades()
print(my_obj.get_grade_dist())


