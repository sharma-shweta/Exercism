def distance(dna1, dna2):
	distance = 0
	for ch1, ch2 in zip(dna1, dna2):
		distance += 1 if ch1 != ch2 else 0
	return distance