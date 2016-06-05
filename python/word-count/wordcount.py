import re

def word_count(sentence):
	unique_words = re.findall(r"[^\W_]+", sentence.decode('utf-8').lower(), flags=re.UNICODE)
	return {word : unique_words.count(word) for word in unique_words}