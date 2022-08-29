from peewee import *


db = SqliteDatabase('db/database.db')

class BaseModel(Model):
	id = PrimaryKeyField(unique = True)

	class Meta:
		database = db
		order_by = 'id'

class Expense(BaseModel):
	name = CharField()
	start_shift = TimeField()
	finish_shift = TimeField()
	houers = TextField()

	class Meta:
		db_table = 'expense'

class Payment(BaseModel):
	work_data = DateField()
	selery = TimeField()

	class Meta:
		db_table = 'payments'
