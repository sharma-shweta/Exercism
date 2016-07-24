def slices(series, size):
	# Validate inputs
	if not size or size > len(series):
		raise ValueError

	result = []
	while len(series) >= size:
		result.append([int(series[i]) for i in range(size)])
		series = series[1:]
	return result
		
