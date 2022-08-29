import datetime
from models import *

with db:
	expenses = Expense.select()
	payments = [
		{'work_data':datetime.date(2022,8,20), 'expense_id':expenses[1]},
		{'work_data':datetime.date(2022,8,26), 'expense_id':expenses[2]},
		{'work_data':datetime.date(2022,8,23), 'expense_id':expenses[3]},
		{'work_data':datetime.date(2022,8,25), 'expense_id':expenses[2]},
		{'work_data':datetime.date(2022,8,22), 'expense_id':expenses[2]},
		{'work_data':datetime.date(2022,8,21), 'expense_id':expenses[4]

	}]
	Payment.insert_many(payments).execute()

print('DONE')