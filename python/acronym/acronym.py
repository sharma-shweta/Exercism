getAcronym = lambda word : word[0].upper() if word.isupper() else word[0].upper() + ''.join(ch if ch.isupper() else '' for ch in word[1:])

def abbreviate(sentence):
	words = sentence.split(' ')
	acronym = ''
	for word in words:
		subWords = word.split('-')
		acronym += ''.join(getAcronym(subWord) for subWord in subWords)
	return acronym
