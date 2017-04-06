import MySQLdb
import sys
#open database connection



db = MySQLdb.connect("localhost", "root", "Faulkner7", "db")

#prepare a cursor object 
cursor = db.cursor()


class Student:
	#base class for all students
	student_id = cursor.execute("SELECT * FROM STUDENTS;")
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.id = Student.student_id + 1

	def display_student(self):
		print 'Id :' , self.id, ", Name :", self.first_name, self.last_name

	def add_student_to_db(self):
		sqlstring = """INSERT INTO STUDENTS (ID, FIRST, LAST) VALUES ({0},'{1}','{2}');"""
		result = cursor.execute(sqlstring.format(self.id,self.first_name,self.last_name))
		if result:
			print "Success: Student", self.first_name, self.last_name, "Created"
		else:
			print "Error"
		db.commit()
		db.close()




