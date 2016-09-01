def sum_of_multiples(uptoNum, factors):
	res = []
	for factor in factors:
		res.extend(filter(lambda num: num%factor == 0, range(uptoNum))) if factor else res
	return sum(set(res))
