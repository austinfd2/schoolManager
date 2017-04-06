from studentClass import Student
import MySQLdb
import sys


arg = sys.argv[1:]
if arg[0] == "--createStudent":
	student1 = Student(arg[1], arg[2])
	student1.add_student_to_db()