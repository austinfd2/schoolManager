import sys
import MySQLdb

args = sys.argv[1:]
def main():
	if args[0] == "--help":
		print "Format Expected: setup.py [-createdb][-removedb] db_address admin_username admin_password db_name"						
		print "Please Provide login for accounts that have admin privledges"
		sys.exit(1)

	if len(args) != 5:
		print "ERROR: Incorrect amount of arguments expected 5 got", len(args)
		print "Please use [--help] for Usage Info"
		sys.exit(1)

	if args[0] == '--createdb':
		cursor = create_connection(args)
		create_db(cursor, args)
		create_tables(cursor, args)


	elif args[0] == '--removedb':
		cursor = create_connection(args)
		remove_database(cursor, args)

	elif args[0] == '--createconfig':
		create_connection_file(args)

	else:
		print "Unknown Command"
		sys.exit(1)


def create_connection(args):
	# Creates a connection to desired Db
	try:
		db = MySQLdb.connect(args[1], args[2], args[3])
		cursor = db.cursor()
	except:
		print "Unable to Connect to Database. Please Check Credentials."
		sys.exit(1)
	print "mySQL Connection Sucessful!"
	return cursor

def create_db(cursor, args):
	try:
		cursor.execute("CREATE DATABASE " + args[4] + ";")
	except:
		print "Unable to create database"
		print "Exiting ..."
		sys.exit(-1)
	print "Database Created!"

def remove_database(cursor, args):
	try:
		cursor.execute("DROP DATABASE `" + args[4] + "`;")
	except:
		print "Unable to remove database"
		print "Exiting ..."
		sys.exit(1)
	print "Database Removed"


def create_tables(cursor, args):
	try:
		cursor.execute("USE `{0}`;".format(args[4]))
		cursor.execute("CREATE TABLE `STUDENTS` (ID INTEGER, FIRST TEXT, LAST TEXT, PRIMARY KEY (id));")
		cursor.execute("CREATE TABLE `STAFF` (ID INTEGER, FIRST TEXT, LAST TEXT, PRIMARY KEY (id));")
		cursor.execute("CREATE TABLE `CLASSES` (CLASS_NAME TEXT, TEACHER_FIRST TEXT, TEACHER_LAST TEXT);")
	except:
		print "ERROR: Creating Tables"
		print "Reseting Database"
		remove_database(cursor, args)
		sys.exit(1)
	print "Tables: STUDENTS, TEACHERS, CLASSES added"

def create_connection_file(args):
	print "A connection file will be created with these login credentials. This prevents users from needing to enter credentials on all operations."
	f = open(".creds.txt", "w")
	f.write("ADDR={0} \n".format(args[1]))
	f.write("USERNAME={0} \n".format(args[2]))
	f.write("PASSWORD={0} \n".format(args[3]))
	f.write("DATABASE={0}".format(args[4]))
	f.close()





if __name__ == '__main__':
	main()

