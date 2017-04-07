import MySQLdb
import sys
import re
from globalFunctionRepo import create_connection_from_file



class Student:
	db = create_connection_from_file()
	cursor = db.cursor()
	#base class for all students
	student_id = cursor.execute("SELECT * FROM STUDENTS;")
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.id = Student.student_id + 1
		print "Student: ", self.first_name, self.last_name

	def display_student(self):
		print 'Id :' , self.id, ", Name :", self.first_name, self.last_name

	def add_student_to_db(self):
		sqlstring = """INSERT INTO STUDENTS (ID, FIRST, LAST) VALUES ({0},'{1}','{2}');"""
		result = Student.cursor.execute(sqlstring.format(self.id,self.first_name,self.last_name))
		Student.db.commit()
		if result:
			print "Success: Student", self.first_name, self.last_name, "Created"
		else:
			print "Error"
		Student.db.close()

	def enroll(self):
		class_name = raw_input("What is the name of the Class? \n")
		sql = "SELECT * FROM CLASSES WHERE CLASS_NAME='{0}';".format(class_name)
		Student.cursor.execute(sql)
		print Student.cursor.fetchall()

		



