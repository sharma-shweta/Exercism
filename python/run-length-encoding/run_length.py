from itertools import groupby
import itertools

def encode(data):
	encoded_str = ''
	for char, count_iter in groupby(data):
		occurance = len(list(count_iter))
		encoded_str +=  str(occurance) if occurance > 1 else ''
		encoded_str += char
	return encoded_str

def decode(data):
	decoded_str = ''
	occurance = ''
	for char in data:
		if char.isdigit():
			occurance += char
		else:
			decoded_str += char*int((occurance) or '1')
			occurance = ''
	return decoded_str
