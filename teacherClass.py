from globalFunctionRepo import create_connection_from_file
import sys

class Staff():
	#base class for all Faculty
	db = create_connection_from_file()
	cursor = db.cursor()
	#base class for all students
	teacher_id = cursor.execute("SELECT * FROM STAFF;")

	def __init__(self, first_name, last_name):
		self.last_name = last_name
		self.first_name = first_name
		self.id = Staff.teacher_id + 1

	def add_staff_to_db(self):
		sqlstring = """INSERT INTO STAFF (ID, FIRST, LAST) VALUES ({0},'{1}','{2}');"""
		result = Staff.cursor.execute(sqlstring.format(self.id,self.first_name,self.last_name))
		Staff.db.commit()
		if result:
			print "Success: Staff", self.first_name, self.last_name, "Created"
		else:
			print "Error"
		
		Staff.db.close()

class Teacher(Staff):

	def create_class(self, subject):
		try:
			class_id = Staff.cursor.execute("SELECT * FROM CLASSES;")
			sql = "INSERT INTO CLASSES (CLASS_ID, CLASS_NAME, TEACHER_FIRST, TEACHER_LAST) VALUES ({0}, '{1}', '{2}','{3}');"
			result = Staff.cursor.execute(sql.format(class_id, subject, self.first_name, self.last_name))
			sql = "CREATE TABLE `{0}_{1}` (STUDENT_FIRST TEXT, STUDENT_LAST TEXT, GRADE INT);"
			result = Staff.cursor.execute(sql.format(subject, class_id))
		except:
				print "Error: Failed To create Class"
				sys.exit(1)
		Staff.db.commit()
		print "Class Added"
		Staff.db.close()

	def set_grade(self):
		sql = "SELECT * FROM CLASSES WHERE TEACHER_FIRST='{0}' and TEACHER_LAST='{1}';".format(self.first_name, self.last_name)
		Teacher.cursor.execute(sql)
		results = Teacher.cursor.fetchall()
		print "Your Classes:"
		print 'Results:' , len(results)
		if len(results) == 0:
			print "No Classes Found."
			sys.exit(1)
		for row in results:
			print '(' + str(row[0]) + ')' , row[1] , ':', row[2], row[3]
		class_id = raw_input("Which Class ID Would you like to enter grades for? \n")
		target = []
		for row in results:
			if str(row[0]) == class_id:
				target.append(class_id)
				target.append(row[1])
		if not target:
			print "Invalid Class Code"
			sys.exit(1)
		print "Students in", target[1], target[0]
		sql = "SELECT * FROM {0}_{1};"
		Teacher.cursor.execute(sql.format(target[1],target[0]))
		results = Teacher.cursor.fetchall()
		for row in results:
			print row
		name = raw_input("Whose grade would you like to change? \n").split()
		found = False
		for row in results:
			if name[0] == row[0] and name[1] == row[1]:
				found = True
		if not found:
			print "Incorrect Name: Please Try again"
			sys.exit(1)
		grade = raw_input("What is this students grade?\n")
		sql = "UPDATE {0}_{1} SET GRADE={2} WHERE STUDENT_FIRST='{3}' AND STUDENT_LAST='{4}'"
		try:
			Teacher.cursor.execute(sql.format(target[1],target[0], int(grade), name[0], name[1]))
		except:
			"Unable to Enter Grade"
			sys.exit(1)
		Teacher.db.commit()
		print "Grade Entered"

