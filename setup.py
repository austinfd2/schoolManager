import sys
import MySQLdb

args = sys.argv[1:]
def main():
	if args[0] == "--help":
		print "Format Expected: setup.py [-createdb][-removedb] db_address admin_username admin_password db_name"						
		sys.exit(1)

	if len(args) != 5:
		print "ERROR: Incorrect amount of arguments expected 5 got", len(args)
		print "Please use [--help] for Usage Info"
		sys.exit(1)

	if args[0] == '--createdb':
		cursor = create_connection(args)
		try:
			cursor.execute("CREATE DATABASE " + args[4] + ";")
		except:
			print "Unable to create database"
			print "Exiting ..."
			sys.exit(-1)
		print "Database created"

	if args[0] == '--removedb':
		cursor = create_connection(args)
		try:
			cursor.execute("DROP DATABASE `" + args[4] + "`;")
		except:
			print "Unable to remove database"
			print "Exiting ..."
			sys.exit(1)
		print "Database Removed"


def create_connection(args):
	try:
		db = MySQLdb.connect(args[1], args[2], args[3])
		cursor = db.cursor()
	except:
		print "Unable to Connect to Database. Please Check Credentials."
		sys.exit(1)
	print "mySQL Connection Sucessful!"
	return cursor

def create_db(cursor):
	pass

def check_db_connection(cursor):
	cursor.execute("SELECT VERSION()")
	results = cursor.fetchone()
	print results
	# Check if anything at all is returned
	if results:
		return True
	else:
		return False  

if __name__ == '__main__':
	main()

