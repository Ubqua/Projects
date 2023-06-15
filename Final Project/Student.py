# Ubqua Jilani
# 1965370

import csv


# Listing all attributes for a student in a class
class Student:
    def __init__(self, student_id, LastName, FirstName, Major, Graduation="", GPA=0.0, Disciplinary=""):
        self.student_id = student_id
        self.last_name = LastName
        self.first_name = FirstName
        self.major = Major
        self.disciplinary = Disciplinary
        self.gpa = GPA
        self.graduation_date = Graduation

# From Student CSV file


# Prints all files in each major in order
def write_majors(filename, list_of_objects):
    with open(filename, 'a', newline="") as newfile:
        newfile.truncate(0)
        writer = csv.writer(newfile)
        for each in list_of_objects:
            data = [each.student_id, each.last_name, each.first_name, each.graduation_date, each.disciplinary]  # this is how the csv file will be displayed
            writer.writerow(data)


# Filtering and adds each student with their gpa
def add_gpa(list_, id_, gpa):
    for each in list_:
        if each.student_id == id_:
            each.gpa = gpa


# Writing a csv files with file title and list of data
def write_files(file_titile, list_of_data):
    with open(file_titile, 'a', newline="") as file:
        file.truncate(0)
        writer = csv.writer(file)
        for each in list_of_data:
            data = [each.student_id, each.major, each.first_name, each.last_name, each.gpa, each.graduation_date,
                    each.disciplinary]  # Listing all attributes of the student
            writer.writerow(data)


# Add graduations dates to each student
def add_graduation(list_, id_, date_):
    for each in list_:
        if each.student_id == id_:
            each.graduation_date = date_


# Outputting a signal file with scholarship candidates with student information
def write_scholarship_candidates(list_of_students):
    with open("ScholarshipCandidates.csv", 'a', newline="") as students_file:
        students_file.truncate(0)
        writer = csv.writer(students_file)
        for each in list_of_students:
            data = [each.student_id, each.last_name, each.first_name, each.major, each.gpa]  # Students information output in order
            writer.writerow(data)


# Outputting a signal file with disciplined student with student information
def create_disciplined_students(filtered_list):
    with open("DisciplinedStudents.csv", 'a', newline="") as file:
        file.truncate(0)
        writer = csv.writer(file)
        for each in filtered_list:
            data = [each.student_id, each.last_name, each.first_name, each.graduation_date]  # Student information output including graduation date
            writer.writerow(data)

