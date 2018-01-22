import ast
import datetime as dt

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import MySQLdb
import pandas as pd 
from slackclient import SlackClient

from data_cleaning import data_cleaning, connect, disconnect
from mixpanel_data import Mixpanel

ESCALA_ANDROID = '2b7a4738c81462f1a47184db55b0e7a4'
ESCALA_IOS = '5a3e81bd96cb62d9862a3b22d559e363'

today = dt.date.today()
week = dt.timedelta(days=7)
last_week = today - week

test = {
	1:2,
	2:3,
	3:4,
	4:{
	5:6,
	8:20,
	33:2
	}
}
test2 = {1: test, 2: {1:9.3}}

#### GENERAL FUNCS
def str_to_dict(string):
	'''(str) -> list of dict'''

	curly_brackets = []
	dicts = []
	iter_before = 0
	for iter, char in enumerate(string):
		if char == '{':
			curly_brackets.append(False)
		elif char == '}':
			for i, opened_bracket in enumerate(reversed(curly_brackets)):
				if not opened_bracket:
					curly_brackets[-1 -i] = True
					break

		#print curly_brackets

		if len(curly_brackets) > 0:
			if curly_brackets[0]:
				#print iter, char
				curly_brackets = []
				str_dict = string[iter_before :iter + 1].strip()
				#print dt.datetime.now().time()
				try:
					dicts.append(ast.literal_eval(str_dict.encode('utf-8')))
				except ValueError:
					print 'deu erro'
					print str_dict
					return 0
				
				#print dt.datetime.now().time()
				iter_before = iter + 1

	return dicts

if __name__ == '__main__':


	#21196
	print today, last_week
	print dt.datetime.now().time()
	api = Mixpanel(ESCALA_ANDROID)
	'''string = api.request(['export'], raw=True, params={
		'from_date' : today,
		'to_date'   : today
		})
	print len(string)
	dicts = str_to_dict(string)
	print len(dicts)
	print dt.datetime.now().time()
	#print dicts'''

	string = '{}\n\n\n\n\n\n     {}     {}\n\t{}'.format(test, test2, test, test2)
	print string
	x = str_to_dict(string)
	print x, len(x)
