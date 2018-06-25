import re

REGEX = '<<+ HEAD\n*(([^=]*\n*)*)\n+==+\n+(([^>]*\n*)*)\n+>>+ [\d,a,c,b,d,e,f,A,B,C,D,E,F]*'

## read py file

def conflict_solver(path, head):
	'''(str, bool) -> none
	gets a conflicted path and undo its conflicts, choosing the first option if
	head is True, or the second when the oposite.
	'''

	code = open(path, 'r').read()

	conflicts = re.search(REGEX, code)

	print(conflicts.group(1), '\n\n\n\n\n\n', conflicts.group(3))

if __name__ == '__main__':
	conflict_solver('./dammed.py', True)

	


