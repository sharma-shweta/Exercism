import re

def hey(what):

	what = what.strip()
	
	if not what:
		return 'Fine. Be that way!'

	if what.isupper():
		return 'Whoa, chill out!'

	if '?' in what[-1]:
		return 'Sure.'
		
	return 'Whatever.'
