import sqlite3

def get_statistic_houer():
	all_houer = []
	with sqlite3.connect('db/database.db') as db:
		db.row_factory = sqlite3.Row
		cursor = db.cursor()
		query = """ SELECT SUM(houers) FROM expense """
		cursor.execute(query)
		all_houer = cursor
	return all_houer