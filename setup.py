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
		create_db(cursor)
		create_tables(cursor)

		print "Database created"

	elif args[0] == '--removedb':
		cursor = create_connection(args)
		try:
			cursor.execute("DROP DATABASE `" + args[4] + "`;")
		except:
			print "Unable to remove database"
			print "Exiting ..."
			sys.exit(1)
		print "Database Removed"

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

def create_db(cursor):
	try:
		cursor.execute("CREATE DATABASE " + args[4] + ";")
	except:
		print "Unable to create database"
		print "Exiting ..."
		sys.exit(-1)

def create_tables(cursor):
	try:
		cursor.execute("""CREATE TABLE `STUDENTS` (ID PRIMARYINTEGER, FIRST TEXT, LAST TEXT, PRIMARY KEY (id)""")
		cursor.execute("""CREATE TABLE `TEACHERS` (ID PRIMARYINTEGER, FIRST TEXT, LAST TEXT, PRIMARY KEY (id)""")
	except



if __name__ == '__main__':
	main()

