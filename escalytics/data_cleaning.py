'''Data cLeaning of the users. Users which belongs in the departments 117 or 129,
or with no department at all, can be disconsidered
if this .py is run, the result will be a test of its operation. To use it outside
here, import the method data_cleaning(ids)
'''

###### IMPORTS
import numpy as np
import pandas as pd
import MySQLdb

###### CONSTANTS
FAKE_DEPTS = [117,129, 130, 133, 134]

def connect():
	''' (None) -> MySQL connection
	connects with database'''

	MYSQL_CN = MySQLdb.connect(
    	host='escala-prod.cj95rai4gddz.us-west-2.rds.amazonaws.com',
    	port=3306,
    	user='analiseUser',
    	passwd='5z844bi3gEAU',
    	db='ebdb'
	)

	return MYSQL_CN


def disconnect(base):
	'''(MySQL connection) -> None
	disconects with database'''
	base.close()


def data_cleaning(ids):
	'''(Series) -> Series
	gets a series of employees id and returns the IDs that are not in the departments 117
	or 129, and the IDs that has at least one department'''

	base = connect()
	real_ids = pd.Series()
	departments = pd.read_sql('select employee_id, department_id from departments_employees;', con=base)

	for ID in ids.values:
		depts = departments[departments.employee_id == ID].department_id.values
		if not (any(dept in depts or dept > 134 for dept in FAKE_DEPTS) or len(depts) == 0 or np.isnan(ID)):
			newID = pd.Series(ID)
			real_ids = real_ids.append(newID, ignore_index=True)

	disconnect(base)

	return real_ids

def test():

	base = connect()
	employees = pd.read_sql('select id from employees;', con=base).id
	print employees
	disconnect(base)
	real_ids = data_cleaning(employees)
	print real_ids

