from globalFunctionRepo import create_connection_from_file

class Staff():
	#base class for all Faculty
	db = create_connection_from_file()
	cursor = db.cursor()
	#base class for all students
	teacher_id = cursor.execute("SELECT * FROM TEACHERS;")

	def __init__(self, first_name, last_name):
		self.last_name = last_name
		self.first_name = first_name
		self.id = Staff.teacher_id + 1

	def add_staff_to_db(self):
		sqlstring = """INSERT INTO TEACHERS (ID, FIRST, LAST) VALUES ({0},'{1}','{2}');"""
		result = Staff.cursor.execute(sqlstring.format(self.id,self.first_name,self.last_name))
		Staff.db.commit()
		if result:
			print "Success: Staff", self.first_name, self.last_name, "Created"
		else:
			print "Error"
		
		Staff.db.close()
