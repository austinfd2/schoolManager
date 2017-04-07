import MySQLdb
import sys
import re

#open database connecti
def create_connection_from_file():
	f = open(".creds.txt", "r")
	lines = f.read().splitlines()
	args = []
	for line in lines:
		args.append(line.split('=',1)[1].strip())

	db = MySQLdb.connect(args[0], args[1], args[2], args[3])

	#prepare a cursor object 
	return db