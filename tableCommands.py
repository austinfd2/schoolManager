from studentClass import Student
from teacherClass import Staff, Teacher
import MySQLdb
import sys


arg = sys.argv[1:]
if arg[0] == "--createStudent":
	student1 = Student(arg[1], arg[2])
	student1.add_student_to_db()
	
if arg[0] == "--createStaff":
	staff = Staff(arg[1], arg[2])
	staff.add_staff_to_db()

if arg[0] == "--createClass":
	teacher = Teacher(arg[1], arg[2])
	teacher.create_class(arg[3])

if arg[0] == "--enroll":
	student = Student(arg[1], arg[2])
	student.enroll()


