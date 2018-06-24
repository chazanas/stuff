import re

## read py file

def conflict_solver(path, head):
	'''(str, bool) -> none
	gets a conflicted path and undo its conflicts, choosing the first option if
	head is True, or the second when the oposite.
	'''

	code = open(path, 'r').read()

	regex = '>>+'


