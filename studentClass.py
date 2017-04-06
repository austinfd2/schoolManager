class Student:
	#base class for all students
	total_students = 0

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		Student.total_students += 1
		self.id = Student.total_students

	def display_student(self):
		print 'Id :' , self.id, ", Name :", self.first_name, self.last_name

student1 = Student("Austin", "Daelemans")

student1.display_student()