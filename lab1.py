#input student numbers (n)
def Number_student():
    n = input("Enter number of students in the class: ")
    while not n.isdigit() or int(n) <= 0:
        print("Invalid input. Please enter a positive integer.")
        n = input("Enter number of students in the class: ")
    return int(n)

#Input each student's information
def Infor_students():
    n_student = Number_student()
    ListStudent = []
    for i in range (1, n_student + 1):
        name = input("Enter name of student {0}: ".format(i))
        id = input("Enter ID of student {0}: ".format(i))
        dob = input("Enter date of birth of student {0}: ".format(i))
        InforStudents = {"name": name, "id": id, "dob": dob}
        ListStudent.append(InforStudents)
    return ListStudent

#Input course numbers
def Number_courses():
    m = input("Enter number of courses: ")
    while not m.isdigit() or int(m) <= 0:
        print("Invalid input. Please enter a positive integer.")
        m = input("Enter number of courses: ")
    return int(m)

#Input each course's information
def Infor_courses():
    m_courses = Number_courses()
    ListCourses = []
    for i in range(1, m_courses + 1):
        course_id = input("Enter ID of course {0}: ".format(i))
        course_name = input("Enter name of course {0}: ".format(i))
        InforCourses = {"course_id": course_id, "course_name": course_name}
        ListCourses.append(InforCourses)
    return ListCourses

#Choose the course to input and show mark
def Select_course(ListCourses):
    print("Select a course:")
    for i, course in enumerate(ListCourses):
        print("{0}. {1} ({2})".format(i+1, course["course_name"], course["course_id"]))
    while True:
        choice = input("Enter course number: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(ListCourses):
            print("Invalid input. Please enter a number between 1 and {0}.".format(len(ListCourses)))
        else:
            break
    return ListCourses[int(choice)-1]["course_id"]

#Input mark for each student in corse lelected
def Input_mark(ListStudent, course_id):
    for student in ListStudent:
        print("Enter mark for {0} ({1}):".format(student["name"], student["id"]))
        while True:
            grade = input("{0}: ".format(course_id))
            if not grade.isdigit() or int(grade) < 0 or int(grade) > 20:
                print("Invalid input. Please enter a number between 0 and 20.")
            else:
                break
        student[course_id] = int(grade)

#Solving the problem and print mark of studen in course selected
def main():
    ListStudent = Infor_students()
    ListCourses = Infor_courses()
    course_id = Select_course(ListCourses)
    Input_mark(ListStudent, course_id)
    for student in ListStudent:
        grade = student.get(course_id, None)
        if grade is None:
            print("{0} ({1}): No grade available for {2}.".format(student["name"], student["id"], course_id))
        else:
            print("{0} ({1}): {2} = {3}".format(student["name"], student["id"], course_id, grade))
main()