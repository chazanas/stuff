import ast

#import matplotlib
#matplotlib.use('TKAgg')
#import matplotlib.pyplot as plt
#import MySQLdb
#import pandas as pd 
#from slackclient import SlackClient

#from data_cleaning import data_cleaning, connect, disconnect
#from mixpanel_data import Mixpanel

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

		print(curly_brackets)

		try:
			if curly_brackets[0]:
				curly_brackets = []
				str_dict = string[iter_before :iter + 1].strip()
				dicts.append(ast.literal_eval(str_dict))
				iter_before = iter + 1
		except:
			pass

	return dicts

if __name__ == '__main__':
	dict_test = "{'hi' : 30, 'dict' : {'bye' : 40}}    \n\t{'last' : 3}"
	l = str_to_dict(dict_test)
	print(l)
	for dic in l:
		print(type(dic))