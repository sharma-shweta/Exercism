def detect_anagrams(word, possibleAnagrams):
	return [w for w in possibleAnagrams if isAnagram(word, w)]

def isAnagram(word1, word2):
	# Same words not anagram
	word1, word2 = word1.lower(), word2.lower()
	return word1 != word2 and sorted(word1) == sorted(word2)