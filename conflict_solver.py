import os
import re

REGEX = '<<<+ HEAD\n*((?:[^=]*\n*)*)\n+===+\n+((?:[^>]*\n*)*)\n+>>>+ .+'

GROUP_CODE = {
	True : 1,
	False: 2
}

HEAD_STR = {
	True: 'HEAD',
	False: 'BRANCH'
}

CHECK_STR = {
	True: 'Are you sure you want to overwrite',
	False: 'Are you sure you want to save in'
}

VERBOSE_STR = {
	True: 'Overwriting',
	False: 'Saving in'
}

DO_CHECK = {
	'S' : True,
	'Y' : True,
	's' : True,
	'y' : True,
	'n' : False,
	'N' : False
}

def conflict_solver(path, 
					head, 
					exclude=False, 
					path_out='', 
					verbose=True, 
					check=True, 
					terminal=False):
	'''(str, bool) -> none
	gets a conflicted path and undo its conflicts, choosing the first option if
	head is True, or the second when the oposite.
	'''

	assert isinstance(head, bool), 'head argument must be a bool'
	assert isinstance(exclude, bool), 'exclude argument must be a bool'
	assert isinstance(path, str), 'path argument must be a string'
	assert isinstance(path_out, str), 'path_out argument must be a str'
	assert isinstance(verbose, bool), 'verbose argument must be a bool'
	assert isinstance(check, bool), 'check argument must be a bool'
	assert isinstance(terminal, bool), 'terminal argument must be a bool'


	try:
		file = open(path, 'r')
	except Exception as e:
		raise(e)


	code = file.read()

	code = conflicts = re.sub(REGEX, '\{}'.format(GROUP_CODE[head]), code)

	file.close()

	if exclude:
		out = path
	else:
		if len(path_out) > 0:
			out = path_out
		else:
			file_full = os.path.abspath(path)
			file_split = file_full.split('.')
			filename = file_split[0]
			ext = file_split[1]
			out = '{}_managed_{}.{}'.format(filename, HEAD_STR[head], ext)

	if check:
		save = input('{} {} like {} (s/n)? '.format(CHECK_STR[exclude], 
													out, 
													HEAD_STR[head]))
		while save not in list(DO_CHECK.keys()):
			print('The valid anwsers are {}.'.format(list(DO_CHECK.keys())))
			save = input('{} {} like {} (s/n)? '.format(CHECK_STR[exclude],
														out, 
														HEAD_STR[head]))
		save = DO_CHECK[save]
	else:
		save = True

	if save:
		if verbose:
			print('{} {} like {}.'.format(VERBOSE_STR[exclude], 
											out, 
											HEAD_STR[head]))

		file = open(out, 'w')
		file.write(code)
		file.close()
	else:
		if verbose:
			print('not saved')

	if terminal:
		print(code)

if __name__ == '__main__':
	conflict_solver('./dammed.py', True)

	


