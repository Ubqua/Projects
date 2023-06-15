# Ubqua Jilani
# 1965370

# import Student class, and other functions from Student module
from student import Student, add_gpa, add_graduation, write_files, write_scholarship_candidates, \
    create_disciplined_students, write_majors
import csv
import datetime


# define main function
def main():
    # define students and major list
    students = []
    majors = []

    # Define student majors list
    filename = "StudentsMajorsList.csv"
    try:
        # open StudentMajors file
        with open(filename) as file:
            reader = csv.reader(file)
            for each in reader:
                majors.append(each[3])  # Add to each students list
                obj = Student(student_id=each[0], last=each[1], first=each[2], major=each[3], disciplinary=each[4])
                students.append(obj)  # Students information in order
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please add {filename} to current directory")
        return

    # Open GPAList
    filename = "GPAList.csv"
    try:
        # adding gpa to each student list from using add_gpa from student.py
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                add_gpa(list_=students, id_=row[0], gpa=row[1])
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please add {filename} to current directory")
        return

    # Open GraduationDatesList
    filename = "GraduationDatesList.csv"
    try:
        # add graduation date using function add_graduation from student.py
        # student module
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                add_graduation(list_=students, id_=row[0], date_=row[1])
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please add {filename} to current directory")
        return

    # sort given data of objects by last_name
    def get_key(x):
        return x.last_name

    # Sort random keys
    students.sort(key=get_key)

    # Print Full Roster from getting the information from FullRoster.csv
    if len(students):
        write_files("FullRoster.csv", students)

    # helper function of student_id
    def get_key(x):
        return x.student_id

    # Creating a CSV file for each major
    for major in majors:
        filename = "".join(major.strip().split())
        filename += ".csv"
        filtered_list = [x for x in students if (x.major == major)]

        # Sorting each list by student_id
        filtered_list.sort(key=get_key)
        if len(filtered_list):
            write_majors(filename, filtered_list)

    # Filtering each student who are eligible
    filtered = [x for x in students if ((float(x.gpa) > 3.8) and (x.disciplinary != "Y"))]
    eligible = []
    today = datetime.datetime.today()

    # Sort each sata by student_id
    def get_key(x):
        return x.gpa

    # Check who have not graduated
    for each in filtered:
        graduation = datetime.datetime.strptime(each.graduation_date, "%m/%d/%Y")
        if graduation > today:
            eligible.append(each)
    eligible.sort(key=get_key, reverse=True)

    # Students eligible for a scholarship
    if len(eligible):
        write_scholarship_candidates(eligible)

    # Sorting given data of objects by graduation_date
    def get_key(x):
        return x.graduation_date

    # write a CSV file titled DisciplinedStudents
    filtered = [student for student in students if (student.disciplinary == "Y")]
    filtered.sort(key=get_key)
    if len(filtered):
        create_disciplined_students(filtered)


if __name__ == "__main__":
    main()
