import sqlite3

def get_statistic_houer():
	all_houer = []
	with sqlite3.connect('db/database.db') as db:
		cursor = db.cursor()
		query = """ SELECT SUM(houers) as Houers FROM expense """
		cursor.execute(query)
		all_houer = cursor
		print(all_houer)